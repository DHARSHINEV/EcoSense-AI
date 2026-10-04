"use client";

import React from "react";
import {
  ResponsiveContainer,
  ScatterChart,
  Scatter,
  XAxis,
  YAxis,
  ZAxis,
  Tooltip,
  CartesianGrid,
  Legend,
} from "recharts";
import { OccupancyCorrelationPoint } from "../lib/types";
import { Badge } from "./Badge";
import { Users } from "lucide-react";

interface OccupancyCorrelationChartProps {
  scatterPoints: OccupancyCorrelationPoint[];
}

export const OccupancyCorrelationChart: React.FC<OccupancyCorrelationChartProps> = ({
  scatterPoints,
}) => {
  return (
    <div className="rounded-xl bg-slate-900/90 border border-slate-800 p-5 shadow-lg backdrop-blur-sm">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-4 border-b border-slate-800 gap-2">
        <div>
          <div className="flex items-center space-x-2">
            <div className="p-1.5 rounded bg-cyan-950/60 border border-cyan-800 text-cyan-400">
              <Users className="w-4 h-4" />
            </div>
            <h2 className="text-sm font-semibold text-white uppercase tracking-wider">
              Occupancy vs Power Demand Correlation
            </h2>
            <Badge label="SIMULATED DATA" variant="simulated" />
          </div>
          <p className="text-xs text-slate-400 mt-1">
            Visualizes decoupling of baseline fixed cooling (grey) vs EcoSense occupancy-responsive load (emerald)
          </p>
        </div>

        <div className="flex items-center space-x-3 text-xs font-mono">
          <span className="flex items-center space-x-1 text-slate-400">
            <span className="w-2.5 h-2.5 rounded-full bg-slate-400 inline-block" />
            <span>Baseline Load (Fixed)</span>
          </span>
          <span className="flex items-center space-x-1 text-emerald-400 font-semibold">
            <span className="w-2.5 h-2.5 rounded-full bg-emerald-400 inline-block" />
            <span>EcoSense Dynamic Load</span>
          </span>
        </div>
      </div>

      <div className="h-64 mt-4">
        <ResponsiveContainer width="100%" height="100%">
          <ScatterChart margin={{ top: 10, right: 20, bottom: 10, left: -10 }}>
            <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" />
            <XAxis
              type="number"
              dataKey="occupancy"
              name="Occupancy"
              unit=" persons"
              stroke="#64748b"
              tick={{ fill: "#64748b", fontSize: 11 }}
            />
            <YAxis
              type="number"
              dataKey="baseline_power_kw"
              name="Power"
              unit=" kW"
              stroke="#64748b"
              tick={{ fill: "#64748b", fontSize: 11 }}
            />
            <ZAxis range={[30, 80]} />
            <Tooltip
              cursor={{ strokeDasharray: "3 3" }}
              contentStyle={{
                backgroundColor: "#0f172a",
                borderColor: "#334155",
                borderRadius: "8px",
                fontSize: "12px",
              }}
            />
            <Scatter
              name="Baseline Load"
              data={scatterPoints}
              fill="#64748b"
              dataKey="baseline_power_kw"
              opacity={0.6}
            />
            <Scatter
              name="EcoSense Load"
              data={scatterPoints}
              fill="#10b981"
              dataKey="optimized_power_kw"
              opacity={0.8}
            />
          </ScatterChart>
        </ResponsiveContainer>
      </div>
      <p className="text-[11px] text-slate-500 mt-2 font-mono">
        Note: When occupancy is near 0, EcoSense drops zone power significantly, whereas baseline continues consuming full cooling and lighting power.
      </p>
    </div>
  );
};
