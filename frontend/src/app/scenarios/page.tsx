"use client";

import React, { useEffect, useState } from "react";
import { api } from "../../lib/api";
import { ScenarioResult } from "../../lib/types";
import { Badge } from "../../components/Badge";
import {
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  Legend,
} from "recharts";
import { 
  Zap, 
  TrendingDown, 
  ShieldCheck, 
  DollarSign, 
  CheckCircle2, 
  Layers, 
  Activity 
} from "lucide-react";

export default function ScenariosPage() {
  const [scenarios, setScenarios] = useState<ScenarioResult[]>([]);
  const [selectedScenarioId, setSelectedScenarioId] = useState<string>("scenario_d");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchScenarios = async () => {
      try {
        const res = await api.getScenarios();
        setScenarios(res);
      } catch (err) {
        console.error("Failed to load scenarios:", err);
      } finally {
        setLoading(false);
      }
    };
    fetchScenarios();
  }, []);

  const selectedScenario = scenarios.find((s) => s.scenario_id === selectedScenarioId) || scenarios[3];

  const chartData = scenarios.map((s) => ({
    name: s.name.split(":")[0],
    energy_kwh: s.total_energy_kwh,
    peak_kw: s.peak_demand_kw,
    cost_inr: Math.round(s.total_cost_inr / 1000), // In thousands
    comfort_pct: s.comfort_compliance_pct,
  }));

  if (loading) {
    return (
      <div className="min-h-[70vh] flex items-center justify-center font-mono text-xs text-slate-400">
        Loading Scenario Simulation Engine...
      </div>
    );
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-6 border-b border-slate-800 gap-4">
        <div>
          <div className="flex items-center space-x-3">
            <h1 className="text-2xl font-bold text-white tracking-tight">Scenario Lab</h1>
            <Badge label="SIMULATION RESULT" variant="result" />
          </div>
          <p className="text-xs text-slate-400 mt-1">
            Comparative analysis across 4 progressive tiers of building automation and intelligence
          </p>
        </div>
      </div>

      {/* Scenario Cards Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        {scenarios.map((scen) => {
          const isSelected = scen.scenario_id === selectedScenarioId;
          return (
            <div
              key={scen.scenario_id}
              onClick={() => setSelectedScenarioId(scen.scenario_id)}
              className={`p-5 rounded-2xl border transition-all cursor-pointer flex flex-col justify-between ${
                isSelected
                  ? "bg-slate-900 border-emerald-500 shadow-xl shadow-emerald-950/40 ring-1 ring-emerald-500"
                  : "bg-slate-900/60 border-slate-800 hover:border-slate-700"
              }`}
            >
              <div>
                <div className="flex items-center justify-between mb-2">
                  <span
                    className={`font-mono text-[10px] px-2 py-0.5 rounded font-bold uppercase ${
                      scen.scenario_id === "scenario_d"
                        ? "bg-emerald-500/20 text-emerald-400"
                        : scen.scenario_id === "scenario_a"
                        ? "bg-slate-800 text-slate-400"
                        : "bg-blue-500/20 text-blue-400"
                    }`}
                  >
                    {scen.scenario_id === "scenario_a"
                      ? "Baseline Tier"
                      : scen.scenario_id === "scenario_d"
                      ? "Full Intelligence"
                      : "Intermediate"}
                  </span>

                  {isSelected && (
                    <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />
                  )}
                </div>

                <h3 className="text-sm font-bold text-white tracking-tight">
                  {scen.name}
                </h3>
                <p className="text-xs text-slate-400 mt-2 leading-relaxed">
                  {scen.description}
                </p>
              </div>

              <div className="mt-5 pt-4 border-t border-slate-800/80 space-y-2 text-xs font-mono">
                <div className="flex justify-between">
                  <span className="text-slate-500">Energy (30d):</span>
                  <span className="text-white font-bold">{scen.total_energy_kwh.toLocaleString()} kWh</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-slate-500">Peak Demand:</span>
                  <span className="text-cyan-400 font-bold">{scen.peak_demand_kw} kW</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-slate-500">Net Savings:</span>
                  <span className="text-emerald-400 font-bold">{scen.energy_savings_pct}%</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-slate-500">Comfort Rate:</span>
                  <span className="text-purple-300 font-bold">{scen.comfort_compliance_pct}%</span>
                </div>
              </div>
            </div>
          );
        })}
      </div>

      {/* Direct Side-by-Side Comparison Charts */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Total Energy Consumption (kWh) */}
        <div className="rounded-xl bg-slate-900/90 border border-slate-800 p-5 shadow-lg backdrop-blur-sm">
          <div className="pb-4 border-b border-slate-800 flex items-center justify-between">
            <div>
              <h3 className="text-sm font-semibold text-white uppercase tracking-wider">
                Total Energy Consumption (kWh)
              </h3>
              <p className="text-xs text-slate-400 mt-0.5">30-day cumulative electrical energy consumed</p>
            </div>
            <Badge label="SIMULATION RESULT" variant="result" size="sm" />
          </div>

          <div className="h-64 mt-4">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={chartData} margin={{ top: 10, right: 10, left: -10, bottom: 0 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" />
                <XAxis dataKey="name" stroke="#64748b" tick={{ fill: "#64748b", fontSize: 11 }} />
                <YAxis stroke="#64748b" tick={{ fill: "#64748b", fontSize: 11 }} unit=" kWh" />
                <Tooltip
                  contentStyle={{
                    backgroundColor: "#0f172a",
                    borderColor: "#334155",
                    borderRadius: "8px",
                    fontSize: "12px",
                  }}
                />
                <Bar dataKey="energy_kwh" name="Energy (kWh)" fill="#059669" radius={[4, 4, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Coincident Peak Demand (kW) */}
        <div className="rounded-xl bg-slate-900/90 border border-slate-800 p-5 shadow-lg backdrop-blur-sm">
          <div className="pb-4 border-b border-slate-800 flex items-center justify-between">
            <div>
              <h3 className="text-sm font-semibold text-white uppercase tracking-wider">
                Peak Demand Shaving (kW)
              </h3>
              <p className="text-xs text-slate-400 mt-0.5">Maximum instantaneous grid load recorded</p>
            </div>
            <Badge label="SIMULATION RESULT" variant="result" size="sm" />
          </div>

          <div className="h-64 mt-4">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={chartData} margin={{ top: 10, right: 10, left: -10, bottom: 0 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" />
                <XAxis dataKey="name" stroke="#64748b" tick={{ fill: "#64748b", fontSize: 11 }} />
                <YAxis stroke="#64748b" tick={{ fill: "#64748b", fontSize: 11 }} unit=" kW" />
                <Tooltip
                  contentStyle={{
                    backgroundColor: "#0f172a",
                    borderColor: "#334155",
                    borderRadius: "8px",
                    fontSize: "12px",
                  }}
                />
                <Bar dataKey="peak_kw" name="Peak Demand (kW)" fill="#0284c7" radius={[4, 4, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>

      {/* Comparative Evaluation Table */}
      <div className="rounded-xl bg-slate-900/90 border border-slate-800 overflow-hidden shadow-lg backdrop-blur-sm">
        <div className="p-5 border-b border-slate-800">
          <h3 className="text-sm font-semibold text-white uppercase tracking-wider">
            Detailed Scenario Performance Matrix
          </h3>
          <p className="text-xs text-slate-400 mt-0.5">
            Side-by-side technical trade-off matrix: Energy vs Peak Shaving vs Operating Cost vs Comfort
          </p>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs font-mono">
            <thead className="bg-slate-950/80 text-slate-400 border-b border-slate-800">
              <tr>
                <th className="p-4">Scenario</th>
                <th className="p-4">Total Energy</th>
                <th className="p-4">Peak kW</th>
                <th className="p-4">Operating Cost</th>
                <th className="p-4">Net Savings</th>
                <th className="p-4">Comfort Compliance</th>
                <th className="p-4">CO₂ Reduction</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/80 text-slate-300">
              {scenarios.map((s) => (
                <tr
                  key={s.scenario_id}
                  className={`hover:bg-slate-800/50 transition-colors ${
                    s.scenario_id === selectedScenarioId ? "bg-emerald-950/20 text-white font-semibold" : ""
                  }`}
                >
                  <td className="p-4 font-sans font-medium text-white">{s.name}</td>
                  <td className="p-4">{s.total_energy_kwh.toLocaleString()} kWh</td>
                  <td className="p-4 text-cyan-300">{s.peak_demand_kw} kW</td>
                  <td className="p-4">₹{Math.round(s.total_cost_inr).toLocaleString()}</td>
                  <td className="p-4 text-emerald-400 font-bold">{s.energy_savings_pct}%</td>
                  <td className="p-4 text-purple-300">{s.comfort_compliance_pct}%</td>
                  <td className="p-4 text-slate-400">{Math.round(s.co2_reduction_kg).toLocaleString()} kg</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
