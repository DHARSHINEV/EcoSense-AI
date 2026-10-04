"""
Unit tests for EcoSense AI Multi-Objective Optimization Engine.
"""
import pytest
from app.simulation.building_sim import BuildingSimulator
from app.simulation.baseline import calculate_baseline
from app.optimization.engine import OptimizationEngine

def test_optimization_reduces_energy():
    sim = BuildingSimulator(random_seed=42, simulation_days=3)
    raw_df = sim.generate_raw_simulation_dataframe()
    b_df = calculate_baseline(raw_df)

    opt_engine = OptimizationEngine()
    opt_df, recs = opt_engine.optimize_building_dataframe(b_df)

    tot_base_kwh = b_df["baseline_energy_kwh"].sum()
    tot_opt_kwh = opt_df["opt_energy_kwh"].sum()

    assert tot_opt_kwh < tot_base_kwh, "Optimized energy must be lower than baseline"
    savings_pct = (tot_base_kwh - tot_opt_kwh) / tot_base_kwh * 100.0
    assert 10.0 <= savings_pct <= 35.0, f"Expected realistic 10-35% savings, got {savings_pct}%"

def test_peak_demand_reduction():
    sim = BuildingSimulator(random_seed=42, simulation_days=5)
    raw_df = sim.generate_raw_simulation_dataframe()
    b_df = calculate_baseline(raw_df)

    opt_engine = OptimizationEngine(peak_threshold_kw=160.0)
    opt_df, recs = opt_engine.optimize_building_dataframe(b_df)

    base_peak = b_df.groupby("timestamp")["baseline_total_power_kw"].sum().max()
    opt_peak = opt_df.groupby("timestamp")["opt_total_power_kw"].sum().max()

    assert opt_peak < base_peak, f"Optimized peak ({opt_peak} kW) should be less than baseline ({base_peak} kW)"

def test_ai_recommendations_structure():
    sim = BuildingSimulator(random_seed=42, simulation_days=3)
    raw_df = sim.generate_raw_simulation_dataframe()
    b_df = calculate_baseline(raw_df)

    opt_engine = OptimizationEngine()
    _, recs = opt_engine.optimize_building_dataframe(b_df)

    assert len(recs) > 0, "Optimization engine should generate actionable recommendations"
    for r in recs:
        assert "id" in r
        assert "title" in r
        assert "reason" in r
        assert "expected_kw_savings" in r
        assert "comfort_impact" in r
        assert "peak_demand_impact" in r
        assert r["status"] in ["PENDING", "ACCEPTED", "DISMISSED", "REVIEWED"]
        assert r["data_label"] == "OPTIMIZATION RECOMMENDATION"
