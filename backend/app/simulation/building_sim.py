"""
EcoSense AI - Deterministic Building Simulation Engine.
Generates realistic hourly multi-zone building data with physical and behavioral realism.
Explicitly tagged as SIMULATED DATA.
"""
import math
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from typing import List, Dict, Any, Tuple
from app.config import settings

# Defined Zones with physical and electrical characteristics
ZONE_DEFINITIONS: Dict[str, Dict[str, Any]] = {
    "Lobby": {
        "zone_id": "z_lobby",
        "name": "Lobby",
        "floor_area_sqm": 400.0,
        "design_occupancy": 30,
        "base_lighting_kw": 3.2,
        "base_hvac_kw": 18.0,
        "base_plug_kw": 2.0,
        "thermal_mass_factor": 1.2,
        "profile_type": "transient_flow"
    },
    "Office Floor": {
        "zone_id": "z_office",
        "name": "Office Floor",
        "floor_area_sqm": 1800.0,
        "design_occupancy": 150,
        "base_lighting_kw": 14.5,
        "base_hvac_kw": 68.0,
        "base_plug_kw": 18.0,
        "thermal_mass_factor": 1.5,
        "profile_type": "standard_office"
    },
    "Meeting Room": {
        "zone_id": "z_meeting",
        "name": "Meeting Room",
        "floor_area_sqm": 120.0,
        "design_occupancy": 16,
        "base_lighting_kw": 1.8,
        "base_hvac_kw": 8.5,
        "base_plug_kw": 1.5,
        "thermal_mass_factor": 0.8,
        "profile_type": "episodic_meetings"
    },
    "Conference Room": {
        "zone_id": "z_conference",
        "name": "Conference Room",
        "floor_area_sqm": 320.0,
        "design_occupancy": 45,
        "base_lighting_kw": 4.0,
        "base_hvac_kw": 18.5,
        "base_plug_kw": 3.5,
        "thermal_mass_factor": 1.0,
        "profile_type": "sporadic_events"
    },
    "Cafeteria": {
        "zone_id": "z_cafeteria",
        "name": "Cafeteria",
        "floor_area_sqm": 600.0,
        "design_occupancy": 85,
        "base_lighting_kw": 5.0,
        "base_hvac_kw": 26.0,
        "base_plug_kw": 9.0,
        "thermal_mass_factor": 1.1,
        "profile_type": "meal_rush"
    }
}

