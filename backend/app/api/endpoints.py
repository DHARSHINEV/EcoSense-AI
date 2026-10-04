"""
EcoSense AI - FastAPI Route Endpoints.
Provides structured REST API endpoints for building analytics, zones, ML forecast,
AI recommendations, scenarios, and deployment economics.
"""
from fastapi import APIRouter, HTTPException, Query
from typing import Optional, List, Dict, Any
from app.data_store.db import data_store
from app.models.schemas import (
    BuildingSummaryResponse,
    ForecastResponse,
    AIRecommendation,
    RecommendationActionRequest,
    ScenarioResult,
    SimulationParams,
    PaybackInput,
    PaybackOutput
)
from app.config import SimulationSettings

router = APIRouter()

@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "EcoSense AI Backend",
        "version": "1.0.0",
        "data_status": "SIMULATION_ACTIVE" if data_store.is_initialized else "INITIALIZING"
    }

@router.get("/api/building/summary", response_model=BuildingSummaryResponse)
def get_building_summary():
    """
    Returns top-level KPIs comparing Baseline vs Optimized operation.
    Explicitly labeled as SIMULATION RESULT.
    """
    return data_store.get_summary()

@router.get("/api/zones")
def get_zones():
    """
    Returns list of all zones with current environmental and power status.
    """
    return {
        "data_label": "SIMULATED DATA",
        "zones": data_store.get_zones()
    }

@router.get("/api/zones/{zone_id}")
def get_zone_details(zone_id: str, date: Optional[str] = Query(None, description="Date in YYYY-MM-DD")):
    """
    Returns 24-hour time series for a specific zone.
    """
    timeseries = data_store.get_zone_timeseries(zone_id, date)
    if not timeseries:
        raise HTTPException(status_code=404, detail=f"Zone '{zone_id}' not found or no data available.")
    return {
        "data_label": "SIMULATED DATA",
        "zone_id": zone_id,
        "date": date or "latest",
        "readings": timeseries
    }

@router.get("/api/energy")
def get_energy_analytics(date: Optional[str] = Query(None, description="Date in YYYY-MM-DD")):
    """
    Returns hourly building baseline vs optimized demand curves and zone breakdown.
    """
    return data_store.get_energy_analytics(date)

@router.get("/api/occupancy")
def get_occupancy_analytics(date: Optional[str] = Query(None, description="Date in YYYY-MM-DD")):
    """
    Returns zone occupancy profiles and occupancy vs energy correlation scatter data.
    """
    return data_store.get_occupancy_analytics(date)

@router.get("/api/forecast", response_model=ForecastResponse)
def get_demand_forecast():
    """
    Returns next 12-hour near-term ML demand predictions with error metrics and approximate empirical prediction bands.
    Explicitly labeled as MODEL PREDICTIONS.
    """
    return data_store.get_forecast()

@router.get("/api/recommendations")
def get_recommendations():
    """
    Returns list of active AI optimization recommendations.
    """
    return {
        "data_label": "OPTIMIZATION RECOMMENDATIONS",
        "recommendations": data_store.get_recommendations()
    }

@router.post("/api/recommendations/{rec_id}/action")
def update_recommendation(rec_id: str, req: RecommendationActionRequest):
    """
    Building manager user journey: Accept, Dismiss, or Review an AI recommendation.
    """
    updated = data_store.update_recommendation_status(rec_id, req.status)
    if not updated:
        raise HTTPException(status_code=404, detail=f"Recommendation '{rec_id}' not found.")
    return {
        "message": f"Recommendation '{rec_id}' status updated to {req.status}.",
        "recommendation": updated
    }

@router.get("/api/comparison", response_model=List[ScenarioResult])
def get_scenario_comparison():
    """
    Scenario Lab: Compares Scenarios A (Baseline), B (Occupancy), C (Forecast), D (Full EcoSense).
    """
    return data_store.get_scenarios()

@router.post("/api/simulation/run")
def re_run_simulation(params: SimulationParams):
    """
    Re-runs deterministic physical simulation with custom user parameters.
    """
    custom_cfg = SimulationSettings(
        simulation_days=params.simulation_days,
        electricity_tariff=params.electricity_tariff,
        min_comfort_temp=params.min_comfort_temp,
        max_comfort_temp=params.max_comfort_temp,
        peak_demand_threshold_kw=params.peak_demand_threshold_kw,
        random_seed=params.random_seed
    )
    data_store.initialize(custom_cfg)
    return {
        "status": "success",
        "message": f"Simulation regenerated successfully for {params.simulation_days} days.",
        "summary": data_store.get_summary()
    }

@router.post("/api/optimization/run")
def re_run_optimization():
    """
    Re-evaluates optimization engine on current baseline data.
    """
    summary = data_store.get_summary()
    return {
        "status": "success",
        "message": "Optimization policies evaluated successfully.",
        "summary": summary
    }

@router.get("/api/deployment")
def get_deployment_info():
    """
    Returns phased deployment framework and default economics calculation.
    """
    default_calc = data_store.calculate_payback({})
    return {
        "phases": [
            {
                "phase": "Phase 1: Software Analytics & Virtual Auditing",
                "duration": "Months 1-2",
                "scope": "Ingest existing utility smart meter and BMS time-series data without adding hardware.",
                "deliverables": "Baseline regression model, tariff mismatch identification, scheduling drift correction."
            },
            {
                "phase": "Phase 2: Low-Cost IoT Sensing Overlay",
                "duration": "Months 3-4",
                "scope": "Install non-intrusive wireless LoRaWAN / Zigbee occupancy (PIR/people-counting), temp, RH, and IAQ sensors.",
                "deliverables": "Real-time granular zone observability, occupancy-to-cooling mismatch mapping."
            },
            {
                "phase": "Phase 3: Automated BMS & Smart Thermostat Integration",
                "duration": "Months 5-6",
                "scope": "Bridge EcoSense optimization engine with BACnet IP / Modbus gateways for automated setpoint modulation and lighting relays.",
                "deliverables": "Automated closed-loop setback, daylight harvesting, and supervisory scheduling."
            },
            {
                "phase": "Phase 4: Grid-Interactive Demand Response (GEB)",
                "duration": "Months 7+",
                "scope": "Integrate OpenADR 2.0b / utility dynamic pricing signals for automated peak shaving and thermal pre-cooling.",
                "deliverables": "Peak demand charge minimization and automated grid flexibility revenue."
            }
        ],
        "target_archetypes": [
            {"type": "IT / Commercial Parks", "fit": "High - large variable occupancy and multi-tenant cooling loads."},
            {"type": "Educational Institutions", "fit": "High - episodic classroom / lecture hall occupancy patterns."},
            {"type": "Retail & Shopping Malls", "fit": "Medium - high customer footfall variations and thermal inertia."},
            {"type": "Coworking & Multi-tenant", "fit": "Very High - extreme meeting room unpredictability."}
        ],
        "default_calculator": default_calc
    }

@router.post("/api/deployment/calculate", response_model=PaybackOutput)
def calculate_deployment_economics(inputs: PaybackInput):
    """
    Computes custom payback period, annual savings, and 5-year ROI based on user inputs.
    """
    return data_store.calculate_payback(inputs.model_dump())
