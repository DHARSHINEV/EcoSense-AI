"use client";

import React from "react";
import {
  ResponsiveContainer,
  AreaChart,
  Area,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
} from "recharts";
import { ForecastResponse } from "../lib/types";
import { Badge } from "./Badge";
import { BrainCircuit, CheckCircle2 } from "lucide-react";

interface DemandForecastChartProps {
  forecastData: ForecastResponse;
}

export const DemandForecastChart: React.FC<DemandForecastChartProps> = ({ forecastData }) => {
  const chartData = forecastData.forecast_points.map((p) => ({
    time: `${p.hour}:00`,
    predicted: p.predicted_demand_kw,
    actual: p.actual_simulated_demand_kw,
    lower: p.lower_bound_kw,
    upper: p.upper_bound_kw,
    band: [p.lower_bound_kw, p.upper_bound_kw],
  }));

  return (
    <div className="rounded-xl bg-slate-900/90 border border-slate-800 p-5 shadow-lg backdrop-blur-sm">
      <div className="flex flex-col md:flex-row md:items-center justify-between pb-4 border-b border-slate-800 gap-3">
        <div>
          <div className="flex items-center space-x-2">
            <div className="p-1.5 rounded bg-purple-950/60 border border-purple-800 text-purple-400">
              <BrainCircuit className="w-4 h-4" />
            </div>
            <h2 className="text-sm font-semibold text-white uppercase tracking-wider">
              AI Near-Term Demand Forecast (Next 12 Hours)
            </h2>
            <Badge label="MODEL PREDICTIONS" variant="prediction" />
          </div>
          <p className="text-xs text-slate-400 mt-1">
            Scikit-Learn RandomForestRegressor trained on chronological multi-zone telemetry (no look-ahead leakage)
          </p>
        </div>

        {/* Model Accuracy Badges */}
        <div className="flex flex-wrap items-center gap-2 text-xs font-mono">
          <div className="px-2.5 py-1 rounded bg-slate-800/90 border border-slate-700 text-slate-300">
            <span className="text-slate-500">R² Score: </span>
            <span className="text-emerald-400 font-bold">{forecastData.r2_score}</span>
          </div>
          <div className="px-2.5 py-1 rounded bg-slate-800/90 border border-slate-700 text-slate-300">
            <span className="text-slate-500">MAE: </span>
            <span className="text-purple-300 font-bold">{forecastData.mae_kw} kW</span>
          </div>
          <div className="px-2.5 py-1 rounded bg-slate-800/90 border border-slate-700 text-slate-300">
            <span className="text-slate-500">RMSE: </span>
            <span className="text-purple-300 font-bold">{forecastData.rmse_kw} kW</span>
          </div>
        </div>
      </div>

      <div className="h-72 mt-4">
        <ResponsiveContainer width="100%" height="100%">
          <AreaChart data={chartData} margin={{ top: 10, right: 20, left: -10, bottom: 0 }}>
            <defs>
              <linearGradient id="predictionBand" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="#a855f7" stopOpacity={0.25} />
                <stop offset="95%" stopColor="#a855f7" stopOpacity={0.02} />
              </linearGradient>
            </defs>
            <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" />
            <XAxis dataKey="time" stroke="#64748b" tick={{ fill: "#64748b", fontSize: 11 }} />
            <YAxis stroke="#64748b" tick={{ fill: "#64748b", fontSize: 11 }} unit=" kW" />
            <Tooltip
              contentStyle={{
                backgroundColor: "#0f172a",
                borderColor: "#334155",
                borderRadius: "8px",
                fontSize: "12px",
              }}
            />
            {/* Approximate Empirical Prediction Band */}
            <Area
              type="monotone"
              dataKey="upper"
              stroke="none"
              fill="url(#predictionBand)"
              name="Upper Empirical Band"
            />
            <Area
              type="monotone"
              dataKey="lower"
              stroke="none"
              fill="#0f172a"
              name="Lower Empirical Band"
            />
            {/* Ground Truth Simulated Actual */}
            <Line
              type="monotone"
              dataKey="actual"
              name="Simulated Ground Truth (kW)"
              stroke="#64748b"
              strokeWidth={1.5}
              strokeDasharray="3 3"
              dot={false}
            />
            {/* Predicted Demand */}
            <Line
              type="monotone"
              dataKey="predicted"
              name="ML Forecast (kW)"
              stroke="#c084fc"
              strokeWidth={2.5}
              dot={{ r: 3, fill: "#c084fc" }}
              activeDot={{ r: 6 }}
            />
          </AreaChart>
        </ResponsiveContainer>
      </div>

      <div className="mt-3 flex items-center justify-between text-xs text-slate-400 border-t border-slate-800/80 pt-2 font-mono">
        <span className="flex items-center space-x-1.5">
          <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" />
          <span>Features: [Hour, DayOfWeek, Occupancy, AmbientTemp, Humidity, Lag1h, Lag24h]</span>
        </span>
        <span className="text-slate-500">Shaded area represents approximate empirical prediction band (±1.645 × MAE)</span>
      </div>
    </div>
  );
};
