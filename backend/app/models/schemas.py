"""
Pydantic schemas and data contracts for EcoSense AI.
Explicitly enforces labeling for SIMULATED DATA, MODEL PREDICTIONS, and SIMULATION RESULT.
"""
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

class ZoneMeta(BaseModel):
    zone_id: str
    name: str
    floor_area_sqm: float
    design_occupancy: int
    base_lighting_kw: float
    base_hvac_kw: float
    base_plug_kw: float

class HourlyZoneReading(BaseModel):
    timestamp: str
    date_str: str
    hour: int
    day_of_week: int
    is_weekend: bool
    zone_id: str
    zone_name: str
    occupancy: int
    occupancy_ratio: float
    ambient_temp: float
    zone_temp: float
    humidity: float
    iaq_score: float  # e.g., 400-1200 ppm CO2 indicator
    hvac_power_kw: float
    lighting_power_kw: float
    plug_load_kw: float
    total_power_kw: float
    energy_kwh: float
    comfort_score: float
    comfort_violation: bool
    data_label: str = "SIMULATED DATA"

class HourlyBuildingDemand(BaseModel):
    timestamp: str
    date_str: str
    hour: int
    day_of_week: int
    is_weekend: bool
    total_occupancy: int
    baseline_power_kw: float
    optimized_power_kw: float
    demand_reduction_kw: float
    is_peak: bool
    ambient_temp: float
    data_label: str = "SIMULATION RESULT"

class AIRecommendation(BaseModel):
    id: str
    timestamp: str
    zone_id: str
    zone_name: str
    title: str
    reason: str
    action_type: str  # HVAC_SETBACK, LIGHTING_DIM, PEAK_LOAD_SHED, PRE_COOLING
    expected_kw_savings: float
    expected_cost_savings_inr: float
    comfort_impact: str
    peak_demand_impact: str
    priority: str  # HIGH, MEDIUM, LOW
    status: str = "PENDING"  # PENDING, ACCEPTED, DISMISSED, REVIEWED
    data_label: str = "OPTIMIZATION RECOMMENDATION"

class RecommendationActionRequest(BaseModel):
    status: str = Field(..., pattern="^(ACCEPTED|DISMISSED|REVIEWED)$")

class BuildingSummaryResponse(BaseModel):
    data_label: str = "SIMULATION RESULT"
    date_range: str
    total_baseline_energy_kwh: float
    total_optimized_energy_kwh: float
    total_energy_saved_kwh: float
    energy_reduction_pct: float
    baseline_peak_kw: float
    optimized_peak_kw: float
    peak_reduction_pct: float
    baseline_cost_inr: float
    optimized_cost_inr: float
    cost_savings_inr: float
    co2_reduction_kg: float
    comfort_compliance_pct: float
    total_comfort_violations: int
    current_occupancy: int
    current_total_power_kw: float
    current_baseline_power_kw: float
    current_savings_kw: float
    active_recommendations_count: int
    electricity_tariff: float
    co2_factor: float
    comfort_range: str

class ForecastItem(BaseModel):
    timestamp: str
    hour: int
    predicted_demand_kw: float
    actual_simulated_demand_kw: float
    error_kw: float
    lower_bound_kw: float
    upper_bound_kw: float
    data_label: str = "MODEL PREDICTION"

class ForecastResponse(BaseModel):
    data_label: str = "MODEL PREDICTIONS"
    model_name: str = "RandomForestRegressor (Trained on Simulated Time-Series)"
    mae_kw: float
    rmse_kw: float
    r2_score: float
    horizon_hours: int
    forecast_points: List[ForecastItem]
    features_used: List[str]

class ScenarioResult(BaseModel):
    scenario_id: str
    name: str
    description: str
    total_energy_kwh: float
    peak_demand_kw: float
    total_cost_inr: float
    comfort_compliance_pct: float
    energy_savings_pct: float
    cost_savings_inr: float
    co2_reduction_kg: float
    data_label: str = "SIMULATION RESULT"

class SimulationParams(BaseModel):
    simulation_days: int = 30
    electricity_tariff: float = 8.50
    min_comfort_temp: float = 22.0
    max_comfort_temp: float = 26.0
    peak_demand_threshold_kw: float = 175.0
    random_seed: int = 42

class PaybackInput(BaseModel):
    building_area_sqm: float = 5000.0
    number_of_zones: int = 5
    sensor_count: int = 25
    estimated_sensor_cost_inr: float = 125000.0  # ₹5,000 / sensor
    estimated_installation_inr: float = 75000.0
    software_annual_subscription_inr: float = 180000.0  # ₹15,000 / month
    annual_energy_bill_inr: float = 4200000.0  # Typical commercial facility bill
    expected_savings_pct: float = 18.5  # From simulation

class PaybackOutput(BaseModel):
    label: str = "Illustrative deployment estimate"
    upfront_capex_inr: float
    annual_opex_inr: float
    estimated_annual_savings_inr: float
    net_annual_benefit_inr: float
    simple_payback_years: float
    five_year_net_savings_inr: float
    five_year_roi_pct: float
