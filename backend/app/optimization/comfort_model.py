"""
EcoSense AI - Occupant Comfort Modeling Module.
Evaluates thermal comfort compliance, scores, and violation tracking.
All metrics explicitly labeled as SIMULATION RESULT.
"""
import numpy as np
from typing import Dict, Any

class ComfortModel:
    def __init__(self, min_temp: float = 22.0, max_temp: float = 26.0, target_temp: float = 24.0):
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.target_temp = target_temp

    def evaluate_comfort(self, temp: float, humidity: float, occupancy: int) -> Dict[str, Any]:
        """
        Evaluates thermal comfort for a zone reading.
        Comfort violation only occurs during occupied hours if temperature falls outside [min_temp, max_temp].
        Score is 0-100, where 100 is ideal thermal comfort.
        """
        is_occupied = occupancy > 0
        violation = False

        if is_occupied:
            if temp < self.min_temp or temp > self.max_temp:
                violation = True

        # Deviation from ideal 24°C
        temp_diff = abs(temp - self.target_temp)
        # Humidity penalty if outside 40-60% RH
        rh_penalty = 0.0
        if humidity < 35.0:
            rh_penalty = (35.0 - humidity) * 0.4
        elif humidity > 65.0:
            rh_penalty = (humidity - 65.0) * 0.4

        raw_score = 100.0 - (temp_diff ** 1.8) * 10.0 - rh_penalty
        comfort_score = round(float(np.clip(raw_score, 20.0, 100.0)), 1)

        return {
            "comfort_score": comfort_score,
            "comfort_violation": violation,
            "is_within_bounds": not violation if is_occupied else True,
            "min_comfort_temp": self.min_temp,
            "max_comfort_temp": self.max_temp
        }
