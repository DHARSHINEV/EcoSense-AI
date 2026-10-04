import React from "react";
import "./globals.css";
import { Navbar } from "../components/Navbar";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className="dark">
      <head>
        <title>EcoSense AI – Intelligent Building Energy Optimizer</title>
        <meta
          name="description"
          content="AI-powered building energy optimization balancing efficiency, occupant comfort, and peak-demand management for commercial facilities."
        />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
      </head>
      <body className="min-h-screen bg-slate-950 text-slate-100 antialiased selection:bg-emerald-500/30 selection:text-emerald-300">
        <div className="flex flex-col min-h-screen">
          <Navbar />

          <main className="flex-1">{children}</main>

          <footer className="border-t border-slate-800/80 bg-slate-950 py-8 px-4 sm:px-6 lg:px-8 text-xs text-slate-500">
            <div className="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
              <div className="flex items-center space-x-2">
                <span className="font-semibold text-slate-400">EcoSense AI</span>
                <span>•</span>
                <span>Yuva Yodha Energy Tech Hackathon 2026</span>
                <span>•</span>
                <span className="font-mono text-[10px] text-cyan-400 bg-cyan-950/60 px-2 py-0.5 rounded border border-cyan-800">
                  SIMULATION ACTIVE
                </span>
              </div>
              <p className="text-[11px] text-slate-500 text-center sm:text-right">
                Engineered for Commercial Buildings • SENSE → PREDICT → OPTIMIZE → RECOMMEND → MEASURE
              </p>
            </div>
          </footer>
        </div>
      </body>
    </html>
  );
}
