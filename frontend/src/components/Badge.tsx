import React from "react";

interface BadgeProps {
  label: string;
  variant?: "simulated" | "prediction" | "result" | "recommendation" | "baseline" | "default";
  size?: "sm" | "md";
}

export const Badge: React.FC<BadgeProps> = ({ label, variant, size = "sm" }) => {
  let colorStyles = "bg-slate-800 text-slate-300 border-slate-700";

  // Derive variant if not explicitly provided
  const l = label.toUpperCase();
  if (variant === "simulated" || l.includes("SIMULATED DATA")) {
    colorStyles = "bg-cyan-950/80 text-cyan-300 border-cyan-700/60";
  } else if (variant === "prediction" || l.includes("MODEL PREDICTION")) {
    colorStyles = "bg-purple-950/80 text-purple-300 border-purple-700/60";
  } else if (variant === "result" || l.includes("SIMULATION RESULT")) {
    colorStyles = "bg-emerald-950/80 text-emerald-300 border-emerald-700/60";
  } else if (variant === "recommendation" || l.includes("OPTIMIZATION RECOMMENDATION") || l.includes("RECOMMENDATION")) {
    colorStyles = "bg-amber-950/80 text-amber-300 border-amber-700/60";
  } else if (variant === "baseline" || l.includes("BASELINE")) {
    colorStyles = "bg-slate-800/90 text-slate-300 border-slate-600";
  }

  const sizeStyles = size === "sm" ? "text-[10px] px-2 py-0.5" : "text-xs px-2.5 py-1";

  return (
    <span
      className={`inline-flex items-center font-mono font-semibold tracking-wider uppercase rounded-full border ${colorStyles} ${sizeStyles}`}
    >
      <span className="w-1.5 h-1.5 rounded-full bg-current mr-1.5 animate-pulse" />
      {label}
    </span>
  );
};
