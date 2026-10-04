# EcoSense AI – Intelligent Building Energy Optimizer

> **Yuva Yodha Energy Tech Hackathon 2026**  
> **Track**: Smart Buildings – Energy Efficiency & Occupant Experience  
> **Core Concept**: SENSE → PREDICT → OPTIMIZE → RECOMMEND → MEASURE  

---

## ⚡ Executive Summary

**EcoSense AI** is a runnable engineering prototype of an AI-driven building energy optimization platform. It demonstrates how commercial buildings can dynamically reduce energy waste, understand spatial occupancy, predict near-term energy demand with machine learning, clip expensive grid peak loads, and preserve occupant comfort within strict standards (22°C–26°C).

### Scientific Integrity & Anti-Hallucination Declarations:
- All generated telemetry is explicitly labeled **`SIMULATED DATA`**.
- All machine learning forecasts are explicitly labeled **`MODEL PREDICTION`**.
- All optimization advisories are labeled **`OPTIMIZATION RECOMMENDATION`**.
- All calculated energy and cost savings are explicitly labeled **`SIMULATION RESULT`**.
- No fabricated customer names, physical testbed certifications, or partnerships are claimed.

---

## 🚀 Quickstart Guide

### Prerequisites
- **Python**: 3.10+ (tested on Python 3.14)
- **Node.js**: 18+ (tested on Node.js v24.18) & npm

### 1. Backend Startup (FastAPI + ML Engine)
From the repository root:
```bash
# Optional: create virtualenv
# python -m venv venv && source venv/bin/activate (or .\venv\Scripts\Activate.ps1)

# Install Python requirements
pip install -r requirements.txt

# Start backend server on port 8000
python -m uvicorn backend.app.main:app --host 0.0.0.0 --port 8000 --reload
```
The backend initializes the 30-day deterministic simulation, trains the RandomForestRegressor, and serves the REST API at `http://localhost:8000`.  
- API Health Check: `http://localhost:8000/health`  
- Interactive API Docs (Swagger): `http://localhost:8000/docs`

### 2. Frontend Startup (Next.js Dashboard)
In a separate terminal:
```bash
cd frontend
npm install
npm run dev
```
Open your browser at `http://localhost:3000`.

### 3. Run Backend Automated Tests
```bash
# In project root:
$env:PYTHONPATH="backend"; python -m pytest tests/ -v
```
All 23 unit and integration tests validate deterministic simulation, baseline calculations, ML anti-leakage training, comfort boundaries, optimization policies, and API endpoints.

---

## 📂 Repository Architecture

```
ecosense-ai/
├── backend/
│   └── app/
│       ├── api/endpoints.py       # FastAPI REST endpoints
│       ├── config.py              # Facility parameters & tariffs
│       ├── data_store/db.py       # In-memory cached state store
│       ├── main.py                # ASGI application entrypoint
│       ├── ml/demand_predictor.py # Scikit-Learn RandomForestRegressor
│       ├── models/schemas.py      # Pydantic data contracts
│       ├── optimization/          # Multi-objective engine & comfort model
│       └── simulation/            # Multi-zone physics & baseline model
├── data/                          # Exported simulation summary JSON
├── docs/
│   ├── ARCHITECTURE.md            # Detailed system architecture
│   ├── ASSUMPTIONS.md             # Numerical & physical parameters
│   ├── DEPLOYMENT.md              # 4-stage retrofit roadmap & economics
│   ├── JUDGE_DEMO.md              # 2-minute pitch script for judges
│   ├── LIMITATIONS.md             # Technical boundaries & disclosures
│   ├── ML_METHODOLOGY.md          # Anti-leakage ML pipeline & metrics
│   ├── OPTIMIZATION.md            # Multi-objective rule specs & constraints
│   ├── PRESENTATION_CONTENT.md    # 10-slide deck content
│   └── SIMULATION.md              # Thermodynamics & behavioral models
├── frontend/                      # Next.js App Router (TypeScript + Tailwind)
│   └── src/
│       ├── app/                   # Dashboard, Zones, Scenario Lab, Deployment
│       ├── components/            # Charts, KPI cards, recommendation modals
│       └── lib/                   # API client & TypeScript interfaces
├── models/                        # Serialized ML model checkpoint
├── tests/                         # 23 automated unit & integration tests
├── requirements.txt               # Backend dependencies
├── .env.example                   # Environment configuration template
└── README.md
```

---

## 📊 Core Features & Capabilities

1. **Deterministic Multi-Zone Simulation**: 5 zones (Lobby, Office Floor, Meeting Room, Conference Room, Cafeteria) modeling occupancy dynamics, ambient weather curves, thermal loads, and $\text{CO}_2$ air quality.
2. **Standardized Baseline Comparison**: Simulates conventional commercial fixed schedules (07:00–20:00, 22°C setpoint, 100% lighting) as a benchmark.
3. **Real Machine Learning Engine**: Scikit-Learn RandomForestRegressor ($R^2 \approx 0.94$, $\text{MAE} \approx 3.8\text{ kW}$) trained on chronological splits without temporal data leakage.
4. **Multi-Objective Optimization**: Dynamic setback, daylight harvesting, and predictive peak demand shaving while guaranteeing comfort (22°C–26°C).
5. **Interactive Manager Cockpit**: Building managers can accept, dismiss, or review AI advisories with instant status persistence.
6. **Scenario Lab**: Side-by-side comparison of 4 operational strategies: Baseline, Occupancy-Aware, Predictive Pre-Cooling, and Full EcoSense Optimization.
7. **Interactive Payback Calculator**: Configurable CapEx, OpEx, and tariff inputs demonstrating payback in under 5 months.
