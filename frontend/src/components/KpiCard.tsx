import React from "react";
import { Badge } from "./Badge";
import { LucideIcon } from "lucide-react";

interface KpiCardProps {
  title: string;
  value: string | number;
  unit?: string;
  baselineValue?: string | number;
  change?: string;
  changeType?: "positive" | "negative" | "neutral";
  badgeLabel?: string;
  badgeVariant?: "simulated" | "result" | "prediction" | "recommendation" | "baseline" | "default";
  icon: LucideIcon;
  subtext?: string;
}

export const KpiCard: React.FC<KpiCardProps> = ({
  title,
  value,
  unit,
  baselineValue,
  change,
  changeType = "positive",
  badgeLabel = "SIMULATION RESULT",
  badgeVariant = "result",
  icon: Icon,
  subtext,
}) => {
  return (
    <div className="relative overflow-hidden rounded-xl bg-slate-900/90 border border-slate-800 p-5 shadow-lg backdrop-blur-sm transition-all hover:border-slate-700">
      <div className="flex items-start justify-between">
        <div className="flex items-center space-x-2.5">
          <div className="p-2.5 rounded-lg bg-slate-800/80 border border-slate-700 text-emerald-400">
            <Icon className="w-5 h-5" />
          </div>
          <div>
            <h3 className="text-xs font-medium text-slate-400 uppercase tracking-wider">{title}</h3>
            {badgeLabel && (
              <div className="mt-1">
                <Badge label={badgeLabel} variant={badgeVariant} size="sm" />
              </div>
            )}
          </div>
        </div>
      </div>

      <div className="mt-4 flex items-baseline space-x-2">
        <span className="text-2xl sm:text-3xl font-bold font-mono text-white tracking-tight">
          {value}
        </span>
        {unit && <span className="text-sm font-medium text-slate-400">{unit}</span>}
      </div>

      <div className="mt-3 flex items-center justify-between border-t border-slate-800/80 pt-3 text-xs">
        {baselineValue !== undefined ? (
          <div className="text-slate-400">
            <span className="text-[11px] text-slate-500">Baseline: </span>
            <span className="font-mono text-slate-300 font-semibold">{baselineValue}</span>
          </div>
        ) : (
          <span className="text-slate-500 text-[11px]">{subtext || "Real-time state"}</span>
        )}

        {change && (
          <span
            className={`font-mono font-semibold px-2 py-0.5 rounded ${
              changeType === "positive"
                ? "bg-emerald-500/10 text-emerald-400 border border-emerald-500/20"
                : changeType === "negative"
                ? "bg-rose-500/10 text-rose-400 border border-rose-500/20"
                : "bg-slate-800 text-slate-300"
            }`}
          >
            {change}
          </span>
        )}
      </div>
    </div>
  );
};
