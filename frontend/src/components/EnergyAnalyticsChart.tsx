"use client";

import React from "react";
import {
  ResponsiveContainer,
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  Legend,
  CartesianGrid,
  BarChart,
  Bar,
} from "recharts";
import { HourlyDemandPoint, ZoneBreakdownPoint } from "../lib/types";
import { Badge } from "./Badge";

interface EnergyAnalyticsChartProps {
  hourlyData: HourlyDemandPoint[];
  zoneData: ZoneBreakdownPoint[];
}

export const EnergyAnalyticsChart: React.FC<EnergyAnalyticsChartProps> = ({
  hourlyData,
  zoneData,
}) => {
  return (
    <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
      {/* 24-Hour Building Demand Curve (2 cols) */}
      <div className="lg:col-span-2 rounded-xl bg-slate-900/90 border border-slate-800 p-5 shadow-lg backdrop-blur-sm">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-4 border-b border-slate-800 gap-2">
          <div>
            <div className="flex items-center space-x-2">
              <h2 className="text-sm font-semibold text-white uppercase tracking-wider">
                Hourly Building Demand Profile
              </h2>
              <Badge label="SIMULATION RESULT" variant="result" />
            </div>
            <p className="text-xs text-slate-400 mt-0.5">
              Coincident electric power demand (kW): Fixed-Schedule Baseline vs EcoSense AI Optimization
            </p>
          </div>
          <div className="flex items-center space-x-3 text-xs font-mono">
            <span className="flex items-center space-x-1 text-slate-400">
              <span className="w-2.5 h-2.5 rounded-full bg-slate-400 inline-block" />
              <span>Baseline</span>
            </span>
            <span className="flex items-center space-x-1 text-emerald-400 font-semibold">
              <span className="w-2.5 h-2.5 rounded-full bg-emerald-400 inline-block" />
              <span>EcoSense Optimized</span>
            </span>
          </div>
        </div>

        <div className="h-72 mt-4">
          <ResponsiveContainer width="100%" height="100%">
            <LineChart data={hourlyData} margin={{ top: 10, right: 20, left: -10, bottom: 0 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" />
              <XAxis
                dataKey="time_label"
                stroke="#64748b"
                tick={{ fill: "#64748b", fontSize: 11 }}
              />
              <YAxis
                stroke="#64748b"
                tick={{ fill: "#64748b", fontSize: 11 }}
                unit=" kW"
              />
              <Tooltip
                contentStyle={{
                  backgroundColor: "#0f172a",
                  borderColor: "#334155",
                  borderRadius: "8px",
                  fontSize: "12px",
                }}
                labelStyle={{ color: "#f8fafc", fontWeight: "bold" }}
              />
              <Line
                type="monotone"
                dataKey="baseline_power_kw"
                name="Baseline (kW)"
                stroke="#94a3b8"
                strokeWidth={2}
                strokeDasharray="4 4"
                dot={false}
              />
              <Line
                type="monotone"
                dataKey="optimized_power_kw"
                name="EcoSense (kW)"
                stroke="#10b981"
                strokeWidth={2.5}
                dot={{ r: 2, fill: "#10b981" }}
                activeDot={{ r: 5 }}
              />
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* Energy Consumption by Zone (1 col) */}
      <div className="rounded-xl bg-slate-900/90 border border-slate-800 p-5 shadow-lg backdrop-blur-sm">
        <div className="pb-4 border-b border-slate-800">
          <div className="flex items-center space-x-2">
            <h2 className="text-sm font-semibold text-white uppercase tracking-wider">
              Zone Energy Breakdown
            </h2>
            <Badge label="SIMULATION RESULT" variant="result" />
          </div>
          <p className="text-xs text-slate-400 mt-0.5">
            Total daily energy (kWh) compared across building zones
          </p>
        </div>

        <div className="h-72 mt-4">
          <ResponsiveContainer width="100%" height="100%">
            <BarChart
              data={zoneData}
              layout="vertical"
              margin={{ top: 10, right: 10, left: 10, bottom: 0 }}
            >
              <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" />
              <XAxis type="number" stroke="#64748b" tick={{ fill: "#64748b", fontSize: 10 }} />
              <YAxis
                type="category"
                dataKey="zone_name"
                stroke="#64748b"
                tick={{ fill: "#94a3b8", fontSize: 10 }}
                width={85}
              />
              <Tooltip
                contentStyle={{
                  backgroundColor: "#0f172a",
                  borderColor: "#334155",
                  borderRadius: "8px",
                  fontSize: "12px",
                }}
              />
              <Bar dataKey="baseline_energy_kwh" name="Baseline (kWh)" fill="#475569" radius={[0, 4, 4, 0]} />
              <Bar dataKey="optimized_energy_kwh" name="EcoSense (kWh)" fill="#059669" radius={[0, 4, 4, 0]} />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
};
