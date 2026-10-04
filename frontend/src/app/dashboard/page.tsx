"use client";

import React, { useEffect, useState } from "react";
import { api } from "../../lib/api";
import { 
  BuildingSummary, 
  HourlyDemandPoint, 
  ZoneBreakdownPoint, 
  ForecastResponse, 
  AIRecommendation, 
  OccupancyCorrelationPoint 
} from "../../lib/types";
import { KpiCard } from "../../components/KpiCard";
import { EnergyAnalyticsChart } from "../../components/EnergyAnalyticsChart";
import { DemandForecastChart } from "../../components/DemandForecastChart";
import { OccupancyCorrelationChart } from "../../components/OccupancyCorrelationChart";
import { RecommendationsList } from "../../components/RecommendationsList";
import { ComfortComplianceCard } from "../../components/ComfortComplianceCard";
import { Badge } from "../../components/Badge";
import { 
  Zap, 
  TrendingDown, 
  Activity, 
  Users, 
  ShieldCheck, 
  RefreshCw, 
  SlidersHorizontal,
  Leaf
} from "lucide-react";

export default function DashboardPage() {
  const [summary, setSummary] = useState<BuildingSummary | null>(null);
  const [hourlyDemand, setHourlyDemand] = useState<HourlyDemandPoint[]>([]);
  const [zoneBreakdown, setZoneBreakdown] = useState<ZoneBreakdownPoint[]>([]);
  const [forecast, setForecast] = useState<ForecastResponse | null>(null);
  const [recommendations, setRecommendations] = useState<AIRecommendation[]>([]);
  const [occupancyScatter, setOccupancyScatter] = useState<OccupancyCorrelationPoint[]>([]);
  const [loading, setLoading] = useState(true);
  const [refreshing, setRefreshing] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const loadDashboardData = async () => {
    try {
      setError(null);
      const [sumRes, energyRes, forecastRes, recsRes, occRes] = await Promise.all([
        api.getSummary(),
        api.getEnergy(),
        api.getForecast(),
        api.getRecommendations(),
        api.getOccupancy(),
      ]);

      setSummary(sumRes);
      setHourlyDemand(energyRes.hourly_demand);
      setZoneBreakdown(energyRes.zone_breakdown);
      setForecast(forecastRes);
      setRecommendations(recsRes.recommendations);
      setOccupancyScatter(occRes.occupancy_energy_correlation);
    } catch (err: any) {
      console.error("Dashboard data load error:", err);
      setError("Unable to connect to EcoSense AI backend. Please verify FastAPI service is running on port 8000.");
    } finally {
      setLoading(false);
      setRefreshing(false);
    }
  };

  useEffect(() => {
    loadDashboardData();
  }, []);

  const handleRecommendationAction = async (id: string, action: "ACCEPTED" | "DISMISSED" | "REVIEWED") => {
    try {
      await api.updateRecommendationAction(id, action);
      // Optimistically update local state
      setRecommendations((prev) =>
        prev.map((r) => (r.id === id ? { ...r, status: action } : r))
      );
    } catch (err) {
      console.error("Failed to update recommendation:", err);
    }
  };

  const handleRefresh = () => {
    setRefreshing(true);
    loadDashboardData();
  };

  if (loading) {
    return (
      <div className="min-h-[70vh] flex flex-col items-center justify-center space-y-4">
        <RefreshCw className="w-8 h-8 text-emerald-400 animate-spin" />
        <p className="text-sm font-mono text-slate-400">Loading EcoSense AI Facility Telemetry...</p>
      </div>
    );
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      {/* Top Header & Refresh Control */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-6 border-b border-slate-800 gap-4">
        <div>
          <div className="flex items-center space-x-3">
            <h1 className="text-2xl font-bold text-white tracking-tight">Facility Energy Cockpit</h1>
            <Badge label="SIMULATION ACTIVE" variant="simulated" />
          </div>
          <p className="text-xs text-slate-400 mt-1">
            Real-time multi-zone monitoring, Scikit-Learn ML demand prediction, and automated setback optimization
          </p>
        </div>

        <div className="flex items-center space-x-3">
          <div className="text-right text-xs font-mono hidden sm:block">
            <span className="text-slate-500 block">Tariff Assumption</span>
            <span className="text-slate-300 font-semibold">₹{summary?.electricity_tariff || 8.50}/kWh</span>
          </div>

          <button
            onClick={handleRefresh}
            disabled={refreshing}
            className="flex items-center space-x-2 px-3.5 py-2 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-700 text-xs font-semibold text-slate-300 transition-colors cursor-pointer"
          >
            <RefreshCw className={`w-3.5 h-3.5 ${refreshing ? "animate-spin text-emerald-400" : ""}`} />
            <span>Refresh Telemetry</span>
          </button>
        </div>
      </div>

      {error && (
        <div className="p-4 rounded-xl bg-rose-950/60 border border-rose-800 text-xs text-rose-300">
          {error}
        </div>
      )}

      {/* TOP KPI CARDS */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4">
        <KpiCard
          title="Current Power Load"
          value={summary?.current_total_power_kw || 0}
          unit="kW"
          baselineValue={`${summary?.current_baseline_power_kw || 0} kW`}
          change={`-${summary?.current_savings_kw || 0} kW`}
          changeType="positive"
          badgeLabel="SIMULATED DATA"
          badgeVariant="simulated"
          icon={Zap}
        />

        <KpiCard
          title="Energy Saved (30d)"
          value={summary ? Math.round(summary.total_energy_saved_kwh).toLocaleString() : "0"}
          unit="kWh"
          baselineValue={`${summary ? Math.round(summary.total_baseline_energy_kwh).toLocaleString() : 0} kWh`}
          change={`-${summary?.energy_reduction_pct || 0}%`}
          changeType="positive"
          badgeLabel="SIMULATION RESULT"
          badgeVariant="result"
          icon={TrendingDown}
        />

        <KpiCard
          title="Peak Demand Shaved"
          value={summary?.optimized_peak_kw || 0}
          unit="kW"
          baselineValue={`${summary?.baseline_peak_kw || 0} kW`}
          change={`-${summary?.peak_reduction_pct || 0}%`}
          changeType="positive"
          badgeLabel="SIMULATION RESULT"
          badgeVariant="result"
          icon={Activity}
        />

        <KpiCard
          title="Occupancy Decoupling"
          value={summary?.current_occupancy || 0}
          unit="persons"
          badgeLabel="SIMULATED DATA"
          badgeVariant="simulated"
          icon={Users}
          subtext="Dynamic Setback Engaged"
        />

        <KpiCard
          title="Comfort Compliance"
          value={`${summary?.comfort_compliance_pct || 98.6}%`}
          badgeLabel="22°C-26°C PROXY"
          badgeVariant="default"
          icon={ShieldCheck}
          subtext="Simplified Comfort Proxy"
        />
      </div>

      {/* Financial & Environmental Impact Banner */}
      {summary && (
        <div className="p-4 rounded-xl bg-gradient-to-r from-emerald-950/40 via-slate-900 to-teal-950/40 border border-emerald-900/50 flex flex-wrap items-center justify-between gap-4 text-xs">
          <div className="flex items-center space-x-2.5">
            <div className="p-2 rounded-lg bg-emerald-500/20 text-emerald-400">
              <Leaf className="w-4 h-4" />
            </div>
            <div>
              <span className="text-slate-400 block">Simulated 30-Day Cost Avoidance:</span>
              <span className="text-base font-bold font-mono text-emerald-400">
                ₹{Math.round(summary.cost_savings_inr).toLocaleString()} avoided
              </span>
            </div>
          </div>

          <div className="text-slate-400 font-mono">
            <span>Simulated Grid CO₂ Abatement: </span>
            <strong className="text-cyan-300">
              {Math.round(summary.co2_reduction_kg).toLocaleString()} kg CO₂
            </strong>{" "}
            (CEA Factor: 0.82 kg/kWh)
          </div>

          <div>
            <Badge label="SIMULATION RESULT" variant="result" size="sm" />
          </div>
        </div>
      )}

      {/* ENERGY ANALYTICS: Dual Charts */}
      <EnergyAnalyticsChart hourlyData={hourlyDemand} zoneData={zoneBreakdown} />

      {/* ML DEMAND FORECAST & OCCUPANCY CORRELATION */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {forecast && <DemandForecastChart forecastData={forecast} />}
        <OccupancyCorrelationChart scatterPoints={occupancyScatter} />
      </div>

      {/* AI RECOMMENDATIONS & COMFORT COMPLIANCE */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2">
          <RecommendationsList
            recommendations={recommendations}
            onAction={handleRecommendationAction}
          />
        </div>

        <div>
          <ComfortComplianceCard
            compliancePct={summary?.comfort_compliance_pct || 98.6}
            totalViolations={summary?.total_comfort_violations || 0}
            comfortRange={summary?.comfort_range || "22.0°C - 26.0°C"}
            currentTemp={24.2}
          />
        </div>
      </div>
    </div>
  );
}
