"""
EcoSense AI - Configuration and Global Settings
"""
from pydantic import BaseModel
from typing import List

class SimulationSettings(BaseModel):
    random_seed: int = 42
    simulation_days: int = 30
    zones: List[str] = [
        "Lobby",
        "Office Floor",
        "Meeting Room",
        "Conference Room",
        "Cafeteria"
    ]
    min_comfort_temp: float = 22.0  # °C
    max_comfort_temp: float = 26.0  # °C
    target_comfort_temp: float = 24.0  # °C
    electricity_tariff: float = 8.50  # ₹/kWh (Indian Commercial Grid standard)
    co2_factor: float = 0.82  # kg CO2 / kWh (CEA Baseline Database for Indian Grid)
    peak_demand_threshold_kw: float = 175.0  # kW building peak trigger
    operating_start_hour: int = 7  # 07:00
    operating_end_hour: int = 20  # 20:00
    hvac_cop: float = 3.2  # Coefficient of performance

settings = SimulationSettings()
