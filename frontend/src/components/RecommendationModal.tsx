"use client";

import React from "react";
import { AIRecommendation } from "../lib/types";
import { Badge } from "./Badge";
import { X, Check, Eye, ThumbsDown, ShieldAlert, Sparkles, TrendingDown, Thermometer } from "lucide-react";

interface RecommendationModalProps {
  recommendation: AIRecommendation | null;
  onClose: () => void;
  onAction: (id: string, action: "ACCEPTED" | "DISMISSED" | "REVIEWED") => void;
}

export const RecommendationModal: React.FC<RecommendationModalProps> = ({
  recommendation,
  onClose,
  onAction,
}) => {
  if (!recommendation) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-sm animate-in fade-in duration-200">
      <div className="w-full max-w-lg rounded-2xl bg-slate-900 border border-slate-700 p-6 shadow-2xl relative">
        {/* Close Button */}
        <button
          onClick={onClose}
          className="absolute top-4 right-4 p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors"
        >
          <X className="w-5 h-5" />
        </button>

        {/* Header */}
        <div className="flex items-center space-x-2">
          <span className="font-mono text-xs text-slate-500 font-semibold">{recommendation.id}</span>
          <Badge label="OPTIMIZATION RECOMMENDATION" variant="recommendation" />
          <span
            className={`text-[10px] font-mono px-2 py-0.5 rounded font-bold uppercase ${
              recommendation.priority === "HIGH"
                ? "bg-rose-500/20 text-rose-300 border border-rose-500/30"
                : recommendation.priority === "MEDIUM"
                ? "bg-amber-500/20 text-amber-300 border border-amber-500/30"
                : "bg-blue-500/20 text-blue-300 border border-blue-500/30"
            }`}
          >
            {recommendation.priority} Priority
          </span>
        </div>

        <h3 className="mt-3 text-lg font-bold text-white tracking-tight">
          {recommendation.title}
        </h3>

        <div className="mt-2 flex items-center space-x-4 text-xs text-slate-400 font-mono">
          <span>Target Zone: <strong className="text-slate-200">{recommendation.zone_name}</strong></span>
          <span>Action: <strong className="text-emerald-400">{recommendation.action_type}</strong></span>
        </div>

        {/* Reason Box */}
        <div className="mt-4 p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 leading-relaxed">
          <div className="flex items-start space-x-2">
            <Sparkles className="w-4 h-4 text-amber-400 shrink-0 mt-0.5" />
            <div>
              <strong className="text-amber-300 block mb-1">Diagnostic Reason:</strong>
              {recommendation.reason}
            </div>
          </div>
        </div>

        {/* Quantitative Impact Grid */}
        <div className="mt-4 grid grid-cols-2 gap-3 text-xs">
          <div className="p-3 rounded-xl bg-slate-800/60 border border-slate-700/60">
            <div className="flex items-center space-x-1.5 text-emerald-400 font-semibold mb-1">
              <TrendingDown className="w-3.5 h-3.5" />
              <span>Energy & Cost Savings</span>
            </div>
            <p className="font-mono text-base font-bold text-white">
              {recommendation.expected_kw_savings} kW
            </p>
            <p className="text-[11px] text-slate-400">
              ₹{recommendation.expected_cost_savings_inr} / hour avoided
            </p>
          </div>

          <div className="p-3 rounded-xl bg-slate-800/60 border border-slate-700/60">
            <div className="flex items-center space-x-1.5 text-blue-400 font-semibold mb-1">
              <Thermometer className="w-3.5 h-3.5" />
              <span>Comfort Safeguard</span>
            </div>
            <p className="text-[11px] text-slate-300">
              {recommendation.comfort_impact}
            </p>
          </div>
        </div>

        <div className="mt-3 p-3 rounded-xl bg-slate-800/40 border border-slate-800 text-xs text-slate-400">
          <strong className="text-slate-300 block mb-0.5">Peak Demand Management:</strong>
          {recommendation.peak_demand_impact}
        </div>

        {/* Status display */}
        <div className="mt-4 flex items-center justify-between border-t border-slate-800 pt-4 text-xs font-mono">
          <span className="text-slate-400">
            Current Status:{" "}
            <span
              className={`font-bold px-2 py-0.5 rounded ${
                recommendation.status === "ACCEPTED"
                  ? "bg-emerald-500/20 text-emerald-300"
                  : recommendation.status === "DISMISSED"
                  ? "bg-slate-700 text-slate-400"
                  : recommendation.status === "REVIEWED"
                  ? "bg-blue-500/20 text-blue-300"
                  : "bg-amber-500/20 text-amber-300"
              }`}
            >
              {recommendation.status}
            </span>
          </span>

          <span className="text-slate-500">Human-in-the-Loop Governance</span>
        </div>

        {/* Action Buttons for Facility Manager */}
        <div className="mt-5 flex items-center justify-end space-x-2">
          <button
            onClick={() => {
              onAction(recommendation.id, "DISMISSED");
              onClose();
            }}
            className="flex items-center space-x-1.5 px-3 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold transition-colors cursor-pointer"
          >
            <ThumbsDown className="w-3.5 h-3.5" />
            <span>Dismiss</span>
          </button>

          <button
            onClick={() => {
              onAction(recommendation.id, "REVIEWED");
              onClose();
            }}
            className="flex items-center space-x-1.5 px-3 py-2 rounded-lg bg-blue-900/40 hover:bg-blue-800/60 border border-blue-700 text-blue-300 text-xs font-semibold transition-colors cursor-pointer"
          >
            <Eye className="w-3.5 h-3.5" />
            <span>Mark Reviewed</span>
          </button>

          <button
            onClick={() => {
              onAction(recommendation.id, "ACCEPTED");
              onClose();
            }}
            className="flex items-center space-x-1.5 px-4 py-2 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold transition-all shadow-md shadow-emerald-900/30 cursor-pointer"
          >
            <Check className="w-4 h-4" />
            <span>Accept Recommendation</span>
          </button>
        </div>
      </div>
    </div>
  );
};
