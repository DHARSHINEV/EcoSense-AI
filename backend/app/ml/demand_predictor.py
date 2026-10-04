"""
EcoSense AI - Near-Term Energy Demand Prediction Engine.
Uses Scikit-Learn RandomForestRegressor trained on simulated time-series data.
Explicitly avoids data leakage through chronological train/test split.
Results explicitly labeled as MODEL PREDICTIONS.
"""
import os
import joblib
import numpy as np
import pandas as pd
from typing import Dict, Any, Tuple, List
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from app.config import settings

MODEL_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../models"))
MODEL_PATH = os.path.join(MODEL_DIR, "demand_forecast_model.joblib")

FEATURES = [
    "hour",
    "day_of_week",
    "is_weekend_int",
    "total_occupancy",
    "ambient_temp",
    "humidity",
    "lag_1h_power",
    "lag_24h_power",
    "is_operating_hours"
]

class DemandPredictor:
    def __init__(self):
        self.model: RandomForestRegressor = None
        self.metrics: Dict[str, float] = {}
        self.feature_names: List[str] = FEATURES

    def prepare_building_timeseries(self, df_with_baseline: pd.DataFrame) -> pd.DataFrame:
        """
        Aggregates multi-zone records into hourly building-level time-series and constructs lag features.
        """
        # Aggregate zones by timestamp
        building_df = df_with_baseline.groupby(["timestamp", "date_str", "hour", "day_of_week", "is_weekend"]).agg({
            "occupancy": "sum",
            "ambient_temp": "mean",
            "humidity": "mean",
            "baseline_total_power_kw": "sum"
        }).reset_index()

        building_df.rename(columns={
            "occupancy": "total_occupancy",
            "baseline_total_power_kw": "total_power_kw"
        }, inplace=True)

        # Sort chronologically
        building_df["timestamp_dt"] = pd.to_datetime(building_df["timestamp"])
        building_df.sort_values("timestamp_dt", inplace=True)
        building_df.reset_index(drop=True, inplace=True)

        # Create time-series lag features
        building_df["is_weekend_int"] = building_df["is_weekend"].astype(int)
        building_df["is_operating_hours"] = ((~building_df["is_weekend"]) & 
                                            (building_df["hour"] >= settings.operating_start_hour) & 
                                            (building_df["hour"] < settings.operating_end_hour)).astype(int)

        # Lag features (1-hour lag, 24-hour lag)
        building_df["lag_1h_power"] = building_df["total_power_kw"].shift(1)
        building_df["lag_24h_power"] = building_df["total_power_kw"].shift(24)

        # Backfill initial lag rows with reasonable hour averages
        building_df["lag_1h_power"] = building_df["lag_1h_power"].bfill()
        building_df["lag_24h_power"] = building_df["lag_24h_power"].bfill()

        return building_df

    def train(self, building_df: pd.DataFrame, test_ratio: float = 0.20) -> Dict[str, Any]:
        """
        Trains RandomForestRegressor with strict chronological split (no shuffle) to avoid leakage.
        """
        df = building_df.dropna(subset=self.feature_names + ["total_power_kw"]).copy()
        
        split_idx = int(len(df) * (1.0 - test_ratio))
        train_df = df.iloc[:split_idx]
        test_df = df.iloc[split_idx:]

        X_train = train_df[self.feature_names]
        y_train = train_df["total_power_kw"]

        X_test = test_df[self.feature_names]
        y_test = test_df["total_power_kw"]

        # Train practical Random Forest model
        self.model = RandomForestRegressor(
            n_estimators=100,
            max_depth=12,
            min_samples_split=4,
            random_state=settings.random_seed,
            n_jobs=-1
        )
        self.model.fit(X_train, y_train)

        # Evaluate on out-of-sample test set
        y_pred = self.model.predict(X_test)
        mae = float(mean_absolute_error(y_test, y_pred))
        rmse = float(np.sqrt(mean_squared_error(y_test, y_pred)))
        r2 = float(r2_score(y_test, y_pred))

        self.metrics = {
            "mae_kw": round(mae, 2),
            "rmse_kw": round(rmse, 2),
            "r2_score": round(r2, 4),
            "train_samples": len(train_df),
            "test_samples": len(test_df)
        }

        # Persist model
        os.makedirs(MODEL_DIR, exist_ok=True)
        joblib.dump({
            "model": self.model,
            "metrics": self.metrics,
            "features": self.feature_names
        }, MODEL_PATH)

        return self.metrics

    def predict_forecast(self, building_df: pd.DataFrame, horizon_hours: int = 12) -> List[Dict[str, Any]]:
        """
        Generates near-term energy demand forecast for the most recent or upcoming window.
        Returns predicted demand, actual simulated demand, and error bands.
        """
        if self.model is None:
            if os.path.exists(MODEL_PATH):
                saved = joblib.load(MODEL_PATH)
                self.model = saved["model"]
                self.metrics = saved["metrics"]
            else:
                self.train(building_df)

        df = building_df.copy()
        # Take the last `horizon_hours` of data for the demo forecast
        eval_window = df.tail(horizon_hours).copy()
        X_eval = eval_window[self.feature_names]
        preds = self.model.predict(X_eval)

        # Approximate empirical prediction band based on training MAE
        margin = self.metrics.get("mae_kw", 4.5) * 1.645  # Approximate empirical prediction band

        results = []
        for i, (_, row) in enumerate(eval_window.iterrows()):
            pred_val = round(float(preds[i]), 1)
            actual_val = round(float(row["total_power_kw"]), 1)
            err = round(abs(pred_val - actual_val), 1)
            results.append({
                "timestamp": row["timestamp"],
                "hour": int(row["hour"]),
                "predicted_demand_kw": pred_val,
                "actual_simulated_demand_kw": actual_val,
                "error_kw": err,
                "lower_bound_kw": round(max(0.0, pred_val - margin), 1),
                "upper_bound_kw": round(pred_val + margin, 1),
                "data_label": "MODEL PREDICTION"
            })

        return results

demand_predictor = DemandPredictor()
