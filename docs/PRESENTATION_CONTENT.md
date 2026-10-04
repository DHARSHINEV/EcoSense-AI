# EcoSense AI – Hackathon Slide Deck (10 Slides)
### Yuva Yodha Energy Tech Hackathon 2026 • Track: Smart Buildings

> **Project:** EcoSense AI – Intelligent Building Energy Optimizer  
> **Challenge:** Smart Buildings  
> **Hackathon:** Yuva Yodha Energy Tech Hackathon 2026  
> **Team:** TEAM NOVA  
> **Team Lead:** Dharshine V (`vdharshine19@gmail.com`)  
> **Final PowerPoint File:** `EcoSense_AI_Yuva_Yodha_Hackathon_2026_FINAL.pptx`  
> **Format:** 16:9 Widescreen (13.333" × 7.5")  
> **Design Philosophy:** Clarity First • High Contrast • Large Typography • Scannable in 5 Seconds  
> **Color Palette:** Deep Navy Slate (`#0A0F1D`), Dark Slate Card (`#111827`), Emerald Green (`#10B981`), Tech Cyan (`#06B6D4`), Cost Amber (`#F59E0B`), Pure White (`#F8FAFC`).

---

## The Core 6-Step Storyline

```
BUILDINGS WASTE ENERGY
        ↓
ECOSENSE AI UNDERSTANDS BUILDING CONDITIONS
        ↓
AI PREDICTS ENERGY DEMAND
        ↓
OPTIMIZATION BALANCES ENERGY + COMFORT + PEAK
        ↓
SYSTEM RECOMMENDS ACTIONS
        ↓
OUR PROTOTYPE SIMULATION SHOWS THE POTENTIAL
```

---

## Slide-by-Slide Detailed Specification

### SLIDE 1: COVER SLIDE
- **Top Tracker:** `YUVA YODHA ENERGY TECH HACKATHON 2026 • CHALLENGE: SMART BUILDINGS`
- **Right Header Badge:** `PROTOTYPE PITCH DECK` (Emerald Green `#10B981`)
- **Title (Largest Text):** **ECOSENSE AI** (46pt Bold, Pure White)
- **Subtitle:** **Intelligent Building Energy Optimizer** (22pt Bold, Emerald Green)
- **3 Value Pills (Horizontal):**
  - `[ AI-Powered Energy Efficiency ]`
  - `[ Comfort-Aware Optimization ]`
  - `[ Peak-Demand Management ]`
- **Center Visual Flow (4-Node Connected Process):**
  `[ 🏢 BUILDING ]  ──▶  [ 📡 SENSORS / DATA ]  ──▶  [ 🧠 AI ENGINE ]  ──▶  [ ⚡ OPTIMIZED CONTROL ]`
  - *Building:* Commercial Spaces & Active Thermal Zones
  - *Sensors/Data:* Occupancy, Temperature, IAQ & Power Telemetry
  - *AI Engine:* Random Forest 24h Ahead Demand Forecasting
  - *Optimized Control:* Peak Shaving, Comfort Guard & Dynamic Setbacks
- **Bottom Left Card (Team NOVA):**
  - Team: **TEAM NOVA** • Yuva Yodha Energy Tech Hackathon 2026
  - Team Lead: **Dharshine V** | `vdharshine19@gmail.com`
- **Bottom Right Card (Current Status):**
  - Status: **CURRENT STATUS**
  - Description: Functional software simulation and energy decision-support prototype.
- **Footer:** Slide 1 of 10

---

### SLIDE 2: THE PROBLEM
- **Top Tracker:** `THE COMMERCIAL BUILDING CHALLENGE`
- **Main Title:** **THE PROBLEM**
- **Right Header Badge:** `PROBLEM STATEMENT` (Red `#EF4444`)
- **Large Bold Headline:**
  > **BUILDINGS OFTEN RUN ON FIXED SCHEDULES — BUT BUILDING CONDITIONS KEEP CHANGING.**
- **Visual Causality Flow:**
  `[ FIXED SCHEDULE ] ──▶ [ VACANT / PARTIAL SPACES ] ──▶ [ UNNECESSARY HVAC + LIGHTING ] ──▶ [ ENERGY WASTE + PEAK SPIKES ]`
