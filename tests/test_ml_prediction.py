"""
Unit tests for EcoSense AI Demand Prediction Engine.
"""
import pytest
from app.simulation.building_sim import BuildingSimulator
from app.simulation.baseline import calculate_baseline
from app.ml.demand_predictor import DemandPredictor

def test_ml_prediction_pipeline():
    sim = BuildingSimulator(random_seed=42, simulation_days=10)
    raw_df = sim.generate_raw_simulation_dataframe()
    b_df = calculate_baseline(raw_df)

    predictor = DemandPredictor()
    bldg_ts = predictor.prepare_building_timeseries(b_df)

    assert "lag_1h_power" in bldg_ts.columns
    assert "lag_24h_power" in bldg_ts.columns
    assert not bldg_ts["lag_1h_power"].isna().any()

    # Train model
    metrics = predictor.train(bldg_ts, test_ratio=0.25)

    assert "mae_kw" in metrics
    assert "rmse_kw" in metrics
    assert "r2_score" in metrics
    assert metrics["mae_kw"] > 0
    assert metrics["r2_score"] > 0.50, f"Model R² should be reasonable, got {metrics['r2_score']}"

    # Generate forecast
    forecast = predictor.predict_forecast(bldg_ts, horizon_hours=12)
    assert len(forecast) == 12
    for item in forecast:
        assert "predicted_demand_kw" in item
        assert "actual_simulated_demand_kw" in item
        assert "lower_bound_kw" in item
        assert "upper_bound_kw" in item
        assert item["lower_bound_kw"] <= item["predicted_demand_kw"] <= item["upper_bound_kw"]
        assert item["data_label"] == "MODEL PREDICTION"
