"""
Unit tests for Occupant Comfort Model.
"""
import pytest
from app.optimization.comfort_model import ComfortModel

def test_comfort_within_bounds():
    model = ComfortModel(min_temp=22.0, max_temp=26.0)
    result = model.evaluate_comfort(temp=24.0, humidity=50.0, occupancy=10)
    assert result["comfort_violation"] is False
    assert result["comfort_score"] >= 95.0

def test_comfort_violation_when_occupied():
    model = ComfortModel(min_temp=22.0, max_temp=26.0)
    # Overheating
    hot_result = model.evaluate_comfort(temp=27.5, humidity=50.0, occupancy=5)
    assert hot_result["comfort_violation"] is True
    assert hot_result["comfort_score"] < 80.0

    # Overcooling
    cold_result = model.evaluate_comfort(temp=21.0, humidity=50.0, occupancy=5)
    assert cold_result["comfort_violation"] is True

def test_no_violation_when_unoccupied():
    model = ComfortModel(min_temp=22.0, max_temp=26.0)
    # When unoccupied, floating temperature should not count as occupant violation
    unoccupied_result = model.evaluate_comfort(temp=28.0, humidity=50.0, occupancy=0)
    assert unoccupied_result["comfort_violation"] is False