- **3 Problem Dimension Cards:**
  1. **01 | ENERGY WASTE (Unnecessary HVAC & lighting operation)**
     - HVAC and lighting run full blast regardless of real headcount.
     - Meeting rooms and empty zones conditioned on rigid timers.
     - Avoidable baseload drives significant continuous energy loss.
  2. **02 | PEAK DEMAND (Simultaneous loads create demand spikes)**
     - Midday outdoor heat combined with occupancy spikes grid draw.
     - Commercial utilities levy steep Maximum Demand charges.
     - Unmanaged coincidence creates expensive electrical spikes.
  3. **03 | COMFORT MISMATCH (Static settings fail to adapt to occupancy)**
     - Thermostats hold a flat setpoint regardless of zone density.
     - Leads to simultaneous overcooling in empty rooms & stuffiness.
     - Occupant dissatisfaction leads to manual setpoint tampering.
- **Bottom Takeaway Callout:**
  > *"Building managers need smarter, data-driven operating decisions."*
- **Footer:** Slide 2 of 10

---

### SLIDE 3: OUR SOLUTION
- **Top Tracker:** `INTELLIGENT ENERGY PLATFORM`
- **Main Title:** **OUR SOLUTION**
- **Right Header Badge:** `SOLUTION OVERVIEW` (Emerald Green `#10B981`)
- **Large Center Statement Card:**
  > **ECOSENSE AI TURNS BUILDING DATA INTO ACTIONABLE ENERGY DECISIONS.**
- **5-Step Horizontal Closed-Loop Flow:**
  1. **STEP 1: SENSE**
     - *Summary:* Occupancy + environmental + energy data
     - Zone occupancy (headcount)
     - Indoor temp (°C) & humidity
     - HVAC, lighting, & plug power
  2. **STEP 2: PREDICT**
     - *Summary:* 24-hour demand forecast
     - Random Forest regression
     - Diurnal pattern modeling
     - Empirical prediction bands
  3. **STEP 3: OPTIMIZE**
     - *Summary:* Energy + comfort + peak demand
     - Simultaneous 3-way balance
     - Strict 22°C–26°C comfort target
     - Peak limit clipping (≤175 kW)
  4. **STEP 4: RECOMMEND**
     - *Summary:* Actionable operating suggestions
     - Dynamic occupancy setbacks
     - Daylight harvesting dimming
     - Thermal pre-cooling triggers
  5. **STEP 5: MEASURE**
     - *Summary:* Baseline vs optimized performance
     - Transparent savings analytics
     - Real-time kWh & ₹ tracking
     - Continuous comfort logging
- **Bottom Status Callout:**
  - `CURRENT PROTOTYPE: Software simulation + decision support`
- **Footer:** Slide 3 of 10

---

### SLIDE 4: HOW ECOSENSE AI WORKS
- **Top Tracker:** `SYSTEM ARCHITECTURE & PIPELINE`
- **Main Title:** **HOW ECOSENSE AI WORKS**
- **Right Header Badge:** `4-LAYER STACK` (Tech Cyan `#06B6D4`)
- **Headline Statement:**
  > **"From raw telemetry → prediction → optimized decision"**
- **4 Progressive Horizontal Layers (Clean Left-Aligned Stack):**
  - **LAYER 1: BUILDING DATA**
    - *Telemetry:* Occupancy • Temperature • Humidity • IAQ • HVAC • Lighting • Plug Loads
    - *Detail:* Collects multi-zone telemetry across 5 building zones (~2,300 m²) with real-time signal validation.
  - **LAYER 2: AI FORECAST**
    - *ML Model:* Random Forest Regressor • 24-Hour Energy Demand Prediction
    - *Detail:* Predicts whole-building power draw (kW) with $R^2 \approx 0.942$ and empirical prediction bands ($\pm 1.645 \times \text{MAE}$).
  - **LAYER 3: OPTIMIZATION ENGINE**
    - *Objective:* Energy + Comfort + Peak Demand Multi-Objective Balance
    - *Detail:* Calculates setpoint offsets, shifts loads before peak hours, and enforces 22°C–26°C comfort boundaries.
  - **LAYER 4: DECISION COCKPIT**
    - *Interface:* Interactive Dashboard • Zone Analytics • Scenario Lab • Recommendations
    - *Detail:* Delivers explainable operating recommendations to facility managers with quantified kWh and ₹ impact.
