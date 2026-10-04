"use client";

import React, { useState } from "react";
import { AIRecommendation } from "../lib/types";
import { Badge } from "./Badge";
import { RecommendationModal } from "./RecommendationModal";
import { 
  Sparkles, 
  ArrowRight, 
  Check, 
  ThumbsDown, 
  Zap, 
  Clock, 
  ShieldCheck 
} from "lucide-react";

interface RecommendationsListProps {
  recommendations: AIRecommendation[];
  onAction: (id: string, action: "ACCEPTED" | "DISMISSED" | "REVIEWED") => void;
}

export const RecommendationsList: React.FC<RecommendationsListProps> = ({
  recommendations,
  onAction,
}) => {
  const [selectedRec, setSelectedRec] = useState<AIRecommendation | null>(null);

  return (
    <div className="rounded-xl bg-slate-900/90 border border-slate-800 p-5 shadow-lg backdrop-blur-sm">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-4 border-b border-slate-800 gap-2">
        <div>
          <div className="flex items-center space-x-2">
            <div className="p-1.5 rounded bg-amber-950/60 border border-amber-800 text-amber-400">
              <Sparkles className="w-4 h-4" />
            </div>
            <h2 className="text-sm font-semibold text-white uppercase tracking-wider">
              AI Optimization Recommendations
            </h2>
            <Badge label="OPTIMIZATION RECOMMENDATION" variant="recommendation" />
          </div>
          <p className="text-xs text-slate-400 mt-1">
            Actionable advisories balancing comfort envelopes, peak shaving, and energy conservation
          </p>
        </div>
        <span className="text-xs font-mono text-slate-400">
          Pending Review:{" "}
          <strong className="text-amber-400">
            {recommendations.filter((r) => r.status === "PENDING").length}
          </strong>
        </span>
      </div>

      <div className="mt-4 space-y-3">
        {recommendations.length === 0 ? (
          <div className="text-center py-8 text-xs text-slate-500 font-mono">
            No active recommendations at this moment. Building is operating optimally.
          </div>
        ) : (
          recommendations.map((rec) => {
            const isPending = rec.status === "PENDING";
            return (
              <div
                key={rec.id}
                className="group p-4 rounded-xl bg-slate-950/60 border border-slate-800/80 hover:border-slate-700 transition-all flex flex-col md:flex-row md:items-center justify-between gap-4"
              >
                {/* Left details */}
                <div
                  className="flex-1 cursor-pointer"
                  onClick={() => setSelectedRec(rec)}
                >
                  <div className="flex items-center space-x-2">
                    <span
                      className={`text-[9px] font-mono px-2 py-0.5 rounded font-bold uppercase ${
                        rec.priority === "HIGH"
                          ? "bg-rose-500/20 text-rose-300 border border-rose-500/30"
                          : rec.priority === "MEDIUM"
                          ? "bg-amber-500/20 text-amber-300 border border-amber-500/30"
                          : "bg-blue-500/20 text-blue-300 border border-blue-500/30"
                      }`}
                    >
                      {rec.priority}
                    </span>
                    <span className="text-xs font-mono text-slate-500">{rec.zone_name}</span>
                    <span className="text-xs font-mono text-slate-600">•</span>
                    <span className="text-xs font-mono text-emerald-400 font-semibold">
                      +{rec.expected_kw_savings} kW savings
                    </span>
                  </div>

                  <h3 className="text-sm font-semibold text-white mt-1 group-hover:text-emerald-400 transition-colors">
                    {rec.title}
                  </h3>
                  <p className="text-xs text-slate-400 line-clamp-1 mt-0.5">{rec.reason}</p>
                </div>

                {/* Right actions and status */}
                <div className="flex items-center space-x-2 shrink-0">
                  <span
                    className={`font-mono text-[10px] font-bold px-2 py-0.5 rounded ${
                      rec.status === "ACCEPTED"
                        ? "bg-emerald-500/20 text-emerald-300 border border-emerald-500/30"
                        : rec.status === "DISMISSED"
                        ? "bg-slate-800 text-slate-500 border border-slate-700"
                        : rec.status === "REVIEWED"
                        ? "bg-blue-500/20 text-blue-300 border border-blue-500/30"
                        : "bg-amber-500/20 text-amber-300 border border-amber-500/30"
                    }`}
                  >
                    {rec.status}
                  </span>

                  {isPending && (
                    <div className="flex items-center space-x-1">
                      <button
                        title="Accept Recommendation"
                        onClick={(e) => {
                          e.stopPropagation();
                          onAction(rec.id, "ACCEPTED");
                        }}
                        className="p-1.5 rounded-lg bg-emerald-600/30 hover:bg-emerald-600 text-emerald-300 hover:text-white transition-all cursor-pointer"
                      >
                        <Check className="w-3.5 h-3.5" />
                      </button>
                      <button
                        title="Dismiss"
                        onClick={(e) => {
                          e.stopPropagation();
                          onAction(rec.id, "DISMISSED");
                        }}
                        className="p-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-white transition-all cursor-pointer"
                      >
                        <ThumbsDown className="w-3.5 h-3.5" />
                      </button>
                    </div>
                  )}

                  <button
                    onClick={() => setSelectedRec(rec)}
                    className="p-1.5 rounded-lg bg-slate-800 text-slate-400 hover:text-white hover:bg-slate-700 transition-colors cursor-pointer"
                  >
                    <ArrowRight className="w-3.5 h-3.5" />
                  </button>
                </div>
              </div>
            );
          })
        )}
      </div>

      {/* Modal Popup */}
      <RecommendationModal
        recommendation={selectedRec}
        onClose={() => setSelectedRec(null)}
        onAction={onAction}
      />
    </div>
  );
};
