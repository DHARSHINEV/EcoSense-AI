"""
Unit tests for EcoSense AI Baseline Model.
"""
import pytest
from app.simulation.building_sim import BuildingSimulator
from app.simulation.baseline import calculate_baseline

def test_baseline_calculation():
    sim = BuildingSimulator(random_seed=42, simulation_days=3)
    raw_df = sim.generate_raw_simulation_dataframe()
    b_df = calculate_baseline(raw_df, min_comfort_temp=22.0, max_comfort_temp=26.0)

    assert "baseline_total_power_kw" in b_df.columns
    assert "baseline_energy_kwh" in b_df.columns
    assert "baseline_cost_inr" in b_df.columns
    assert "baseline_comfort_score" in b_df.columns
    assert "baseline_comfort_violation" in b_df.columns

    # Verify that during operating hours (weekday 07:00-19:00), baseline lighting is 100%
    work_hours = b_df[(~b_df["is_weekend"]) & (b_df["hour"].between(8, 18))]
    assert (work_hours["baseline_lighting_kw"] == work_hours["base_lighting_kw"]).all()

    # Off hours lighting should be standby (10%)
    night_hours = b_df[(~b_df["is_weekend"]) & (b_df["hour"] == 2)]
    assert (night_hours["baseline_lighting_kw"] < night_hours["base_lighting_kw"] * 0.15).all()

    # Baseline power is positive
    assert (b_df["baseline_total_power_kw"] > 0).all()
