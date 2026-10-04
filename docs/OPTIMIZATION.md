# EcoSense AI – Multi-Objective Optimization & Control Logic

## 1. Problem Formulation

The EcoSense AI Optimization Engine solves a constrained multi-objective problem across three conflicting operational goals:

1. **Objective 1 (Energy Reduction)**: Minimize total building electrical consumption:
   $$\min \sum_{z \in \text{Zones}} \left( P_{\text{HVAC}, z}(t) + P_{\text{Lighting}, z}(t) + P_{\text{Plug}, z}(t) \right) \cdot \Delta t$$
2. **Objective 2 (Occupant Comfort Preservation)**: Maintain zone temperatures within strict comfort boundaries during occupied hours using a simplified temperature-based comfort compliance proxy:
   $$T_{\min} \le T_z(t) \le T_{\max}, \quad \forall t \text{ where } \text{Occupancy}_z(t) > 0$$
   $$\text{Default Comfort Range: } [22.0^\circ\text{C}, 26.0^\circ\text{C}]$$
   $$\text{Violation Indicator: } V_z(t) = \begin{cases} 1 & \text{if } \text{Occupancy}_z(t) > 0 \text{ and } (T_z(t) < T_{\min} \text{ or } T_z(t) > T_{\max}) \\ 0 & \text{otherwise} \end{cases}$$
   $$\text{Temperature Comfort Compliance (\%)} = \left( 1 - \frac{\sum_{t \in \text{Occupied}} V_z(t)}{N_{\text{Occupied}}} \right) \times 100\%$$
   $$\text{Comfort Score (0–100)} = \text{clip}\left(100 - |T_z(t) - 24.0|^{1.8} \times 10.0 - \text{RH Penalty}, 20, 100\right)$$
3. **Objective 3 (Peak Demand Clipping)**: Restrict coincident building-level power to prevent utility maximum demand penalty thresholds:
   $$P_{\text{Total}}(t) \le P_{\text{Peak Threshold}} \quad (175\text{ kW default})$$

---

## 2. Optimization Rules & Safety Guardrails

### Rule 1: Occupancy-Aware HVAC Setback
- **Trigger**: Zone occupancy is zero ($\text{Occupancy}_z = 0$) during scheduled operating hours (07:00–20:00).
- **Control Action**: Shift cooling setpoint from nominal comfort center ($24.0^\circ\text{C}$) to eco-standby ($25.5^\circ\text{C}$).
- **Thermodynamic Impact**: Compresses chiller temperature lift, reducing compressor lift work and cutting zone cooling load by 25–35%.
- **Safety Check**: Temperature never exceeds $26.0^\circ\text{C}$, ensuring rapid pulldown (within 8–10 minutes) when occupants re-enter.

### Rule 2: Occupancy-Driven Lighting Modulation & Daylight Harvesting
- **Trigger A (Vacant)**: When $\text{Occupancy}_z = 0$, lighting is dimmed to 5% emergency level or turned off entirely.
- **Trigger B (Occupied Midday)**: When $10 \le \text{hour} \le 16$, perimeter fixtures with exterior window exposure are dimmed by 25–30% to harvest ambient lux.
- **Safety Check**: Emergency stairwells and essential egress fixtures are never switched off.

### Rule 3: Predictive Pre-Cooling & Peak Demand Shaving
- **Trigger**: Near-term ML forecast predicts total facility power demand will approach or cross 90% of the peak threshold ($175\text{ kW}$).
- **Control Action**:
  1. *Pre-Cooling*: Sub-cool building thermal mass to $23.0^\circ\text{C}$ during off-peak morning hours (07:00–09:00).
  2. *Floating Setback*: Float active setpoint to $24.8^\circ\text{C}$ during peak tariff hours (13:00–16:00).
- **Grid Impact**: Clips coincident peak spike by 15–20 kW, avoiding steep utility contract demand penalties.

---

## 3. Human-in-the-Loop Recommendation Engine

Rather than an opaque "black-box" override, EcoSense AI surfaces transparent, prioritized recommendations to the facility manager:
- **Unique Recommendation ID** (e.g., `REC-2026-001`)
- **Affected Zone**: Clearly specifies the targeted physical area.
- **Action Type**: `HVAC_SETBACK`, `LIGHTING_DIM`, `PEAK_LOAD_SHED`, or `PRE_COOLING`.
- **Expected Energy & Cost Savings**: Quantified in instantaneous kW and ₹/hour.
- **Comfort Impact Assessment**: Explicit assurance that temperature remains inside the 22–26°C band.
- **Interactive Manager Journey**: Facility managers can **Accept**, **Dismiss**, or mark as **Reviewed**.