class BuildingSimulator:
    def __init__(self, random_seed: int = 42, simulation_days: int = 30):
        self.seed = random_seed
        self.days = simulation_days
        self.rng = np.random.RandomState(self.seed)

    def _get_ambient_conditions(self, day_idx: int, hour: int) -> Tuple[float, float]:
        """
        Diurnal ambient outdoor temperature and relative humidity.
        Simulates warm/tropical climate: Daily high at 14:00, low at 05:00.
        """
        # Weekly weather front drift (+/- 3°C)
        weather_drift = 2.5 * math.sin(2 * math.pi * day_idx / 7.0)
        daily_noise = self.rng.normal(0, 0.6)
        
        # Diurnal curve: minimum at 5 AM, maximum at 2 PM (hour 14)
        diurnal_rad = 2 * math.pi * (hour - 5) / 24.0
        # Peak 35°C, trough 24°C on typical day
        mean_temp = 29.5 + weather_drift
        temp_amp = 5.5
        ambient_temp = mean_temp + temp_amp * math.cos(diurnal_rad - math.pi) + daily_noise
        ambient_temp = round(max(20.0, min(42.0, ambient_temp)), 1)

        # Humidity is inversely correlated with temperature
        mean_rh = 60.0 - weather_drift * 2.0
        rh_amp = 18.0
        humidity = mean_rh - rh_amp * math.cos(diurnal_rad - math.pi) + self.rng.normal(0, 2.0)
        humidity = round(max(30.0, min(85.0, humidity)), 1)

        return ambient_temp, humidity

    def _simulate_occupancy(self, profile_type: str, max_occ: int, hour: int, is_weekend: bool, day_idx: int) -> int:
        """
        Generate realistic zone occupancy based on zone archetype and time of day.
        """
        if is_weekend:
            # Minimal weekend skeleton staff (0-5% of max)
            if profile_type == "standard_office" and 10 <= hour <= 16:
                return int(self.rng.binomial(max_occ, 0.04))
            return 0

        # Weekday profiles
        if profile_type == "standard_office":
            if hour < 7 or hour >= 21:
                return 0
            elif 7 <= hour < 9:  # Arrival ramp
                ratio = 0.15 + 0.35 * (hour - 7) / 2.0
            elif 9 <= hour < 12:  # Morning peak
                ratio = 0.85 + self.rng.uniform(-0.08, 0.08)
            elif 12 <= hour < 14:  # Lunch dip
                ratio = 0.50 + self.rng.uniform(-0.06, 0.06)
            elif 14 <= hour < 18:  # Afternoon productive block
                ratio = 0.88 + self.rng.uniform(-0.06, 0.06)
            elif 18 <= hour < 20:  # Departure ramp
                ratio = 0.35 * (20 - hour) / 2.0
            else:
                ratio = 0.05
            occ = int(round(max_occ * max(0.0, min(1.0, ratio))))
            return occ

        elif profile_type == "transient_flow":  # Lobby
            if hour < 6 or hour >= 22:
                return 0
            if hour in [8, 9, 13, 17, 18]:  # Peak flow times
                ratio = 0.65 + self.rng.uniform(-0.15, 0.15)
            elif 9 < hour < 17:
                ratio = 0.30 + self.rng.uniform(-0.08, 0.08)
            else:
                ratio = 0.10
            return int(round(max_occ * max(0.0, min(1.0, ratio))))

        elif profile_type == "episodic_meetings":  # Meeting Room
            if hour < 9 or hour >= 19:
                return 0
            # Discrete meeting blocks: meetings occur with 60% probability per work hour
            # Use deterministic pseudo-random per hour/day
            meeting_active = self.rng.rand() < 0.62
            if meeting_active:
                ratio = self.rng.uniform(0.40, 0.95)
            else:
                ratio = 0.0
            return int(round(max_occ * ratio))

        elif profile_type == "sporadic_events":  # Conference Room
            if hour < 10 or hour >= 18:
                return 0
            # Town halls or large team reviews: 2-3 events per week
            event_active = (day_idx % 2 == 1) and (hour in [11, 14, 15, 16]) and (self.rng.rand() < 0.70)
            if event_active:
                ratio = self.rng.uniform(0.60, 0.95)
            else:
                ratio = 0.0
            return int(round(max_occ * ratio))

        elif profile_type == "meal_rush":  # Cafeteria
            if 12 <= hour <= 14:  # Lunch peak
                ratio = 0.75 + self.rng.uniform(-0.15, 0.15)
            elif hour in [10, 16]:  # Tea/coffee breaks
                ratio = 0.35 + self.rng.uniform(-0.10, 0.10)
            elif 8 <= hour < 18:
                ratio = 0.10
            else:
                ratio = 0.0
            return int(round(max_occ * max(0.0, min(1.0, ratio))))

        return 0

    def generate_raw_simulation_dataframe(self, start_date: datetime = datetime(2026, 9, 1, 0, 0)) -> pd.DataFrame:
        """
        Generate complete hourly dataset for all zones over simulation_days.
        Includes simulated occupancy, environmental variables, and default operational patterns.
        """
        rows = []
        total_hours = self.days * 24

        for zone_name, zone_meta in ZONE_DEFINITIONS.items():
            # Reset random stream for consistency across zones
            self.rng = np.random.RandomState(self.seed + hash(zone_name) % 10000)
            
            zone_id = zone_meta["zone_id"]
            max_occ = zone_meta["design_occupancy"]
            base_lighting = zone_meta["base_lighting_kw"]
            base_hvac = zone_meta["base_hvac_kw"]
            base_plug = zone_meta["base_plug_kw"]
            profile_type = zone_meta["profile_type"]

            # Initial thermal state
            current_zone_temp = 24.5

            for h_idx in range(total_hours):
                current_time = start_date + timedelta(hours=h_idx)
                day_idx = h_idx // 24
                hour = current_time.hour
                day_of_week = current_time.weekday()  # 0=Monday, 6=Sunday
                is_weekend = day_of_week >= 5

                ambient_temp, humidity = self._get_ambient_conditions(day_idx, hour)
                occupancy = self._simulate_occupancy(profile_type, max_occ, hour, is_weekend, day_idx)
                occupancy_ratio = occupancy / max_occ if max_occ > 0 else 0.0

                # Simulated Indoor Air Quality indicator (CO2 ppm equivalent: 400 outdoors to 1200+ with high occupancy)
                base_co2 = 420.0
                co2_generation = occupancy * 14.5
                iaq_indicator = base_co2 + co2_generation + self.rng.normal(0, 15.0)
                iaq_indicator = round(max(400.0, min(1400.0, iaq_indicator)), 1)

                rows.append({
                    "timestamp": current_time.isoformat(),
                    "date_str": current_time.strftime("%Y-%m-%d"),
                    "hour": hour,
                    "day_of_week": day_of_week,
                    "is_weekend": is_weekend,
                    "zone_id": zone_id,
                    "zone_name": zone_name,
                    "occupancy": occupancy,
                    "occupancy_ratio": round(occupancy_ratio, 3),
                    "ambient_temp": ambient_temp,
                    "humidity": humidity,
                    "iaq_score": iaq_indicator,
                    "base_lighting_kw": base_lighting,
                    "base_hvac_kw": base_hvac,
                    "base_plug_kw": base_plug,
                    "floor_area_sqm": zone_meta["floor_area_sqm"],
                    "design_occupancy": max_occ,
                    "data_label": "SIMULATED DATA"
                })

        df = pd.DataFrame(rows)
        return df

sim_engine = BuildingSimulator(settings.random_seed, settings.simulation_days)