- **Footer:** Slide 4 of 10

---

### SLIDE 5: WHAT WE ACTUALLY BUILT
- **Top Tracker:** `WORKING SOFTWARE PROTOTYPE`
- **Main Title:** **WHAT WE ACTUALLY BUILT**
- **Right Header Badge:** `LIVE DEMO READY` (Emerald Green `#10B981`)
- **Subtitle Callout:**
  - *A fully functional software simulation prototype & analytics decision support platform.*
- **Main Visual (Left / Center):**
  - **Actual Live Screenshot of EcoSense AI Dashboard:** Framed in a sleek browser container showing live KPI telemetry (10.7 kW current load, 15,816 kWh energy saved, 150.1 kW peak shaved, 89.6% comfort compliance), the 24h Hourly Building Demand Profile chart, and Zone Energy Breakdown!
- **4 Stacked Capability Cards (Right Side):**
  1. **DASHBOARD:** Monitor simulated building performance (Live 24h demand timeseries, current zone telemetry, and active optimization status).
  2. **ZONE ANALYTICS:** Inspect 5 building zones (Granular occupancy, dry-bulb temp, relative humidity, and power breakdown per zone).
  3. **SCENARIO LAB:** Compare optimization strategies (Test Comfort-First, Aggressive Energy, and Peak-Shaving operational trade-offs).
  4. **SIMULATION:** Baseline vs EcoSense evaluation (Side-by-side verification of fixed schedule vs intelligent optimized control).
- **Bottom Technology Stack Pill:**
  - `Technology Stack: Next.js (React) • FastAPI • Python • scikit-learn`
- **Footer:** Slide 5 of 10

---

### SLIDE 6: THE AI ENGINE
- **Top Tracker:** `PREDICTIVE MODELING & MULTI-OBJECTIVE TARGETS`
- **Main Title:** **THE AI ENGINE**
- **Right Header Badge:** `RANDOM FOREST REGRESSOR` (Tech Cyan `#06B6D4`)
- **Left Side:**
  - **Pipeline Ribbon:** `SIMULATED DATA ➔ FEATURE ENGINEERING ➔ RANDOM FOREST ➔ 24-HR FORECAST ➔ OPTIMIZATION`
  - **24-Hour Forecast Chart:** Embedded high-resolution chart showing simulated ground truth (kW), Random Forest forecast (kW), and approximate empirical prediction bands ($\pm 1.645 \times \text{MAE}$).
- **Right Side:**
  - **Card 1: MODEL ACCURACY METRICS**
    - $R^2 \approx 0.942$ (94.2% Variance Explained)
    - $\text{MAE} \approx 3.85\text{ kW}$ (Mean Absolute Error)
    - $\text{RMSE} \approx 5.21\text{ kW}$ (Root Mean Squared Error)
    - *Provenance:* Chronological 80/20 train-test split on 30-day simulated telemetry.
  - **Card 2: OPTIMIZATION TARGETS**
    - *Energy:* Minimize active power consumption across all zones.
    - *Comfort:* Maintain 22°C – 26°C occupied indoor temperature.
    - *Peak Demand:* Keep whole-building draw $\le 175\text{ kW}$ threshold.
- **Bottom Scientific Clarification:**
  - *Approximate empirical prediction band defined as forecast $\pm 1.645 \times \text{MAE}$.*
- **Footer:** Slide 6 of 10

---

