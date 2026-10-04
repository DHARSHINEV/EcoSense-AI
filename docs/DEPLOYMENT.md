# EcoSense AI – Phased Deployment & Economic Viability

## 1. Phased Deployment Roadmap

Deploying AI optimization into commercial buildings should minimize operational disruption and mitigate hardware capital risk. EcoSense AI proposes a structured 4-stage engineering rollout:

### Phase 1: Software Analytics & Virtual Auditing (Months 1–2)
- **Objective**: Ingest existing smart meter interval data and available BMS logs without installing physical hardware.
- **Activities**:
  - Establish API connection with utility smart meters or building main incomer energy meters.
  - Train baseline regression model and identify nighttime scheduling drifts, base load anomalies, and tariff mismatch penalties.
  - Zero disruption to building operations.

### Phase 2: Low-Cost IoT Sensing Overlay (Months 3–4)
- **Objective**: Introduce high-granularity zone observability.
- **Activities**:
  - Deploy non-intrusive wireless multi-sensor pods (battery-operated LoRaWAN / Zigbee 3.0 sensors measuring PIR occupancy, temperature, humidity, and $\text{CO}_2$).
  - Map spatial occupancy profiles and identify over-cooled vacant zones (meeting rooms, unoccupied conference suites).

### Phase 3: Automated BMS & Smart Thermostat Integration (Months 5–6)
- **Objective**: Establish closed-loop supervisory control.
- **Activities**:
  - Deploy BACnet IP / Modbus RTU IoT gateway interfacing with Chiller Plant Managers and VAV/VRF controllers.
  - Implement occupancy-aware automated setbacks and perimeter daylight harvesting dimming.
  - Human-in-the-loop validation: Facility managers retain full manual override capability.

### Phase 4: Grid-Interactive Efficient Building (GEB) & Demand Response (Months 7+)
- **Objective**: Dynamic peak shaving and grid revenue.
- **Activities**:
  - Integrate OpenADR 2.0b / utility Time-of-Day (ToD) tariff signaling.
  - Implement automated pre-cooling of building thermal mass before peak tariff periods.
  - Monetize automated load flexibility in utility demand-response programs.

---

## 2. Target Building Archetypes

| Building Type | Structural Characteristics | Primary Energy Waste Driver | EcoSense Value Proposition |
| :--- | :--- | :--- | :--- |
| **IT & Tech Parks** | Multi-tenant, large floorplates, 24/7 partial usage | Overcooling during hybrid-work off-days; rigid chiller schedules | Dynamic occupancy setback & VAV airflow optimization |
| **Educational Campuses** | Variable class schedules, lecture halls, auditoriums | Cooling empty classrooms between lectures | Schedule & sensor-linked fast thermal setback |
| **Retail & Shopping Malls** | High customer footfall swings, high ceilings | Overcooling during low-footfall mornings | Pre-cooling and ambient-responsive chiller modulation |
| **Commercial Coworking** | Unpredictable meeting room usage, high turnover | Vacant meeting rooms cooled continuously | Instantaneous PIR/BLE occupancy setback & lighting shutoff |

---

## 3. Financial & Payback Model

*Note: All economic figures are illustrative deployment estimates based on simulated facility parameters.*

### Illustrative Baseline Facility:
- **Conditioned Area**: 5,000 sq.m (approx. 54,000 sq.ft)
- **Annual Electricity Bill**: ₹4,200,000 (~₹3.5 lakh/month)
- **Target Simulated Savings**: 18.5%
- **Estimated Annual Energy Savings**: **₹777,000 / year**

### Capital & Operational Expenditure:
- **IoT Sensors (25 wireless pods @ ₹5,000)**: ₹125,000
- **Gateway & Physical Commissioning**: ₹75,000
- **Total Initial CapEx**: **₹200,000**
- **SaaS Software Subscription**: ₹180,000 / year (₹15,000/month)
- **Net Annual Benefit (Savings - SaaS)**: **₹597,000 / year**

### Investment Returns:
- **Simple Payback Period**: **4.0 months** ($\approx 0.33$ years)
- **5-Year Net Cash Savings**: **₹2,785,000**
- **5-Year Return on Investment (ROI)**: **> 1,300%**
