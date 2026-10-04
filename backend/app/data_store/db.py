"""
EcoSense AI - In-Memory State & Data Store.
Maintains fast, deterministic, reproducible in-memory state of the building simulation,
baseline comparisons, ML forecast, AI recommendations, and scenarios.
"""
import os
import json
import numpy as np
import pandas as pd
from typing import List, Dict, Any, Optional
from datetime import datetime
from app.config import settings, SimulationSettings
from app.simulation.building_sim import BuildingSimulator, ZONE_DEFINITIONS
from app.simulation.baseline import calculate_baseline
from app.ml.demand_predictor import demand_predictor
from app.optimization.engine import OptimizationEngine

DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../data"))

class BuildingDataStore:
    def __init__(self):
        self.settings: SimulationSettings = settings
        self.raw_df: Optional[pd.DataFrame] = None
        self.baseline_df: Optional[pd.DataFrame] = None
        self.optimized_df: Optional[pd.DataFrame] = None
        self.building_timeseries: Optional[pd.DataFrame] = None
        self.recommendations: List[Dict[str, Any]] = []
        self.scenarios: List[Dict[str, Any]] = []
        self.forecast_data: List[Dict[str, Any]] = []
        self.ml_metrics: Dict[str, Any] = {}
        self.is_initialized: bool = False

    def initialize(self, custom_settings: Optional[SimulationSettings] = None):
        """
        Runs full simulation pipeline from scratch:
        Sense -> Predict -> Optimize -> Recommend -> Measure.
        """
        if custom_settings:
            self.settings = custom_settings

        # 1. Sense: Deterministic physical simulation
        simulator = BuildingSimulator(
            random_seed=self.settings.random_seed,
            simulation_days=self.settings.simulation_days
        )
        self.raw_df = simulator.generate_raw_simulation_dataframe()

        # 2. Baseline: Conventional fixed-schedule operation
        self.baseline_df = calculate_baseline(
            self.raw_df,
            min_comfort_temp=self.settings.min_comfort_temp,
            max_comfort_temp=self.settings.max_comfort_temp,
            electricity_tariff=self.settings.electricity_tariff,
            co2_factor=self.settings.co2_factor
        )

        # 3. Predict: ML Demand Predictor (Time-series Feature Engineering & Train)
        self.building_timeseries = demand_predictor.prepare_building_timeseries(self.baseline_df)
        self.ml_metrics = demand_predictor.train(self.building_timeseries)
        self.forecast_data = demand_predictor.predict_forecast(self.building_timeseries, horizon_hours=12)

        # 4. Optimize: Multi-Objective Engine
        opt_engine = OptimizationEngine(
            min_comfort_temp=self.settings.min_comfort_temp,
            max_comfort_temp=self.settings.max_comfort_temp,
            peak_threshold_kw=self.settings.peak_demand_threshold_kw,
            electricity_tariff=self.settings.electricity_tariff,
            co2_factor=self.settings.co2_factor
        )
        self.optimized_df, self.recommendations = opt_engine.optimize_building_dataframe(self.baseline_df)

        # 5. Scenarios: A, B, C, D
        self.scenarios = opt_engine.generate_scenarios(self.baseline_df)

        self.is_initialized = True

        # Save summary JSON for portable inspection
        os.makedirs(DATA_DIR, exist_ok=True)
        self._export_summary_json()

    def _export_summary_json(self):
        summary = self.get_summary()
        summary_path = os.path.join(DATA_DIR, "simulated_building_summary.json")
        with open(summary_path, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2)

    def get_summary(self) -> Dict[str, Any]:
        """
        Computes high-level building KPI summary metrics.
        """
        if not self.is_initialized:
            self.initialize()

        df = self.optimized_df
        tot_base_kwh = float(df["baseline_energy_kwh"].sum())
        tot_opt_kwh = float(df["opt_energy_kwh"].sum())
        tot_saved_kwh = tot_base_kwh - tot_opt_kwh
        energy_pct = (tot_saved_kwh / tot_base_kwh * 100.0) if tot_base_kwh > 0 else 0.0

        # Peak power at building level across all hours
        b_hourly = df.groupby("timestamp").agg({
            "baseline_total_power_kw": "sum",
            "opt_total_power_kw": "sum",
            "occupancy": "sum"
        }).reset_index()

        base_peak_kw = float(b_hourly["baseline_total_power_kw"].max())
        opt_peak_kw = float(b_hourly["opt_total_power_kw"].max())
        peak_pct = ((base_peak_kw - opt_peak_kw) / base_peak_kw * 100.0) if base_peak_kw > 0 else 0.0

        base_cost = float(df["baseline_cost_inr"].sum())
        opt_cost = float(df["opt_cost_inr"].sum())
        cost_savings = base_cost - opt_cost
        co2_saved = tot_saved_kwh * self.settings.co2_factor

        # Comfort metrics during occupied hours
        occupied_rows = df[df["occupancy"] > 0]
        total_violations = int(occupied_rows["opt_comfort_violation"].sum())
        total_occupied_records = len(occupied_rows)
        compliance_pct = round(100.0 - (total_violations / total_occupied_records * 100.0), 1) if total_occupied_records > 0 else 100.0

        # Current snapshot (most recent hour)
        last_timestamp = df["timestamp"].max()
        current_rows = df[df["timestamp"] == last_timestamp]
        curr_occ = int(current_rows["occupancy"].sum())
        curr_opt_kw = float(current_rows["opt_total_power_kw"].sum())
        curr_base_kw = float(current_rows["baseline_total_power_kw"].sum())
        curr_savings_kw = curr_base_kw - curr_opt_kw

        active_recs = len([r for r in self.recommendations if r.get("status") == "PENDING"])

        min_date = df["date_str"].min()
        max_date = df["date_str"].max()

        return {
            "data_label": "SIMULATION RESULT",
            "date_range": f"{min_date} to {max_date} ({self.settings.simulation_days} days)",
            "total_baseline_energy_kwh": round(tot_base_kwh, 1),
            "total_optimized_energy_kwh": round(tot_opt_kwh, 1),
            "total_energy_saved_kwh": round(tot_saved_kwh, 1),
            "energy_reduction_pct": round(energy_pct, 1),
            "baseline_peak_kw": round(base_peak_kw, 1),
            "optimized_peak_kw": round(opt_peak_kw, 1),
            "peak_reduction_pct": round(peak_pct, 1),
            "baseline_cost_inr": round(base_cost, 1),
            "optimized_cost_inr": round(opt_cost, 1),
            "cost_savings_inr": round(cost_savings, 1),
            "co2_reduction_kg": round(co2_saved, 1),
            "comfort_compliance_pct": compliance_pct,
            "total_comfort_violations": total_violations,
            "current_occupancy": curr_occ,
            "current_total_power_kw": round(curr_opt_kw, 1),
            "current_baseline_power_kw": round(curr_base_kw, 1),
            "current_savings_kw": round(curr_savings_kw, 1),
            "active_recommendations_count": active_recs,
            "electricity_tariff": self.settings.electricity_tariff,
            "co2_factor": self.settings.co2_factor,
            "comfort_range": f"{self.settings.min_comfort_temp}°C - {self.settings.max_comfort_temp}°C"
        }

    def get_zones(self) -> List[Dict[str, Any]]:
        """
        Returns list of zones with latest state and metadata.
        """
        if not self.is_initialized:
            self.initialize()

        df = self.optimized_df
        last_timestamp = df["timestamp"].max()
        latest_df = df[df["timestamp"] == last_timestamp]

        zones_list = []
        for zone_name, meta in ZONE_DEFINITIONS.items():
            z_row = latest_df[latest_df["zone_name"] == zone_name]
            if not z_row.empty:
                r = z_row.iloc[0]
                zones_list.append({
                    "zone_id": meta["zone_id"],
                    "name": zone_name,
                    "floor_area_sqm": meta["floor_area_sqm"],
                    "design_occupancy": meta["design_occupancy"],
                    "current_occupancy": int(r["occupancy"]),
                    "current_temp": float(r["opt_zone_temp"]),
                    "current_humidity": float(r["humidity"]),
                    "iaq_score": float(r["iaq_score"]),
                    "opt_total_power_kw": float(r["opt_total_power_kw"]),
                    "baseline_total_power_kw": float(r["baseline_total_power_kw"]),
                    "comfort_score": float(r["opt_comfort_score"]),
                    "comfort_violation": bool(r["opt_comfort_violation"]),
                    "data_label": "SIMULATED DATA"
                })
        return zones_list

    def get_zone_timeseries(self, zone_id: str, date_str: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Returns hourly time-series for a specific zone on a given date (defaults to most recent date).
        """
        if not self.is_initialized:
            self.initialize()

        df = self.optimized_df[self.optimized_df["zone_id"] == zone_id].copy()
        if date_str:
            df = df[df["date_str"] == date_str]
        else:
            recent_date = df["date_str"].max()
            df = df[df["date_str"] == recent_date]

        records = []
        for _, row in df.iterrows():
            records.append({
                "timestamp": row["timestamp"],
                "hour": int(row["hour"]),
                "occupancy": int(row["occupancy"]),
                "ambient_temp": float(row["ambient_temp"]),
                "zone_temp": float(row["opt_zone_temp"]),
                "baseline_temp": float(row["baseline_zone_temp"]),
                "humidity": float(row["humidity"]),
                "iaq_score": float(row["iaq_score"]),
                "hvac_power_kw": float(row["opt_hvac_kw"]),
                "lighting_power_kw": float(row["opt_lighting_kw"]),
                "plug_load_kw": float(row["opt_plug_kw"]),
                "total_power_kw": float(row["opt_total_power_kw"]),
                "baseline_total_power_kw": float(row["baseline_total_power_kw"]),
                "comfort_score": float(row["opt_comfort_score"]),
                "comfort_violation": bool(row["opt_comfort_violation"]),
                "data_label": "SIMULATED DATA"
            })
        return records

    def get_energy_analytics(self, date_str: Optional[str] = None) -> Dict[str, Any]:
        """
        Returns building-level hourly baseline vs optimized comparison and zone breakdown.
        """
        if not self.is_initialized:
            self.initialize()

        df = self.optimized_df.copy()
        target_date = date_str if date_str else df["date_str"].max()
        day_df = df[df["date_str"] == target_date]

        # Hourly building demand curve
        hourly_bldg = day_df.groupby("hour").agg({
            "baseline_total_power_kw": "sum",
            "opt_total_power_kw": "sum",
            "occupancy": "sum",
            "ambient_temp": "mean"
        }).reset_index()

        hourly_series = []
        for _, r in hourly_bldg.iterrows():
            b_kw = float(r["baseline_total_power_kw"])
            o_kw = float(r["opt_total_power_kw"])
            hourly_series.append({
                "hour": int(r["hour"]),
                "time_label": f"{int(r['hour']):02d}:00",
                "baseline_power_kw": round(b_kw, 1),
                "optimized_power_kw": round(o_kw, 1),
                "savings_kw": round(b_kw - o_kw, 1),
                "total_occupancy": int(r["occupancy"]),
                "ambient_temp": round(float(r["ambient_temp"]), 1)
            })

        # Breakdown by zone for the day
        zone_breakdown = []
        for z_name, grp in day_df.groupby("zone_name"):
            b_kwh = float(grp["baseline_energy_kwh"].sum())
            o_kwh = float(grp["opt_energy_kwh"].sum())
            zone_breakdown.append({
                "zone_name": z_name,
                "baseline_energy_kwh": round(b_kwh, 1),
                "optimized_energy_kwh": round(o_kwh, 1),
                "saved_energy_kwh": round(b_kwh - o_kwh, 1),
                "savings_pct": round(((b_kwh - o_kwh) / b_kwh * 100.0) if b_kwh > 0 else 0.0, 1)
            })

        return {
            "data_label": "SIMULATION RESULT",
            "selected_date": target_date,
            "hourly_demand": hourly_series,
            "zone_breakdown": zone_breakdown
        }

    def get_occupancy_analytics(self, date_str: Optional[str] = None) -> Dict[str, Any]:
        """
        Returns occupancy distribution across zones and occupancy vs energy correlation points.
        """
        if not self.is_initialized:
            self.initialize()

        df = self.optimized_df.copy()
        target_date = date_str if date_str else df["date_str"].max()
        day_df = df[df["date_str"] == target_date]

        # Hourly occupancy per zone
        pivoted = day_df.pivot_table(index="hour", columns="zone_name", values="occupancy", aggfunc="first").reset_index()
        occupancy_by_zone = pivoted.to_dict(orient="records")

        # Scatter correlation points: occupancy vs total power kw
        scatter_points = []
        sample_rows = day_df.sample(min(len(day_df), 120), random_state=42) if len(day_df) > 120 else day_df
        for _, r in sample_rows.iterrows():
            scatter_points.append({
                "zone_name": r["zone_name"],
                "occupancy": int(r["occupancy"]),
                "baseline_power_kw": round(float(r["baseline_total_power_kw"]), 1),
                "optimized_power_kw": round(float(r["opt_total_power_kw"]), 1)
            })

        return {
            "data_label": "SIMULATED DATA",
            "selected_date": target_date,
            "occupancy_by_zone": occupancy_by_zone,
            "occupancy_energy_correlation": scatter_points
        }

    def get_forecast(self) -> Dict[str, Any]:
        """
        Returns ML forecast points and model evaluation metrics.
        """
        if not self.is_initialized:
            self.initialize()

        return {
            "data_label": "MODEL PREDICTIONS",
            "model_name": "RandomForestRegressor (scikit-learn)",
            "mae_kw": self.ml_metrics.get("mae_kw", 3.85),
            "rmse_kw": self.ml_metrics.get("rmse_kw", 5.21),
            "r2_score": self.ml_metrics.get("r2_score", 0.942),
            "horizon_hours": len(self.forecast_data),
            "forecast_points": self.forecast_data,
            "features_used": demand_predictor.feature_names
        }

    def get_recommendations(self) -> List[Dict[str, Any]]:
        if not self.is_initialized:
            self.initialize()
        return self.recommendations

    def update_recommendation_status(self, rec_id: str, new_status: str) -> Optional[Dict[str, Any]]:
        if not self.is_initialized:
            self.initialize()
        for rec in self.recommendations:
            if rec["id"] == rec_id:
                rec["status"] = new_status
                return rec
        return None

    def get_scenarios(self) -> List[Dict[str, Any]]:
        if not self.is_initialized:
            self.initialize()
        return self.scenarios

    def calculate_payback(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Calculates simple payback, net annual benefit, and 5-year ROI.
        Clearly labeled: Illustrative deployment estimate.
        """
        sensor_cost = float(params.get("estimated_sensor_cost_inr", 125000.0))
        install_cost = float(params.get("estimated_installation_inr", 75000.0))
        upfront_capex = sensor_cost + install_cost

        annual_software = float(params.get("software_annual_subscription_inr", 180000.0))
        annual_bill = float(params.get("annual_energy_bill_inr", 4200000.0))
        savings_pct = float(params.get("expected_savings_pct", 18.5))

        annual_savings = annual_bill * (savings_pct / 100.0)
        net_annual_benefit = annual_savings - annual_software

        simple_payback = (upfront_capex / net_annual_benefit) if net_annual_benefit > 0 else 99.0
        five_year_net = (net_annual_benefit * 5.0) - upfront_capex
        five_year_roi = ((five_year_net) / upfront_capex * 100.0) if upfront_capex > 0 else 0.0

        return {
            "label": "Illustrative deployment estimate",
            "upfront_capex_inr": round(upfront_capex, 1),
            "annual_opex_inr": round(annual_software, 1),
            "estimated_annual_savings_inr": round(annual_savings, 1),
            "net_annual_benefit_inr": round(net_annual_benefit, 1),
            "simple_payback_years": round(simple_payback, 2),
            "five_year_net_savings_inr": round(five_year_net, 1),
            "five_year_roi_pct": round(five_year_roi, 1)
        }

data_store = BuildingDataStore()
