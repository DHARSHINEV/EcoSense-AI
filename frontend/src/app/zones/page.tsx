"use client";

import React, { useEffect, useState } from "react";
import { api } from "../../lib/api";
import { ZoneItem, ZoneReading } from "../../lib/types";
import { Badge } from "../../components/Badge";
import {
  ResponsiveContainer,
  AreaChart,
  Area,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  Legend,
} from "recharts";
import { 
  Layers, 
  Users, 
  Thermometer, 
  Droplets, 
  Wind, 
  Zap, 
  ShieldCheck, 
  AlertCircle 
} from "lucide-react";

export default function ZonesPage() {
  const [zones, setZones] = useState<ZoneItem[]>([]);
  const [selectedZoneId, setSelectedZoneId] = useState<string>("");
  const [zoneReadings, setZoneReadings] = useState<ZoneReading[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchZoneData = async () => {
      try {
        const res = await api.getZones();
        setZones(res.zones);
        if (res.zones.length > 0) {
          const firstId = res.zones[0].zone_id;
          setSelectedZoneId(firstId);
          const detailRes = await api.getZoneDetail(firstId);
          setZoneReadings(detailRes.readings);
        }
      } catch (err) {
        console.error("Failed to load zone details:", err);
      } finally {
        setLoading(false);
      }
    };
    fetchZoneData();
  }, []);

  const handleSelectZone = async (zoneId: string) => {
    setSelectedZoneId(zoneId);
    try {
      const detailRes = await api.getZoneDetail(zoneId);
      setZoneReadings(detailRes.readings);
    } catch (err) {
      console.error("Failed to load zone detail:", err);
    }
  };

  const selectedZone = zones.find((z) => z.zone_id === selectedZoneId) || zones[0];

  const chartData = zoneReadings.map((r) => ({
    time: `${r.hour}:00`,
    hvac: r.hvac_power_kw,
    lighting: r.lighting_power_kw,
    plug: r.plug_load_kw,
    total: r.total_power_kw,
    baseline: r.baseline_total_power_kw,
    temp: r.zone_temp,
    occupancy: r.occupancy,
  }));

  if (loading) {
    return (
      <div className="min-h-[70vh] flex items-center justify-center font-mono text-xs text-slate-400">
        Loading Zone Spatial Observability...
      </div>
    );
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-6 border-b border-slate-800 gap-4">
        <div>
          <div className="flex items-center space-x-3">
            <h1 className="text-2xl font-bold text-white tracking-tight">Zone Observability & Sub-Metering</h1>
            <Badge label="SIMULATED DATA" variant="simulated" />
          </div>
          <p className="text-xs text-slate-400 mt-1">
            Granular thermal comfort, Indoor Air Quality (CO₂), and end-use power circuits (HVAC, Lighting, Plugs)
          </p>
        </div>
      </div>

      {/* Zone Selector Tabs */}
      <div className="flex flex-wrap gap-2">
        {zones.map((z) => {
          const isSelected = z.zone_id === selectedZoneId;
          return (
            <button
              key={z.zone_id}
              onClick={() => handleSelectZone(z.zone_id)}
              className={`flex items-center space-x-2 px-4 py-2.5 rounded-xl text-xs font-semibold transition-all cursor-pointer ${
                isSelected
                  ? "bg-emerald-600 text-white shadow-lg shadow-emerald-900/30 border border-emerald-500"
                  : "bg-slate-900 text-slate-300 hover:bg-slate-800 border border-slate-800"
              }`}
            >
              <Layers className="w-3.5 h-3.5" />
              <span>{z.name}</span>
              <span className="font-mono text-[10px] px-1.5 py-0.5 rounded bg-black/30">
                {z.current_occupancy} occ
              </span>
            </button>
          );
        })}
      </div>

      {selectedZone && (
        <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-4">
          <div className="p-4 rounded-xl bg-slate-900/80 border border-slate-800">
            <div className="flex items-center space-x-2 text-slate-400 text-xs mb-1">
              <Users className="w-3.5 h-3.5 text-cyan-400" />
              <span>Occupancy</span>
            </div>
            <span className="text-xl font-bold font-mono text-white">
              {selectedZone.current_occupancy}{" "}
              <span className="text-xs text-slate-500 font-normal">/ {selectedZone.design_occupancy}</span>
            </span>
          </div>

          <div className="p-4 rounded-xl bg-slate-900/80 border border-slate-800">
            <div className="flex items-center space-x-2 text-slate-400 text-xs mb-1">
              <Thermometer className="w-3.5 h-3.5 text-emerald-400" />
              <span>Temperature</span>
            </div>
            <span className="text-xl font-bold font-mono text-white">
              {selectedZone.current_temp}°C
            </span>
          </div>

          <div className="p-4 rounded-xl bg-slate-900/80 border border-slate-800">
            <div className="flex items-center space-x-2 text-slate-400 text-xs mb-1">
              <Droplets className="w-3.5 h-3.5 text-blue-400" />
              <span>Relative Humidity</span>
            </div>
            <span className="text-xl font-bold font-mono text-white">
              {selectedZone.current_humidity}%
            </span>
          </div>

          <div className="p-4 rounded-xl bg-slate-900/80 border border-slate-800">
            <div className="flex items-center space-x-2 text-slate-400 text-xs mb-1">
              <Wind className="w-3.5 h-3.5 text-purple-400" />
              <span>IAQ (CO₂ Proxy)</span>
            </div>
            <span className="text-xl font-bold font-mono text-white">
              {selectedZone.iaq_score}{" "}
              <span className="text-xs text-slate-500 font-normal">ppm</span>
            </span>
          </div>

          <div className="p-4 rounded-xl bg-slate-900/80 border border-slate-800">
            <div className="flex items-center space-x-2 text-slate-400 text-xs mb-1">
              <Zap className="w-3.5 h-3.5 text-amber-400" />
              <span>Current Power</span>
            </div>
            <span className="text-xl font-bold font-mono text-white">
              {selectedZone.opt_total_power_kw}{" "}
              <span className="text-xs text-slate-500 font-normal">kW</span>
            </span>
          </div>

          <div className="p-4 rounded-xl bg-slate-900/80 border border-slate-800">
            <div className="flex items-center space-x-2 text-slate-400 text-xs mb-1">
              <ShieldCheck className="w-3.5 h-3.5 text-emerald-400" />
              <span>Comfort Status</span>
            </div>
            <span className="text-sm font-bold font-mono text-emerald-400">
              {selectedZone.comfort_score}/100 Ideal
            </span>
          </div>
        </div>
      )}

      {/* 24-Hour Time-Series: Circuit End-Use Breakdown */}
      <div className="rounded-xl bg-slate-900/90 border border-slate-800 p-5 shadow-lg backdrop-blur-sm">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-4 border-b border-slate-800 gap-2">
          <div>
            <div className="flex items-center space-x-2">
              <h2 className="text-sm font-semibold text-white uppercase tracking-wider">
                {selectedZone?.name} – 24-Hour Circuit Sub-Meter Profile
              </h2>
              <Badge label="SIMULATED DATA" variant="simulated" />
            </div>
            <p className="text-xs text-slate-400 mt-1">
              Stacked breakdown of HVAC, Lighting, and Plug loads vs. Unmanaged Fixed Baseline
            </p>
          </div>

          <div className="flex items-center space-x-4 text-xs font-mono">
            <span className="flex items-center space-x-1 text-slate-400">
              <span className="w-2.5 h-2.5 rounded-full bg-slate-500 inline-block" />
              <span>Fixed Baseline</span>
            </span>
            <span className="flex items-center space-x-1 text-emerald-400">
              <span className="w-2.5 h-2.5 rounded-full bg-emerald-500 inline-block" />
              <span>Total EcoSense</span>
            </span>
          </div>
        </div>

        <div className="h-80 mt-4">
          <ResponsiveContainer width="100%" height="100%">
            <AreaChart data={chartData} margin={{ top: 10, right: 20, left: -10, bottom: 0 }}>
              <defs>
                <linearGradient id="hvacGrad" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#059669" stopOpacity={0.7} />
                  <stop offset="95%" stopColor="#059669" stopOpacity={0.1} />
                </linearGradient>
                <linearGradient id="lightingGrad" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#eab308" stopOpacity={0.7} />
                  <stop offset="95%" stopColor="#eab308" stopOpacity={0.1} />
                </linearGradient>
                <linearGradient id="plugGrad" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#3b82f6" stopOpacity={0.7} />
                  <stop offset="95%" stopColor="#3b82f6" stopOpacity={0.1} />
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
              <Area
                type="monotone"
                dataKey="hvac"
                name="HVAC (kW)"
                stackId="1"
                stroke="#059669"
                fill="url(#hvacGrad)"
              />
              <Area
                type="monotone"
                dataKey="lighting"
                name="Lighting (kW)"
                stackId="1"
                stroke="#eab308"
                fill="url(#lightingGrad)"
              />
              <Area
                type="monotone"
                dataKey="plug"
                name="Plug Loads (kW)"
                stackId="1"
                stroke="#3b82f6"
                fill="url(#plugGrad)"
              />
              <Line
                type="monotone"
                dataKey="baseline"
                name="Baseline Fixed Load (kW)"
                stroke="#94a3b8"
                strokeWidth={2}
                strokeDasharray="4 4"
                dot={false}
              />
            </AreaChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
}
