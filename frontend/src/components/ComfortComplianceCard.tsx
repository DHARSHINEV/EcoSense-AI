"use client";

import React from "react";
import { Badge } from "./Badge";
import { Thermometer, ShieldCheck, AlertTriangle } from "lucide-react";

interface ComfortComplianceCardProps {
  compliancePct: number;
  totalViolations: number;
  comfortRange: string;
  currentTemp?: number;
}

export const ComfortComplianceCard: React.FC<ComfortComplianceCardProps> = ({
  compliancePct,
  totalViolations,
  comfortRange,
  currentTemp = 24.2,
}) => {
  return (
    <div className="rounded-xl bg-slate-900/90 border border-slate-800 p-5 shadow-lg backdrop-blur-sm">
      <div className="flex items-center justify-between pb-4 border-b border-slate-800">
        <div className="flex items-center space-x-2">
          <div className="p-1.5 rounded bg-emerald-950/60 border border-emerald-800 text-emerald-400">
            <Thermometer className="w-4 h-4" />
          </div>
          <h2 className="text-sm font-semibold text-white uppercase tracking-wider">
            Temperature-Based Comfort Compliance
          </h2>
          <Badge label="SIMULATION RESULT" variant="result" />
        </div>
        <span className="font-mono text-xs text-slate-400">Simplified Comfort Proxy (22°C–26°C)</span>
      </div>

      <div className="mt-4 grid grid-cols-1 sm:grid-cols-3 gap-4">
        {/* Compliance percentage */}
        <div className="p-4 rounded-xl bg-slate-950/60 border border-slate-800 flex items-center space-x-3">
          <div className="p-2.5 rounded-lg bg-emerald-500/10 text-emerald-400">
            <ShieldCheck className="w-5 h-5" />
          </div>
          <div>
            <span className="text-[11px] text-slate-400 font-medium block">Compliance Rate</span>
            <span className="text-2xl font-bold font-mono text-white tracking-tight">
              {compliancePct}%
            </span>
          </div>
        </div>

        {/* Violations count */}
        <div className="p-4 rounded-xl bg-slate-950/60 border border-slate-800 flex items-center space-x-3">
          <div className="p-2.5 rounded-lg bg-blue-500/10 text-blue-400">
            <AlertTriangle className="w-5 h-5" />
          </div>
          <div>
            <span className="text-[11px] text-slate-400 font-medium block">Occupied Violations</span>
            <span className="text-2xl font-bold font-mono text-white tracking-tight">
              {totalViolations} <span className="text-xs font-normal text-slate-400">hours</span>
            </span>
          </div>
        </div>

        {/* Configured Band */}
        <div className="p-4 rounded-xl bg-slate-950/60 border border-slate-800">
          <span className="text-[11px] text-slate-400 font-medium block">Configured Comfort Band</span>
          <span className="text-lg font-bold font-mono text-emerald-400 tracking-tight block mt-0.5">
            {comfortRange}
          </span>
          <span className="text-[10px] text-slate-500 font-mono">Configured Temperature Constraint</span>
        </div>
      </div>

      {/* Visual Comfort Gauge Bar */}
      <div className="mt-5 p-4 rounded-xl bg-slate-950 border border-slate-800/80">
        <div className="flex justify-between text-xs font-mono text-slate-400 mb-1.5">
          <span>20°C (Cold)</span>
          <span className="text-emerald-400 font-bold">24°C Ideal Comfort</span>
          <span>28°C (Hot)</span>
        </div>
        <div className="relative w-full h-3 bg-slate-800 rounded-full overflow-hidden">
          {/* Green acceptable zone (22 to 26 out of 20 to 28 => 25% to 75%) */}
          <div className="absolute left-[25%] right-[25%] h-full bg-emerald-500/30 border-x border-emerald-400/50" />
          {/* Current Temp Marker */}
          <div
            className="absolute top-0 bottom-0 w-2 bg-emerald-400 rounded-full shadow-md shadow-emerald-400/80 -ml-1 transition-all"
            style={{ left: `${((currentTemp - 20) / (28 - 20)) * 100}%` }}
          />
        </div>
        <div className="flex justify-between items-center text-[11px] text-slate-500 font-mono mt-2">
          <span>Min Limit: 22.0°C</span>
          <span className="text-slate-300 font-semibold">Current Avg: {currentTemp}°C</span>
          <span>Max Limit: 26.0°C</span>
        </div>
      </div>
    </div>
  );
};
