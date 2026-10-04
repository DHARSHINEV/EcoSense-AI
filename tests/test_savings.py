"""
Unit tests for EcoSense AI Savings and Payback Calculation.
"""
import pytest
from app.data_store.db import BuildingDataStore
from app.config import SimulationSettings

def test_savings_calculation_and_labels():
    store = BuildingDataStore()
    cfg = SimulationSettings(simulation_days=4, electricity_tariff=10.0, co2_factor=0.82)
    store.initialize(cfg)

    summary = store.get_summary()

    assert summary["data_label"] == "SIMULATION RESULT"
    assert summary["total_baseline_energy_kwh"] > summary["total_optimized_energy_kwh"]
    assert summary["total_energy_saved_kwh"] > 0
    assert summary["energy_reduction_pct"] > 0
    assert summary["baseline_cost_inr"] > summary["optimized_cost_inr"]
    assert summary["cost_savings_inr"] > 0
    assert summary["co2_reduction_kg"] > 0

    # Verify exact tariff math
    expected_saved_cost = summary["total_energy_saved_kwh"] * 10.0
    assert abs(summary["cost_savings_inr"] - expected_saved_cost) < 5.0

def test_payback_calculator():
    store = BuildingDataStore()
    payback = store.calculate_payback({
        "estimated_sensor_cost_inr": 100000.0,
        "estimated_installation_inr": 50000.0,
        "software_annual_subscription_inr": 150000.0,
        "annual_energy_bill_inr": 3000000.0,
        "expected_savings_pct": 20.0
    })

    assert payback["label"] == "Illustrative deployment estimate"
    assert payback["upfront_capex_inr"] == 150000.0
    assert payback["estimated_annual_savings_inr"] == 600000.0
    assert payback["net_annual_benefit_inr"] == 450000.0
    assert payback["simple_payback_years"] == round(150000.0 / 450000.0, 2)
    assert payback["five_year_net_savings_inr"] == (450000.0 * 5.0) - 150000.0
