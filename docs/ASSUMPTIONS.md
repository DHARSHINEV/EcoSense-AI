# EcoSense AI – Simulation Assumptions & Engineering Specifications

This document outlines the numerical, thermodynamic, and operational assumptions embedded within the EcoSense AI prototype simulation engine.

---

## 1. Facility & Zone Archetypes

The simulated commercial facility represents a standard **Grade-A Commercial Office Facility** located in a tropical/sub-tropical climate (e.g., Bengaluru / Hyderabad / Mumbai):

| Zone Name | Floor Area (sq.m) | Design Occupancy | Base Lighting (kW) | Base HVAC (kW) | Base Plug Load (kW) | Typical Occupancy Dynamics |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Lobby** | 400 | 30 | 3.2 | 18.0 | 2.0 | Transient throughput peak during morning/evening commute and lunch. |
| **Office Floor** | 1,800 | 150 | 14.5 | 68.0 | 18.0 | Core working hours (09:00–18:00) with typical lunch dip at 13:00. |
| **Meeting Room** | 120 | 16 | 1.8 | 8.5 | 1.5 | Episodic calendar-driven bursts (60% work-hour probability). |
| **Conference Room** | 320 | 45 | 4.0 | 18.5 | 3.5 | Sporadic events (2–3 large team meetings per week; vacant 65% of work hours). |
| **Cafeteria** | 600 | 85 | 5.0 | 26.0 | 9.0 | Concentrated demand during meal windows (12:00–14:30) and tea breaks. |
| **Total Facility** | **3,240** | **326** | **28.5** | **139.0** | **34.0** | **Total Connected Electrical Capacity: ~201.5 kW** |

---

## 2. Weather & Diurnal Thermodynamics

1. **Ambient Temperature**:
   - Diurnal sinusoidal oscillation: Daily minimum at 05:00 (~24.0°C), daily maximum at 14:00 (~35.0°C).
   - Weekly synoptic weather fluctuations: Sinusoidal drift of $\pm 2.5^\circ\text{C}$ to simulate heatwaves and overcast frontal passages.
   - Stochastic noise: Gaussian $\mathcal{N}(0, 0.6^\circ\text{C})$.
2. **Relative Humidity (RH)**:
   - Inversely correlated with ambient temperature: Peaks around 65–75% RH at dawn, drops to 35–45% RH in peak afternoon.
3. **Internal Heat Gains**:
   - Metabolic heat output: Simulated as 100 W sensible + latent heat per active occupant.
   - Equipment and lighting thermal dissipation: 80% of active lighting and 60% of plug loads dissipate as convective/radiative room heat.

---

## 3. Baseline Building Assumptions (Scenario A)

The baseline model reflects standard fixed-schedule non-automated operation:
- **Operating Schedule**: Rigidly active between **07:00 and 20:00 (Monday–Friday)** regardless of presence.
- **Cooling Setpoint**: Static **22.0°C** maintained constantly across all zones during operating hours.
- **Lighting Operation**: **100% full capacity** across all fixtures during operating hours; 10% security lighting overnight.
- **Plug Loads**: Constant 85% daytime active load; 20% overnight standby.
- **Peak Demand Management**: None. Peak tariff penalties are incurred whenever cooling coincidently spikes with daytime ambient temperature.
- **Weekends**: Reduced to 5% standby HVAC and 10% emergency lighting.

---

## 4. EcoSense Optimized Control Assumptions (Scenario D)

- **Occupancy-Aware HVAC Setback**:
  - Unoccupied zones during work hours: Cooling setpoint relaxed to **25.5°C** (saving 25–35% compressor power while remaining inside maximum comfort boundaries).
  - Occupied zones: Optimal setpoint centered at **24.0°C** (reducing unnecessary overcooling compared to the rigid 22.0°C baseline).
- **Daylight Harvesting & Lighting Dimming**:
  - Empty rooms dimmed to 5% security level or turned off completely.
  - Active zones with perimeter solar exposure dimmed by 25–30% during midday (10:00–16:00).
- **Predictive Pre-Cooling & Peak Shaving**:
  - When forecasted aggregate building demand exceeds the **175 kW threshold**, the facility pre-cools building thermal mass by 0.5°C between 07:00–09:00 and relaxes setpoints to 24.8°C during peak hours (13:00–16:00), clipping peak demand spikes.
- **Occupant Comfort Envelope (Simplified Temperature Proxy)**:
  - **Configured Comfort Range**: 22.0°C to 26.0°C (temperature-based comfort proxy inspired by adaptive thermal standards).
  - **Compliance Formula**: Evaluated strictly during occupied hours ($\text{Occupancy} > 0$):
    $$\text{Compliance Rate} = \left( 1 - \frac{\text{Hours with } (T < 22^\circ\text{C} \text{ or } T > 26^\circ\text{C})}{\text{Total Occupied Hours}} \right) \times 100\%$$
  - The optimization engine rejects any setbacks that would push an occupied zone outside this band.

---

## 5. Economic & Environmental Parameters

- **Electricity Commercial Tariff**: **₹8.50 per kWh** (default blended commercial energy tariff for urban Indian utilities; user-configurable in the control panel).
- **Peak Demand Penalty**: Assumed 1.5× multiplier during critical grid peak hours.
- **Grid Carbon Emission Factor**: **0.82 kg $\text{CO}_2$ per kWh** (Central Electricity Authority – CEA Baseline Carbon Database for the Indian National Grid Version 19).
- **Payback & Installation Assumptions**:
  - Wireless IoT multisensors (PIR + Temp + RH + $\text{CO}_2$): ₹5,000 per unit.
  - BACnet/Modbus Gateway Installation & Commissioning: ₹75,000 lump sum.
  - Software SaaS Platform Subscription: ₹15,000 per month (₹180,000/year).
