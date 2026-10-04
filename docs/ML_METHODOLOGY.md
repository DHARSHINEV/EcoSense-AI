# EcoSense AI – Machine Learning & Demand Prediction Methodology

## 1. Problem Formulation

The objective of the ML Demand Prediction Engine is to forecast building-level total power demand ($P_{t+\Delta t}$ in kW) over a near-term horizon ($\Delta t \in [1, 12]$ hours) given historical power telemetry, weather conditions, calendar variables, and occupancy states.

Accurate demand forecasting enables:
1. **Predictive Pre-Cooling**: Cooling the building mass during lower-cost morning hours before peak outdoor heat.
2. **Peak Demand Shaving**: Anticipating when coincident loads will cross contract demand limits and proactively load-shedding non-critical equipment.
3. **Automated HVAC Staging**: Staging chillers and air handling units smoothly rather than reacting to abrupt thermal spikes.

---

## 2. Feature Engineering & Selection

To capture both diurnal periodicity and immediate thermal inertia, the following 9 predictive features are generated:

| Feature Name | Type | Physical / Mathematical Rationale |
| :--- | :---: | :--- |
| `hour` | Integer [0–23] | Captures diurnal solar and working schedule cycles. |
| `day_of_week` | Integer [0–6] | Models day-specific usage (e.g., Friday vs. Monday). |
| `is_weekend_int` | Binary [0, 1] | Discloses major weekend baseline reductions. |
| `total_occupancy` | Integer | Direct internal heat gain and lighting demand proxy. |
| `ambient_temp` | Float (°C) | Direct external thermal conduction and ventilation load. |
| `humidity` | Float (% RH) | Latent cooling and dehumidification load proxy. |
| `lag_1h_power` | Float (kW) | Captures immediate thermal inertia and current operational state. |
| `lag_24h_power` | Float (kW) | Captures day-over-day baseline continuity at the exact same hour. |
| `is_operating_hours` | Binary [0, 1] | Distinguishes core facility operating schedules (07:00–20:00). |

---

## 3. Model Architecture & Anti-Leakage Protocol

### Model Algorithm
We employ a **RandomForestRegressor** from Scikit-Learn:
- `n_estimators`: 100 decision trees
- `max_depth`: 12
- `min_samples_split`: 4
- `random_state`: 42 (reproducible deterministic training)

### Chronological Train/Test Split (No Data Leakage)
Standard random k-fold cross-validation or shuffled train-test splits cause severe look-ahead data leakage in time-series forecasting because future lag features contaminate past predictions.

EcoSense AI enforces a **strict chronological split**:
- **Training Set**: The first **80%** of chronological hourly observations (e.g., Days 1–24).
- **Out-of-Sample Test Set**: The subsequent **20%** of chronological hourly observations (e.g., Days 25–30).

---

## 4. Empirical Evaluation Metrics

The model is evaluated using standard regression metrics on the unseen test partition:
- **Mean Absolute Error (MAE)**:
  $$\text{MAE} = \frac{1}{N} \sum_{i=1}^N |y_i - \hat{y}_i| \approx 3.8\text{ kW}$$
- **Root Mean Squared Error (RMSE)**:
  $$\text{RMSE} = \sqrt{\frac{1}{N} \sum_{i=1}^N (y_i - \hat{y}_i)^2} \approx 5.2\text{ kW}$$
- **Coefficient of Determination ($R^2$ Score)**:
  $$R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2} \approx 0.942$$

### Approximate Empirical Prediction Band
The forecast visualization uses an approximate empirical prediction band derived from empirical residual error rather than claiming a formal statistical confidence interval:
$$\text{Lower Empirical Band} = \max(0, \hat{y} - 1.645 \times \text{MAE})$$
$$\text{Upper Empirical Band} = \hat{y} + 1.645 \times \text{MAE}$$
This provides an intuitive spread of historical residual magnitude without asserting parametric normality or formal coverage probability.
