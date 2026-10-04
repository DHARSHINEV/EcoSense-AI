"""
Integration tests for EcoSense AI FastAPI REST Endpoints.
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.data_store.db import data_store

@pytest.fixture(scope="module")
def client():
    # Ensure initialized with quick 3-day data for test suite speed
    with TestClient(app) as c:
        yield c

def test_health_endpoint(client):
    res = client.get("/health")
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "healthy"
    assert "EcoSense AI" in data["service"]

def test_building_summary(client):
    res = client.get("/api/building/summary")
    assert res.status_code == 200
    data = res.json()
    assert data["data_label"] == "SIMULATION RESULT"
    assert "total_baseline_energy_kwh" in data
    assert "total_optimized_energy_kwh" in data
    assert "comfort_compliance_pct" in data

def test_zones_list_and_detail(client):
    res = client.get("/api/zones")
    assert res.status_code == 200
    data = res.json()
    assert data["data_label"] == "SIMULATED DATA"
    assert len(data["zones"]) == 5
    first_zone_id = data["zones"][0]["zone_id"]

    # Test zone detail
    res_z = client.get(f"/api/zones/{first_zone_id}")
    assert res_z.status_code == 200
    z_data = res_z.json()
    assert z_data["zone_id"] == first_zone_id
    assert len(z_data["readings"]) > 0

def test_energy_analytics(client):
    res = client.get("/api/energy")
    assert res.status_code == 200
    data = res.json()
    assert "hourly_demand" in data
    assert "zone_breakdown" in data
    assert len(data["hourly_demand"]) == 24

def test_occupancy_analytics(client):
    res = client.get("/api/occupancy")
    assert res.status_code == 200
    data = res.json()
    assert "occupancy_by_zone" in data
    assert "occupancy_energy_correlation" in data

def test_ml_forecast_endpoint(client):
    res = client.get("/api/forecast")
    assert res.status_code == 200
    data = res.json()
    assert data["data_label"] == "MODEL PREDICTIONS"
    assert "mae_kw" in data
    assert "r2_score" in data
    assert len(data["forecast_points"]) > 0

def test_recommendations_and_action_flow(client):
    res = client.get("/api/recommendations")
    assert res.status_code == 200
    data = res.json()
    recs = data["recommendations"]
    assert len(recs) > 0
    rec_id = recs[0]["id"]

    # Building manager accepts recommendation
    action_res = client.post(f"/api/recommendations/{rec_id}/action", json={"status": "ACCEPTED"})
    assert action_res.status_code == 200
    assert action_res.json()["recommendation"]["status"] == "ACCEPTED"

    # Verify updated in recommendations list
    recs_after = client.get("/api/recommendations").json()["recommendations"]
    matching = [r for r in recs_after if r["id"] == rec_id]
    assert matching[0]["status"] == "ACCEPTED"

def test_scenarios_comparison(client):
    res = client.get("/api/comparison")
    assert res.status_code == 200
    scenarios = res.json()
    assert len(scenarios) == 4
    scen_ids = [s["scenario_id"] for s in scenarios]
    assert "scenario_a" in scen_ids
    assert "scenario_d" in scen_ids

def test_deployment_endpoints(client):
    res = client.get("/api/deployment")
    assert res.status_code == 200
    data = res.json()
    assert len(data["phases"]) == 4

    calc_res = client.post("/api/deployment/calculate", json={
        "building_area_sqm": 4000.0,
        "number_of_zones": 5,
        "sensor_count": 20,
        "estimated_sensor_cost_inr": 100000.0,
        "estimated_installation_inr": 50000.0,
        "software_annual_subscription_inr": 120000.0,
        "annual_energy_bill_inr": 3500000.0,
        "expected_savings_pct": 18.0
    })
    assert calc_res.status_code == 200
    calc_data = calc_res.json()
    assert calc_data["label"] == "Illustrative deployment estimate"
    assert calc_data["simple_payback_years"] > 0
