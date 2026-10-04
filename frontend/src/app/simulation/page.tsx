"use client";

import React, { useState } from "react";
import { api } from "../../lib/api";
import { BuildingSummary } from "../../lib/types";
import { Badge } from "../../components/Badge";
import { 
  Sliders, 
  RefreshCw, 
  RotateCcw, 
  Zap, 
  CheckCircle2, 
  ShieldAlert, 
  Sparkles,
  TrendingDown,
  Thermometer
} from "lucide-react";

export default function SimulationPage() {
  const [days, setDays] = useState<number>(30);
  const [tariff, setTariff] = useState<number>(8.5);
  const [minTemp, setMinTemp] = useState<number>(22.0);
  const [maxTemp, setMaxTemp] = useState<number>(26.0);
  const [peakThreshold, setPeakThreshold] = useState<number>(175.0);
  const [seed, setSeed] = useState<number>(42);

  const [loading, setLoading] = useState<boolean>(false);
  const [message, setMessage] = useState<string | null>(null);
  const [updatedSummary, setUpdatedSummary] = useState<BuildingSummary | null>(null);

  const handleGenerateSimulation = async () => {
    setLoading(true);
    setMessage(null);
    try {
      const res = await api.runSimulation({
        simulation_days: Number(days),
        electricity_tariff: Number(tariff),
        min_comfort_temp: Number(minTemp),
        max_comfort_temp: Number(maxTemp),
        peak_demand_threshold_kw: Number(peakThreshold),
        random_seed: Number(seed),
      });
      setMessage(res.message);
      setUpdatedSummary(res.summary);
    } catch (err: any) {
      console.error("Simulation generation failed:", err);
      setMessage("Failed to run simulation. Please ensure backend is running.");
    } finally {
      setLoading(false);
    }
  };

  const handleRunOptimization = async () => {
    setLoading(true);
    setMessage(null);
    try {
      const res = await api.runOptimization();
      setMessage(res.message);
      setUpdatedSummary(res.summary);
    } catch (err: any) {
      console.error("Optimization failed:", err);
      setMessage("Failed to re-run optimization.");
    } finally {
      setLoading(false);
    }
  };

  const handleResetDefaults = () => {
    setDays(30);
    setTariff(8.5);
    setMinTemp(22.0);
    setMaxTemp(26.0);
    setPeakThreshold(175.0);
    setSeed(42);
    setMessage("Parameters reset to standard defaults.");
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-6 border-b border-slate-800 gap-4">
        <div>
          <div className="flex items-center space-x-3">
            <h1 className="text-2xl font-bold text-white tracking-tight">Simulation Engine & Controls</h1>
            <Badge label="CONFIGURABLE ENGINE" variant="default" />
          </div>
          <p className="text-xs text-slate-400 mt-1">
            Configure physical parameters, utility tariff assumptions, comfort envelopes, and re-run simulations live
          </p>
        </div>

        <button
          onClick={handleResetDefaults}
          className="flex items-center space-x-1.5 px-3 py-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-700 text-xs font-semibold text-slate-300 transition-colors cursor-pointer w-fit"
        >
          <RotateCcw className="w-3.5 h-3.5" />
          <span>Reset Defaults</span>
        </button>
      </div>

      {message && (
        <div className="p-4 rounded-xl bg-emerald-950/60 border border-emerald-800 text-xs text-emerald-300 flex items-center space-x-2">
          <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />
          <span>{message}</span>
        </div>
      )}

      {/* Control Sliders Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {/* Simulation Duration */}
        <div className="p-5 rounded-xl bg-slate-900/90 border border-slate-800 space-y-3">
          <div className="flex justify-between items-center text-xs">
            <span className="font-semibold text-white">Simulation Duration</span>
            <span className="font-mono text-emerald-400 font-bold">{days} Days</span>
          </div>
          <input
            type="range"
            min="7"
            max="60"
            step="1"
            value={days}
            onChange={(e) => setDays(Number(e.target.value))}
            className="w-full accent-emerald-500 cursor-pointer"
          />
          <p className="text-[11px] text-slate-500 font-mono">
            Generates {days * 24 * 5} total hourly zone records (5 zones × 24h × {days}d).
          </p>
        </div>

        {/* Electricity Tariff */}
        <div className="p-5 rounded-xl bg-slate-900/90 border border-slate-800 space-y-3">
          <div className="flex justify-between items-center text-xs">
            <span className="font-semibold text-white">Commercial Electricity Tariff</span>
            <span className="font-mono text-emerald-400 font-bold">₹{tariff.toFixed(2)} / kWh</span>
          </div>
          <input
            type="range"
            min="4.0"
            max="18.0"
            step="0.25"
            value={tariff}
            onChange={(e) => setTariff(Number(e.target.value))}
            className="w-full accent-emerald-500 cursor-pointer"
          />
          <p className="text-[11px] text-slate-500 font-mono">
            Indian state commercial tariff rate benchmark (BESCOM / MSEDCL / Tata Power).
          </p>
        </div>

        {/* Minimum Comfort Limit */}
        <div className="p-5 rounded-xl bg-slate-900/90 border border-slate-800 space-y-3">
          <div className="flex justify-between items-center text-xs">
            <span className="font-semibold text-white">Min Comfort Boundary</span>
            <span className="font-mono text-cyan-400 font-bold">{minTemp.toFixed(1)} °C</span>
          </div>
          <input
            type="range"
            min="19.0"
            max="23.5"
            step="0.5"
            value={minTemp}
            onChange={(e) => setMinTemp(Number(e.target.value))}
            className="w-full accent-cyan-500 cursor-pointer"
          />
          <p className="text-[11px] text-slate-500 font-mono">
            Prevents overcooling complaints in cold/perimeter zones.
          </p>
        </div>

        {/* Maximum Comfort Limit */}
        <div className="p-5 rounded-xl bg-slate-900/90 border border-slate-800 space-y-3">
          <div className="flex justify-between items-center text-xs">
            <span className="font-semibold text-white">Max Comfort Boundary</span>
            <span className="font-mono text-purple-400 font-bold">{maxTemp.toFixed(1)} °C</span>
          </div>
          <input
            type="range"
            min="24.5"
            max="28.0"
            step="0.5"
            value={maxTemp}
            onChange={(e) => setMaxTemp(Number(e.target.value))}
            className="w-full accent-purple-500 cursor-pointer"
          />
          <p className="text-[11px] text-slate-500 font-mono">
            Hard upper limit for allowable setback temperatures during occupied hours.
          </p>
        </div>

        {/* Peak Demand Threshold */}
        <div className="p-5 rounded-xl bg-slate-900/90 border border-slate-800 space-y-3">
          <div className="flex justify-between items-center text-xs">
            <span className="font-semibold text-white">Peak Demand Shaving Threshold</span>
            <span className="font-mono text-amber-400 font-bold">{peakThreshold} kW</span>
          </div>
          <input
            type="range"
            min="120.0"
            max="220.0"
            step="5.0"
            value={peakThreshold}
            onChange={(e) => setPeakThreshold(Number(e.target.value))}
            className="w-full accent-amber-500 cursor-pointer"
          />
          <p className="text-[11px] text-slate-500 font-mono">
            Triggers proactive pre-cooling and flexible load shifting when approached.
          </p>
        </div>

        {/* Deterministic Random Seed */}
        <div className="p-5 rounded-xl bg-slate-900/90 border border-slate-800 space-y-3">
          <div className="flex justify-between items-center text-xs">
            <span className="font-semibold text-white">Random Seed</span>
            <span className="font-mono text-slate-300 font-bold">#{seed}</span>
          </div>
          <input
            type="number"
            min="1"
            max="9999"
            value={seed}
            onChange={(e) => setSeed(Number(e.target.value))}
            className="w-full bg-slate-950 border border-slate-800 rounded-lg px-3 py-1.5 text-xs font-mono text-white"
          />
          <p className="text-[11px] text-slate-500 font-mono">
            Guarantees 100% reproducible scientific simulation runs.
          </p>
        </div>
      </div>

      {/* Action Buttons */}
      <div className="flex flex-wrap items-center gap-4">
        <button
          onClick={handleGenerateSimulation}
          disabled={loading}
          className="flex items-center space-x-2 px-6 py-3 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition-all shadow-lg shadow-emerald-950/40 cursor-pointer disabled:opacity-50"
        >
          <RefreshCw className={`w-4 h-4 ${loading ? "animate-spin" : ""}`} />
          <span>Regenerate Simulation & ML Pipeline</span>
        </button>

        <button
          onClick={handleRunOptimization}
          disabled={loading}
          className="flex items-center space-x-2 px-5 py-3 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 text-white font-semibold text-xs transition-all cursor-pointer disabled:opacity-50"
        >
          <Zap className="w-4 h-4 text-emerald-400" />
          <span>Re-Evaluate Optimization Policies</span>
        </button>
      </div>

      {/* Dynamic Summary Output (if regenerated) */}
      {updatedSummary && (
        <div className="rounded-xl bg-slate-900/90 border border-emerald-500/40 p-6 shadow-xl space-y-4">
          <div className="flex items-center justify-between pb-3 border-b border-slate-800">
            <h3 className="text-sm font-bold text-white uppercase tracking-wider flex items-center space-x-2">
              <CheckCircle2 className="w-4 h-4 text-emerald-400" />
              <span>Newly Computed Simulation Summary</span>
            </h3>
            <Badge label="SIMULATION RESULT" variant="result" />
          </div>

          <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 text-xs font-mono">
            <div className="p-3 rounded-lg bg-slate-950 border border-slate-800">
              <span className="text-slate-500 block">Baseline Energy:</span>
              <span className="text-base font-bold text-white">
                {Math.round(updatedSummary.total_baseline_energy_kwh).toLocaleString()} kWh
              </span>
            </div>
            <div className="p-3 rounded-lg bg-slate-950 border border-slate-800">
              <span className="text-slate-500 block">Optimized Energy:</span>
              <span className="text-base font-bold text-emerald-400">
                {Math.round(updatedSummary.total_optimized_energy_kwh).toLocaleString()} kWh
              </span>
            </div>
            <div className="p-3 rounded-lg bg-slate-950 border border-slate-800">
              <span className="text-slate-500 block">Energy Reduction:</span>
              <span className="text-base font-bold text-emerald-400">
                {updatedSummary.energy_reduction_pct}%
              </span>
            </div>
            <div className="p-3 rounded-lg bg-slate-950 border border-slate-800">
              <span className="text-slate-500 block">Cost Avoidance:</span>
              <span className="text-base font-bold text-cyan-300">
                ₹{Math.round(updatedSummary.cost_savings_inr).toLocaleString()}
              </span>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
