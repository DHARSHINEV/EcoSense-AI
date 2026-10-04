"""
Unit tests for EcoSense AI Data Simulation Engine.
"""
import pytest
import pandas as pd
from app.simulation.building_sim import BuildingSimulator, ZONE_DEFINITIONS

def test_deterministic_simulation_reproducibility():
    """Verify that identical random seeds generate identical data."""
    sim1 = BuildingSimulator(random_seed=42, simulation_days=2)
    sim2 = BuildingSimulator(random_seed=42, simulation_days=2)

    df1 = sim1.generate_raw_simulation_dataframe()
    df2 = sim2.generate_raw_simulation_dataframe()

    pd.testing.assert_frame_equal(df1, df2)

def test_simulation_shape_and_columns():
    """Verify total rows, days, zones and column integrity."""
    days = 5
    sim = BuildingSimulator(random_seed=123, simulation_days=days)
    df = sim.generate_raw_simulation_dataframe()

    expected_rows = days * 24 * len(ZONE_DEFINITIONS)
    assert len(df) == expected_rows, f"Expected {expected_rows} rows, got {len(df)}"

    required_cols = [
        "timestamp", "date_str", "hour", "day_of_week", "is_weekend",
        "zone_id", "zone_name", "occupancy", "occupancy_ratio",
        "ambient_temp", "humidity", "iaq_score", "data_label"
    ]
    for col in required_cols:
        assert col in df.columns, f"Missing required column: {col}"
    assert (df["data_label"] == "SIMULATED DATA").all()

def test_physical_plausibility():
    """Verify that physical values stay within realistic ranges."""
    sim = BuildingSimulator(random_seed=42, simulation_days=7)
    df = sim.generate_raw_simulation_dataframe()

    assert (df["occupancy"] >= 0).all()
    assert (df["ambient_temp"] >= 15.0).all() and (df["ambient_temp"] <= 45.0).all()
    assert (df["humidity"] >= 20.0).all() and (df["humidity"] <= 95.0).all()
    assert (df["iaq_score"] >= 380.0).all() and (df["iaq_score"] <= 1500.0).all()

def test_weekend_occupancy_reduction():
    """Verify that weekends exhibit vastly lower occupancy than weekday peak hours."""
    sim = BuildingSimulator(random_seed=42, simulation_days=7)
    df = sim.generate_raw_simulation_dataframe()

    weekday_peak = df[(~df["is_weekend"]) & (df["hour"].between(10, 16))]["occupancy"].mean()
    weekend_day = df[(df["is_weekend"]) & (df["hour"].between(10, 16))]["occupancy"].mean()

    assert weekday_peak > weekend_day * 4.0, "Weekday peak occupancy must be significantly higher than weekend"
