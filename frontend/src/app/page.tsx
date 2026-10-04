"use client";

import React from "react";
import Link from "next/link";
import { 
  Building2, 
  ArrowRight, 
  Zap, 
  BrainCircuit, 
  ShieldCheck, 
  Sparkles, 
  BarChart3, 
  Sliders, 
  Calculator,
  Layers,
  Thermometer,
  Activity
} from "lucide-react";
import { Badge } from "../components/Badge";

export default function LandingPage() {
  const steps = [
    {
      step: "01",
      name: "SENSE",
      title: "Multi-Zone Telemetry",
      desc: "Granular simulated IoT data for occupancy, temperature, humidity, CO2 air quality, and electrical circuits across 5 building zones.",
      icon: Activity,
    },
    {
      step: "02",
      name: "PREDICT",
      title: "ML Demand Forecasting",
      desc: "Scikit-Learn RandomForestRegressor trained chronologically to forecast next 12-hour building power demand without look-ahead data leakage.",
      icon: BrainCircuit,
    },
    {
      step: "03",
      name: "OPTIMIZE",
      title: "Multi-Objective Balancing",
      desc: "Simultaneously balances energy reduction, strict comfort compliance (22°C–26°C), and automated peak demand shaving.",
      icon: Zap,
    },
    {
      step: "04",
      name: "RECOMMEND",
      title: "Human-in-the-Loop",
      desc: "Actionable advisories with quantified kW savings and comfort verification for facility managers to accept or dismiss.",
      icon: Sparkles,
    },
    {
      step: "05",
      name: "MEASURE",
      title: "Baseline Verification",
      desc: "IPMVP-aligned measurement against conventional fixed-schedule operation, verifying energy, cost, and carbon abatement.",
      icon: ShieldCheck,
    },
  ];

  return (
    <div className="relative overflow-hidden">
      {/* Background Glows */}
      <div className="absolute top-0 left-1/2 -translate-x-1/2 w-full max-w-7xl h-96 bg-gradient-to-b from-emerald-500/10 to-transparent blur-3xl pointer-events-none" />

      {/* Hero Section */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-16 pb-20 sm:pt-24 sm:pb-28">
        <div className="text-center max-w-3xl mx-auto">
          <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-slate-900 border border-emerald-500/30 text-xs font-mono text-emerald-400 mb-6 shadow-sm">
            <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
            <span>Yuva Yodha Energy Tech Hackathon 2026 • Smart Buildings Track</span>
          </div>

          <h1 className="text-4xl sm:text-6xl font-extrabold tracking-tight text-white leading-tight sm:leading-none">
            EcoSense <span className="text-emerald-400">AI</span>
          </h1>

          <p className="mt-4 text-2xl sm:text-3xl font-semibold text-slate-200 tracking-tight">
            “Make Every Square Metre Smarter.”
          </p>

          <p className="mt-4 text-base sm:text-lg text-slate-400 max-w-2xl mx-auto leading-relaxed">
            AI-powered building energy optimization that balances efficiency, occupant comfort, and peak-demand management for commercial facilities.
          </p>

          <div className="mt-8 flex flex-wrap items-center justify-center gap-4">
            <Link
              href="/dashboard"
              className="flex items-center space-x-2 px-6 py-3 rounded-xl bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-bold text-sm transition-all shadow-lg shadow-emerald-500/25 hover:scale-105"
            >
              <span>Launch Dashboard</span>
              <ArrowRight className="w-4 h-4" />
            </Link>

            <Link
              href="/scenarios"
              className="flex items-center space-x-2 px-6 py-3 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 text-white font-semibold text-sm transition-all shadow-md hover:border-slate-600"
            >
              <Zap className="w-4 h-4 text-emerald-400" />
              <span>Explore Scenario Lab</span>
            </Link>

            <Link
              href="/simulation"
              className="flex items-center space-x-2 px-5 py-3 rounded-xl bg-slate-900/60 hover:bg-slate-800 text-slate-300 font-medium text-sm transition-colors border border-slate-800"
            >
              <Sliders className="w-4 h-4 text-cyan-400" />
              <span>Simulation Controls</span>
            </Link>
          </div>
        </div>

        {/* Highlight Stats Banner */}
        <div className="mt-16 max-w-5xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-4 p-6 rounded-2xl bg-slate-900/80 border border-slate-800 backdrop-blur-md">
          <div className="text-center p-3">
            <span className="block text-2xl sm:text-3xl font-bold font-mono text-emerald-400">27.8%</span>
            <span className="text-xs text-slate-400 font-medium mt-1 block">Simulated Energy Reduction</span>
            <div className="mt-1"><Badge label="SIMULATION RESULT" variant="result" size="sm" /></div>
          </div>
          <div className="text-center p-3 border-l border-slate-800">
            <span className="block text-2xl sm:text-3xl font-bold font-mono text-cyan-400">23.2%</span>
            <span className="text-xs text-slate-400 font-medium mt-1 block">Simulated Peak Shaved</span>
            <div className="mt-1"><Badge label="SIMULATION RESULT" variant="result" size="sm" /></div>
          </div>
          <div className="text-center p-3 border-l border-slate-800">
            <span className="block text-2xl sm:text-3xl font-bold font-mono text-purple-400">89.6%</span>
            <span className="text-xs text-slate-400 font-medium mt-1 block">Temperature Comfort Proxy</span>
            <div className="mt-1"><Badge label="22°C - 26°C PROXY" variant="default" size="sm" /></div>
          </div>
          <div className="text-center p-3 border-l border-slate-800">
            <span className="block text-2xl sm:text-3xl font-bold font-mono text-amber-400">4.0 Mos</span>
            <span className="text-xs text-slate-400 font-medium mt-1 block">Simple Payback Period</span>
            <div className="mt-1"><Badge label="ILLUSTRATIVE ESTIMATE" variant="default" size="sm" /></div>
          </div>
        </div>

        {/* Architecture Flow Visualization */}
        <div className="mt-24 max-w-6xl mx-auto">
          <div className="text-center mb-12">
            <h2 className="text-xs font-mono uppercase tracking-widest text-emerald-400 font-bold">
              Engineering Architecture
            </h2>
            <p className="mt-2 text-2xl sm:text-3xl font-bold text-white tracking-tight">
              The Closed-Loop Energy Optimization Paradigm
            </p>
            <p className="mt-2 text-sm text-slate-400 max-w-xl mx-auto">
              How EcoSense AI senses multi-zone telemetry, forecasts electrical load, optimizes equipment, and surfaces human-in-the-loop recommendations.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-5 gap-4">
            {steps.map((st, i) => {
              const Icon = st.icon;
              return (
                <div
                  key={st.step}
                  className="relative rounded-xl bg-slate-900 border border-slate-800 p-5 hover:border-emerald-500/50 transition-all flex flex-col justify-between group"
                >
                  <div>
                    <div className="flex items-center justify-between">
                      <span className="text-xs font-mono font-bold text-emerald-400">
                        {st.step}
                      </span>
                      <div className="p-2 rounded-lg bg-slate-800 text-slate-300 group-hover:text-emerald-400 transition-colors">
                        <Icon className="w-4 h-4" />
                      </div>
                    </div>
                    <span className="text-[10px] font-mono tracking-wider text-slate-500 font-bold block mt-3 uppercase">
                      {st.name}
                    </span>
                    <h3 className="text-sm font-bold text-white mt-0.5">
                      {st.title}
                    </h3>
                    <p className="text-xs text-slate-400 mt-2 leading-relaxed">
                      {st.desc}
                    </p>
                  </div>

                  {i < steps.length - 1 && (
                    <div className="hidden md:block absolute -right-3.5 top-1/2 -translate-y-1/2 z-10 text-slate-600">
                      →
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        </div>

        {/* Feature Grid */}
        <div className="mt-24 max-w-6xl mx-auto">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="p-6 rounded-2xl bg-slate-900/60 border border-slate-800">
              <div className="p-2.5 rounded-xl bg-emerald-500/10 text-emerald-400 w-fit mb-4">
                <Layers className="w-5 h-5" />
              </div>
              <h3 className="text-base font-bold text-white">Multi-Zone Observability</h3>
              <p className="text-xs text-slate-400 mt-2 leading-relaxed">
                Independent thermal and occupancy tracking across Lobby, Office Floor, Meeting Rooms, Conference Rooms, and Cafeteria.
              </p>
            </div>

            <div className="p-6 rounded-2xl bg-slate-900/60 border border-slate-800">
              <div className="p-2.5 rounded-xl bg-purple-500/10 text-purple-400 w-fit mb-4">
                <BrainCircuit className="w-5 h-5" />
              </div>
              <h3 className="text-base font-bold text-white">Scikit-Learn ML Forecaster</h3>
              <p className="text-xs text-slate-400 mt-2 leading-relaxed">
                Trained on chronological 80/20 train-test splits (no look-ahead leakage) with transparent approximate empirical prediction bands.
              </p>
            </div>

            <div className="p-6 rounded-2xl bg-slate-900/60 border border-slate-800">
              <div className="p-2.5 rounded-xl bg-cyan-500/10 text-cyan-400 w-fit mb-4">
                <Calculator className="w-5 h-5" />
              </div>
              <h3 className="text-base font-bold text-white">Phased Retrofit & ROI Model</h3>
              <p className="text-xs text-slate-400 mt-2 leading-relaxed">
                Interactive payback calculator modeling sensor CapEx, software OpEx, and utility tariffs for typical commercial facility sizes.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
