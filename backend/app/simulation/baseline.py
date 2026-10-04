"""
EcoSense AI - Baseline Model Engine.
Simulates conventional fixed-schedule building operation without occupancy-awareness or peak management.
Explicitly tagged as SIMULATION RESULT.
"""
import pandas as pd
import numpy as np
from typing import Dict, Any
from app.config import settings

def calculate_baseline(raw_df: pd.DataFrame, 
                       min_comfort_temp: float = settings.min_comfort_temp,
                       max_comfort_temp: float = settings.max_comfort_temp,
                       electricity_tariff: float = settings.electricity_tariff,
                       co2_factor: float = settings.co2_factor) -> pd.DataFrame:
    """
    Computes baseline energy consumption for each zone reading under standard fixed-schedule assumptions:
    - Fixed operating schedule: 07:00 to 20:00 on weekdays (Mon-Fri).
    - Fixed cooling setpoint: 22.0°C regardless of occupancy.
    - Fixed 100% lighting during operating hours regardless of occupancy or daylight.
    - Standby night/weekend loads: 5% HVAC standby, 10% emergency lighting, 20% base plug load.
    - Zero peak demand optimization.
    """
    df = raw_df.copy()

    # Determine operating hours: Weekdays 07:00 to 20:00
    is_operating_hours = (~df["is_weekend"]) & (df["hour"] >= settings.operating_start_hour) & (df["hour"] < settings.operating_end_hour)

    # 1. Baseline HVAC Power (kW)
    # Under fixed schedule, HVAC runs whenever within operating hours, maintaining 22°C setpoint
    fixed_setpoint = 22.0
    cooling_delta = np.maximum(0.0, df["ambient_temp"] - fixed_setpoint)
    # Cooling load fraction from ambient heat gain + internal occupant heat load
    cooling_factor = 0.50 + 0.45 * (cooling_delta / 16.0) + 0.15 * df["occupancy_ratio"]
    cooling_factor = np.clip(cooling_factor, 0.35, 1.0)

    # When operating, consumes base_hvac * cooling_factor; when off, consumes 5% standby
    df["baseline_hvac_kw"] = np.where(
        is_operating_hours,
        df["base_hvac_kw"] * cooling_factor,
        df["base_hvac_kw"] * 0.05
    )

    # 2. Baseline Lighting Power (kW)
    # 100% full blast during all operating hours regardless of occupancy; 10% overnight
    df["baseline_lighting_kw"] = np.where(
        is_operating_hours,
        df["base_lighting_kw"] * 1.0,
        df["base_lighting_kw"] * 0.10
    )

    # 3. Baseline Plug Load (kW)
    # 85% during operating hours, 20% standby overnight
    df["baseline_plug_kw"] = np.where(
        is_operating_hours,
        df["base_plug_kw"] * 0.85,
        df["base_plug_kw"] * 0.20
    )

    # Total baseline power & energy
    df["baseline_total_power_kw"] = df["baseline_hvac_kw"] + df["baseline_lighting_kw"] + df["baseline_plug_kw"]
    df["baseline_energy_kwh"] = df["baseline_total_power_kw"] * 1.0  # 1 hour intervals

    # Baseline Zone Temperature (°C)
    # Actively cooled to ~22.0°C during operating hours (sometimes slightly overcooled 21.5°C)
    # In off-hours, drifts toward ambient
    df["baseline_zone_temp"] = np.where(
        is_operating_hours,
        22.0 + np.random.RandomState(42).normal(0.0, 0.4, len(df)),
        df["ambient_temp"] * 0.70 + 22.0 * 0.30
    )
    df["baseline_zone_temp"] = df["baseline_zone_temp"].round(1)

    # Baseline Comfort Violations (evaluated when occupants are present)
    # In baseline, occupants frequently experience overcooling (< 22.0°C) or off-hour overheating
    temp = df["baseline_zone_temp"]
    is_occupied = df["occupancy"] > 0
    temp_violation = is_occupied & ((temp < min_comfort_temp) | (temp > max_comfort_temp))
    df["baseline_comfort_violation"] = temp_violation

    # Comfort score (0-100): 100 when exactly at target (24°C), penalized for deviation
    temp_diff = np.abs(df["baseline_zone_temp"] - 24.0)
    df["baseline_comfort_score"] = np.clip(100.0 - (temp_diff ** 1.8) * 12.0, 30.0, 100.0).round(1)

    # Baseline Operating Cost & CO2
    df["baseline_cost_inr"] = (df["baseline_energy_kwh"] * electricity_tariff).round(2)
    df["baseline_co2_kg"] = (df["baseline_energy_kwh"] * co2_factor).round(2)

    return df