### SLIDE 7: WHAT DID THE PROTOTYPE SHOW?
- **Top Tracker:** `SIMULATION RESULTS & PERFORMANCE EVALUATION`
- **Main Title:** **WHAT DID THE PROTOTYPE SHOW?**
- **Right Header Badge:** `SIMULATION RESULT` (Emerald Green `#10B981`)
- **Top Row — 3 Large Bold Impact Metrics:**
  1. **27.8% SIMULATED ENERGY REDUCTION**
     - Baseline: **56,961.7 kWh** ➔ EcoSense: **41,145.4 kWh**
     - Saved: **15,816.3 kWh** across 30 days
  2. **23.2% SIMULATED PEAK SHAVED**
     - Baseline: **195.4 kW** ➔ EcoSense: **150.1 kW**
     - Shaved: **45.3 kW** (Kept safely $\le 175\text{ kW}$ threshold)
  3. **₹134,433 SIMULATED 30-DAY COST DIFFERENCE**
     - Baseline: **₹484,170** ➔ EcoSense: **₹349,738**
     - Calculated at commercial electricity tariff ₹8.50/kWh
- **Center Visual:**
  - High-resolution 3-part comparison chart visualizing 30-Day Energy (kWh), Peak Demand (kW), and 30-Day Utility Cost (₹ INR).
- **Mandatory Bottom Disclaimer Card:**
  > **SIMULATION RESULT — NOT MEASURED REAL-WORLD BUILDING DATA**  
  > *Compared with defined fixed-schedule baseline across 5 simulated zones (~2,300 m²).*
- **Footer:** Slide 7 of 10

---

### SLIDE 8: WHY ECOSENSE AI?
- **Top Tracker:** `COMPETITIVE DIFFERENTIATION & CORE VALUE`
- **Main Title:** **WHY ECOSENSE AI?**
- **Right Header Badge:** `WHY WE WIN` (Emerald Green `#10B981`)
- **4 Large Distinct Quadrant Cards:**
  1. **01 | ENERGY + COMFORT + PEAK**
     - *Optimizes all three instead of energy alone.*
     - Traditional systems often cut energy by sacrificing occupant comfort.
     - EcoSense AI strictly guards the 22°C–26°C comfort boundary.
     - Simultaneously manages peak demand charges ($\le 175\text{ kW}$ threshold).
  2. **02 | PREDICTIVE DEMAND FORECASTING**
     - *Forecasts demand before peak periods arrive.*
     - Proactively anticipates afternoon thermal and occupancy surges.
     - Enables smart pre-cooling during low-tariff, low-demand morning hours.
     - Prevents reactive throttling when peak demand penalties kick in.
  3. **03 | ZONE-AWARE INTELLIGENCE**
     - *Different zones receive different recommendations.*
     - Evaluates conference rooms, cafeteria, and open offices individually.
     - Applies dynamic setbacks only to vacant or partially occupied zones.
     - Eliminates clumsy whole-building blanket setpoint adjustments.
  4. **04 | ACTIONABLE & EXPLAINABLE**
     - *Turns predictions into clear operating recommendations.*
     - Delivers quantified kWh and cost savings for every proposed action.
     - Provides transparent rationale for facility manager verification.
     - Keeps humans in the loop for safe, accountable supervisory control.
- **Bottom Callout:**
  > *"Not just a dashboard. A decision-support layer for smarter buildings."*
- **Footer:** Slide 8 of 10

---

### SLIDE 9: FROM PROTOTYPE TO REAL BUILDINGS
- **Top Tracker:** `IMPLEMENTATION ROADMAP & VALUE REALIZATION`
- **Main Title:** **FROM PROTOTYPE TO REAL BUILDINGS**
- **Right Header Badge:** `4-PHASE ROADMAP` (Tech Cyan `#06B6D4`)
- **Top Row — 4 Progressive Implementation Phases:**
  1. **NOW: SOFTWARE PROTOTYPE (Simulation + ML + optimization + dashboard)**
     - 30-day multi-zone simulation
     - Random Forest demand forecasting
     - Multi-objective optimization cockpit
  2. **NEXT: SENSOR PILOT (Occupancy + temperature + IAQ + energy meters)**
     - IoT sensor deployment in 1 zone
     - Validate ground-truth thermal inertia
     - Refine empirical prediction models
  3. **THEN: BMS INTEGRATION (HVAC + lighting supervisory control)**
     - BACnet / Modbus protocol bridge
     - Automated setpoint recommendations
     - Supervised closed-loop control
  4. **SCALE: MULTI-BUILDING FLEET (Continuous learning + portfolio management)**
     - Cross-building knowledge transfer
     - Enterprise portfolio dashboard
     - Grid interactive demand response
