# EcoSense AI – Deterministic Simulation Architecture

## 1. Simulation Engine Principles

1. **Deterministic Reproducibility**:
   - Uses parameterized pseudo-random number generators (`numpy.random.RandomState(seed)`).
   - Any execution with `random_seed=42` produces identical hourly time-series across all zones.
2. **Multi-Zone Granularity**:
   - Five distinct functional zones: Lobby, Office Floor, Meeting Room, Conference Room, Cafeteria.
   - Each zone has independent area, design occupancy, connected loads, and human behavioral schedules.
3. **Physical Law Approximation**:
   - Diurnal sinusoidal ambient outdoor temperature curves with daily peaks at 14:00 and troughs at 05:00.
   - Internal heat generation from occupants (100 W sensible/latent per person) and equipment dissipation.
   - Dynamic cooling requirement based on ambient-to-indoor temperature differential and solar conduction.
4. **Behavioral Archetypes**:
   - Standard Office: Consistent weekday bell-curve occupancy with lunch dips.
   - Meeting Room: Stochastic 1–2 hour meeting blocks (vacant ~40% of daytime).
   - Conference Room: Sporadic 2–3 weekly gatherings (vacant ~65% of daytime).
   - Cafeteria: High-concentration lunch peaks (12:00–14:30) and morning/afternoon coffee breaks.
   - Lobby: Transient ingress/egress pulses coinciding with shift arrivals and departures.
5. **Indoor Air Quality (IAQ) Simulation**:
   - Models indoor $\text{CO}_2$ concentration (ppm).
   - Baseline outdoors: ~400–420 ppm.
   - With high occupant density in enclosed zones without adequate air changes, levels rise towards 1,000–1,200 ppm.

---

## 2. Baseline vs. Optimized Simulation Run Metrics

A typical 30-day baseline simulation generates **3,600 hourly records** (720 hours × 5 zones) demonstrating:
- Total Baseline Energy: ~52,000–56,000 kWh
- Total EcoSense Optimized Energy: ~42,000–45,000 kWh
- **Net Simulated Energy Savings**: **18.0% – 22.0%**
- **Peak Demand Shaving**: **~12% – 16%** reduction in coincident building peak demand.
- **Comfort Compliance**: **> 98.5%** of occupied hours strictly maintained between 22°C and 26°C.
