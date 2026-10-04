"use client";

import React, { useState } from "react";
import { api } from "../../lib/api";
import { PaybackOutput } from "../../lib/types";
import { Badge } from "../../components/Badge";
import { 
  Calculator, 
  Layers, 
  ArrowRight, 
  Clock, 
  CheckCircle2, 
  TrendingUp, 
  AlertCircle,
  Building,
  GraduationCap,
  ShoppingBag,
  Briefcase
} from "lucide-react";

export default function DeploymentPage() {
  // Configurable Calculator Inputs
  const [area, setArea] = useState<number>(5000); // sq.m
  const [zonesCount, setZonesCount] = useState<number>(5);
  const [sensorsCount, setSensorsCount] = useState<number>(25);
  const [sensorCost, setSensorCost] = useState<number>(125000); // ₹5,000 / unit
  const [installCost, setInstallCost] = useState<number>(75000);
  const [softwareCost, setSoftwareCost] = useState<number>(180000); // ₹15k/mo
  const [annualBill, setAnnualBill] = useState<number>(4200000);
  const [savingsPct, setSavingsPct] = useState<number>(18.5);

  const [output, setOutput] = useState<PaybackOutput>({
    label: "Illustrative deployment estimate",
    upfront_capex_inr: 200000,
    annual_opex_inr: 180000,
    estimated_annual_savings_inr: 777000,
    net_annual_benefit_inr: 597000,
    simple_payback_years: 0.33,
    five_year_net_savings_inr: 2785000,
    five_year_roi_pct: 1392.5,
  });

  const handleRecalculate = async () => {
    try {
      const res = await api.calculatePayback({
        building_area_sqm: Number(area),
        number_of_zones: Number(zonesCount),
        sensor_count: Number(sensorsCount),
        estimated_sensor_cost_inr: Number(sensorCost),
        estimated_installation_inr: Number(installCost),
        software_annual_subscription_inr: Number(softwareCost),
        annual_energy_bill_inr: Number(annualBill),
        expected_savings_pct: Number(savingsPct),
      });
      setOutput(res);
    } catch (err) {
      console.error("Recalculate error:", err);
    }
  };

  const phases = [
    {
      phase: "Phase 1: Software Analytics & Virtual Auditing",
      time: "Months 1–2",
      capex: "₹0 CapEx",
      desc: "Ingest utility smart meter interval data and available BMS logs. Train baseline regression model and identify nighttime scheduling drifts.",
    },
    {
      phase: "Phase 2: Low-Cost IoT Sensing Overlay",
      time: "Months 3–4",
      capex: "Low CapEx",
      desc: "Deploy battery-operated wireless LoRaWAN / Zigbee multi-sensors (PIR occupancy, temperature, humidity, CO2) without pulling wires.",
    },
    {
      phase: "Phase 3: BMS & Smart Thermostat Integration",
      time: "Months 5–6",
      capex: "Standard Gateway",
      desc: "Install BACnet IP / Modbus IoT gateways to dynamically modulate chiller setpoints and lighting relays with human-in-the-loop overrides.",
    },
    {
      phase: "Phase 4: Grid-Interactive Demand Response (GEB)",
      time: "Months 7+",
      capex: "Software Upgrade",
      desc: "Connect to utility OpenADR signals for automated peak shaving and pre-cooling, monetizing flexible load capacity.",
    },
  ];

  const archetypes = [
    {
      name: "IT & Corporate Parks",
      fit: "Very High Fit",
      icon: Briefcase,
      desc: "Large variable occupancy due to hybrid work; significant cooling savings in meeting suites and cafeteria wings.",
    },
    {
      name: "Educational Campuses",
      fit: "High Fit",
      icon: GraduationCap,
      desc: "Classrooms and lecture halls sitting unoccupied for hours between lectures while AC remains active.",
    },
    {
      name: "Retail & Malls",
      fit: "High Fit",
      icon: ShoppingBag,
      desc: "Footfall variations from morning to evening; high potential for pre-cooling and ambient-responsive chiller modulation.",
    },
    {
      name: "Commercial Facilities",
      fit: "Medium to High Fit",
      icon: Building,
      desc: "Branch offices and coworking hubs with decentralized VRF systems seeking automated setback.",
    },
  ];

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-10">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-6 border-b border-slate-800 gap-4">
        <div>
          <div className="flex items-center space-x-3">
            <h1 className="text-2xl font-bold text-white tracking-tight">Deployment & Economics Model</h1>
            <Badge label="ILLUSTRATIVE DEPLOYMENT ESTIMATE" variant="default" />
          </div>
          <p className="text-xs text-slate-400 mt-1">
            Phased 4-stage non-intrusive retrofit framework and configurable payback economics
          </p>
        </div>
      </div>

      {/* CALCULATOR SECTION */}
      <div className="rounded-2xl bg-slate-900/90 border border-slate-800 p-6 shadow-xl backdrop-blur-sm">
        <div className="flex flex-col md:flex-row md:items-center justify-between pb-4 border-b border-slate-800 gap-2">
          <div>
            <div className="flex items-center space-x-2">
              <Calculator className="w-5 h-5 text-emerald-400" />
              <h2 className="text-base font-bold text-white">Interactive Payback & ROI Calculator</h2>
            </div>
            <p className="text-xs text-slate-400 mt-0.5">
              Input your facility parameters to calculate capital expenditure, payback period, and 5-year returns
            </p>
          </div>
          <Badge label="Illustrative deployment estimate" variant="default" size="sm" />
        </div>

        {/* Inputs Grid */}
        <div className="mt-6 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 text-xs">
          <div className="space-y-1.5">
            <label className="text-slate-400 font-medium">Conditioned Area (sq.m)</label>
            <input
              type="number"
              value={area}
              onChange={(e) => setArea(Number(e.target.value))}
              className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2 font-mono text-white"
            />
          </div>

          <div className="space-y-1.5">
            <label className="text-slate-400 font-medium">Number of Zones</label>
            <input
              type="number"
              value={zonesCount}
              onChange={(e) => setZonesCount(Number(e.target.value))}
              className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2 font-mono text-white"
            />
          </div>

          <div className="space-y-1.5">
            <label className="text-slate-400 font-medium">Wireless Sensor Count</label>
            <input
              type="number"
              value={sensorsCount}
              onChange={(e) => {
                const count = Number(e.target.value);
                setSensorsCount(count);
                setSensorCost(count * 5000);
              }}
              className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2 font-mono text-white"
            />
          </div>

          <div className="space-y-1.5">
            <label className="text-slate-400 font-medium">Annual Electricity Bill (₹)</label>
            <input
              type="number"
              value={annualBill}
              onChange={(e) => setAnnualBill(Number(e.target.value))}
              className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2 font-mono text-white"
            />
          </div>

          <div className="space-y-1.5">
            <label className="text-slate-400 font-medium">Sensor Hardware CapEx (₹)</label>
            <input
              type="number"
              value={sensorCost}
              onChange={(e) => setSensorCost(Number(e.target.value))}
              className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2 font-mono text-white"
            />
          </div>

          <div className="space-y-1.5">
            <label className="text-slate-400 font-medium">Gateway & Install (₹)</label>
            <input
              type="number"
              value={installCost}
              onChange={(e) => setInstallCost(Number(e.target.value))}
              className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2 font-mono text-white"
            />
          </div>

          <div className="space-y-1.5">
            <label className="text-slate-400 font-medium">Annual SaaS Software (₹)</label>
            <input
              type="number"
              value={softwareCost}
              onChange={(e) => setSoftwareCost(Number(e.target.value))}
              className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2 font-mono text-white"
            />
          </div>

          <div className="space-y-1.5">
            <label className="text-slate-400 font-medium">Simulated Savings (%)</label>
            <input
              type="number"
              step="0.5"
              value={savingsPct}
              onChange={(e) => setSavingsPct(Number(e.target.value))}
              className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2 font-mono text-emerald-400 font-bold"
            />
          </div>
        </div>

        <div className="mt-4 flex justify-end">
          <button
            onClick={handleRecalculate}
            className="px-5 py-2 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition-colors cursor-pointer"
          >
            Update Economics
          </button>
        </div>

        {/* Output Metrics */}
        <div className="mt-6 p-6 rounded-xl bg-slate-950 border border-slate-800/80 grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3 text-xs font-mono">
          <div className="p-3 rounded-lg bg-slate-900 border border-slate-800">
            <span className="text-slate-500 block text-[11px]">Upfront CapEx:</span>
            <span className="text-lg font-bold text-white">
              ₹{output.upfront_capex_inr.toLocaleString()}
            </span>
            <span className="text-[10px] text-slate-500 block">Sensors + Install</span>
          </div>

          <div className="p-3 rounded-lg bg-slate-900 border border-slate-800">
            <span className="text-slate-500 block text-[11px]">Gross Annual Savings:</span>
            <span className="text-lg font-bold text-emerald-400">
              ₹{Math.round(output.estimated_annual_savings_inr).toLocaleString()}
            </span>
            <span className="text-[10px] text-slate-500 block">{savingsPct}% of bill</span>
          </div>

          <div className="p-3 rounded-lg bg-slate-900 border border-slate-800">
            <span className="text-slate-500 block text-[11px]">Annual Software OpEx:</span>
            <span className="text-lg font-bold text-slate-300">
              ₹{Math.round(output.annual_opex_inr).toLocaleString()}
            </span>
            <span className="text-[10px] text-slate-500 block">SaaS Platform</span>
          </div>

          <div className="p-3 rounded-lg bg-slate-900 border border-slate-800">
            <span className="text-slate-500 block text-[11px]">Net Annual Benefit:</span>
            <span className="text-lg font-bold text-emerald-400">
              ₹{Math.round(output.net_annual_benefit_inr).toLocaleString()}
            </span>
            <span className="text-[10px] text-slate-500 block">Savings - OpEx</span>
          </div>

          <div className="p-3 rounded-lg bg-slate-900 border border-slate-800">
            <span className="text-slate-500 block text-[11px]">Simple Payback:</span>
            <span className="text-lg font-bold text-cyan-300">
              {Math.round(output.simple_payback_years * 12)} Months
            </span>
            <span className="text-[10px] text-slate-500 block">({output.simple_payback_years} years)</span>
          </div>

          <div className="p-3 rounded-lg bg-slate-900 border border-slate-800">
            <span className="text-slate-500 block text-[11px]">5-Year Net ROI:</span>
            <span className="text-lg font-bold text-purple-300">
              {output.five_year_roi_pct}%
            </span>
            <span className="text-[10px] text-slate-500 block">₹{Math.round(output.five_year_net_savings_inr).toLocaleString()} net</span>
          </div>
        </div>

        <div className="mt-4 p-3 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-400 font-mono">
          <strong className="text-slate-300">Notice:</strong> This model provides an <em>Illustrative deployment estimate</em> based on user-entered parameters (CapEx ₹{output.upfront_capex_inr.toLocaleString()}, OpEx ₹{output.annual_opex_inr.toLocaleString()}/yr, simulated savings {savingsPct}%). It does not represent an actual quotation, vendor contract, or guaranteed performance.
        </div>
      </div>

      {/* PHASED DEPLOYMENT ROADMAP */}
      <div>
        <div className="mb-6">
          <h2 className="text-base font-bold text-white uppercase tracking-wider">
            Phased 4-Stage Retrofit Roadmap
          </h2>
          <p className="text-xs text-slate-400 mt-1">
            Engineered to eliminate capital risk through virtual software auditing before hardware deployment
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
          {phases.map((p, i) => (
            <div
              key={p.phase}
              className="p-5 rounded-2xl bg-slate-900/80 border border-slate-800 flex flex-col justify-between"
            >
              <div>
                <div className="flex items-center justify-between text-xs font-mono mb-2">
                  <span className="text-emerald-400 font-bold">{p.time}</span>
                  <span className="text-slate-500">{p.capex}</span>
                </div>
                <h3 className="text-sm font-bold text-white">{p.phase}</h3>
                <p className="text-xs text-slate-400 mt-2 leading-relaxed">{p.desc}</p>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* TARGET ARCHETYPES */}
      <div>
        <div className="mb-6">
          <h2 className="text-base font-bold text-white uppercase tracking-wider">
            Target Commercial Building Archetypes
          </h2>
          <p className="text-xs text-slate-400 mt-1">
            High-waste facility types where occupancy unpredictability creates maximum ROI
          </p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          {archetypes.map((a) => {
            const Icon = a.icon;
            return (
              <div
                key={a.name}
                className="p-5 rounded-2xl bg-slate-900/80 border border-slate-800 flex flex-col justify-between"
              >
                <div>
                  <div className="flex items-center justify-between mb-3">
                    <div className="p-2 rounded-lg bg-slate-800 text-emerald-400">
                      <Icon className="w-5 h-5" />
                    </div>
                    <span className="font-mono text-[10px] px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 font-bold">
                      {a.fit}
                    </span>
                  </div>
                  <h3 className="text-sm font-bold text-white">{a.name}</h3>
                  <p className="text-xs text-slate-400 mt-2 leading-relaxed">{a.desc}</p>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}