- **Bottom Card — EXPECTED OPERATIONAL VALUE:**
  - *ENERGY:* Reduce unnecessary consumption during low/zero occupancy hours.
  - *PEAK DEMAND:* Reduce avoidable afternoon demand spikes to curb maximum demand charges.
  - *COMFORT:* Strictly maintain 22°C–26°C target across all occupied spaces.
  - *OPERATIONS:* Equip facility managers with actionable, explainable operational guidance.
- **Footnote:**
  - *Roadmap represents planned progression. Future phases require physical hardware pilots and BMS integration.*
- **Footer:** Slide 9 of 10

---

### SLIDE 10: CONCLUSION & VISION
- **Top Tracker:** `YUVA YODHA ENERGY TECH HACKATHON 2026`
- **Main Title:** **BUILDING SMARTER, NOT JUST USING LESS**
- **Right Header Badge:** `CONCLUSION & VISION` (Emerald Green `#10B981`)
- **Hero Center Showcase:**
  - Project Title: **ECOSENSE AI** (36pt Bold Emerald Green)
  - Subtitle: **Intelligent Building Energy Optimizer** (18pt Bold Cyan)
  - Core Closing Vision:
    > *"Turning building data into smarter energy decisions."*
  - **3 Core Outcome Badges (Cleanly Positioned With Zero Overlap):**
    - `[ 27.8% | Simulated Energy Reduction ]`
    - `[ 23.2% | Simulated Peak Shaved ]`
    - `[ 22°C–26°C | Strict Comfort Target Guard ]`
- **Bottom Left Card (Team NOVA):**
  - Team: **TEAM NOVA** • Yuva Yodha Energy Tech Hackathon 2026
  - Team Lead: **Dharshine V** | `vdharshine19@gmail.com`
  - Challenge: **Smart Buildings**
- **Bottom Right Card (Current Status):**
  - Status: **CURRENT STATUS**
  - Description: Functional software simulation and decision-support prototype. Evaluated on 5 commercial zones with 30-day deterministic telemetry.
- **Footer:** Slide 10 of 10

---

## Verified Evaluation Figures & Technical Grounding

| Parameter / Metric | Measured Prototype Value | Provenance / Context |
| :--- | :---: | :--- |
| **Baseline 30-Day Energy** | **56,961.7 kWh** | Fixed-schedule operation (07:00–19:00, constant 22°C setpoint) |
| **EcoSense 30-Day Energy** | **41,145.4 kWh** | AI-driven dynamic setback + load modulation |
| **Simulated Energy Saved** | **15,816.3 kWh (27.8%)** | Calculated vs defined fixed-schedule baseline |
| **Baseline Peak Demand** | **195.4 kW** | Midday peak load coincidence |
| **EcoSense Peak Demand** | **150.1 kW (23.2% shaved)** | Kept under 175 kW threshold via predictive pre-cooling |
| **30-Day Cost Difference** | **₹134,433 saved** | Calculated at commercial electricity tariff ₹8.50/kWh |
| **Simulated $CO_2$ Reduction**| **12,969.4 kg $CO_2$** | CEA grid emission factor ($0.82\text{ kg }CO_2/\text{kWh}$) |
| **Machine Learning Model** | **Random Forest Regressor** | Scikit-learn, 100 estimators, 24-hour ahead horizon |
| **Model Fit ($R^2$)** | **$\approx 0.942$** | Chronological 80/20 train-test split |
| **Forecast MAE / RMSE** | **$3.85\text{ kW}$ / $5.21\text{ kW}$** | Mean Absolute Error / Root Mean Squared Error |
| **Prediction Band** | **$\pm 1.645 \times \text{MAE}$** | Approximate empirical prediction band |
| **Comfort Boundary** | **22°C – 26°C** | Strict indoor temperature proxy enforced across all zones |
