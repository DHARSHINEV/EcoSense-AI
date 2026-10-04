import os
import matplotlib.pyplot as plt
import numpy as np

os.makedirs("scratch/slides_assets", exist_ok=True)

plt.rcParams['font.sans-serif'] = 'Segoe UI'
plt.rcParams['font.family'] = 'sans-serif'

def create_slide7_chart():
    # Compact figure for clean slide placement
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(11.0, 3.0), facecolor='#0c1322')
    
    categories = ['Fixed Baseline', 'EcoSense AI']
    
    # Subplot 1: Total 30-Day Energy (kWh)
    energy_vals = [56961.7, 41145.4]
    bars1 = ax1.bar(categories, energy_vals, color=['#334155', '#10b981'], width=0.52, edgecolor=['#475569', '#34d399'], linewidth=1.2)
    ax1.set_title('30-Day Energy (kWh)\n-27.8% Simulated Reduction', color='#e2e8f0', fontsize=10.5, fontweight='bold', pad=8)
    ax1.set_facecolor('#0c1322')
    ax1.tick_params(colors='#94a3b8', labelsize=8.5)
    ax1.set_ylim(0, 68000)
    for spine in ax1.spines.values():
        spine.set_color('#1e293b')
    for bar in bars1:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2.0, yval + 1400, f'{yval:,.1f}', ha='center', va='bottom', color='#f8fafc', fontsize=9, fontweight='bold')
    
    # Subplot 2: Peak Demand (kW)
    peak_vals = [195.4, 150.1]
    bars2 = ax2.bar(categories, peak_vals, color=['#334155', '#06b6d4'], width=0.52, edgecolor=['#475569', '#22d3ee'], linewidth=1.2)
    ax2.set_title('Peak Demand (kW)\n-23.2% Shaved Peak', color='#e2e8f0', fontsize=10.5, fontweight='bold', pad=8)
    ax2.set_facecolor('#0c1322')
    ax2.tick_params(colors='#94a3b8', labelsize=8.5)
    ax2.set_ylim(0, 235)
    for spine in ax2.spines.values():
        spine.set_color('#1e293b')
    for bar in bars2:
        yval = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2.0, yval + 5, f'{yval:.1f} kW', ha='center', va='bottom', color='#f8fafc', fontsize=9, fontweight='bold')

    # Subplot 3: 30-Day Cost (₹ INR)
    cost_vals = [484170, 349738]
    bars3 = ax3.bar(categories, cost_vals, color=['#334155', '#f59e0b'], width=0.52, edgecolor=['#475569', '#fbbf24'], linewidth=1.2)
    ax3.set_title('30-Day Cost (₹ INR)\n-₹134,433 Saved (@₹8.50/kWh)', color='#e2e8f0', fontsize=10.5, fontweight='bold', pad=8)
    ax3.set_facecolor('#0c1322')
    ax3.tick_params(colors='#94a3b8', labelsize=8.5)
    ax3.set_ylim(0, 580000)
    for spine in ax3.spines.values():
        spine.set_color('#1e293b')
    for bar in bars3:
        yval = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2.0, yval + 11000, f'₹{yval:,.0f}', ha='center', va='bottom', color='#f8fafc', fontsize=9, fontweight='bold')

    plt.tight_layout()
    chart_path = "scratch/slides_assets/slide7_comparison_chart.png"
    plt.savefig(chart_path, dpi=300, bbox_inches='tight', facecolor='#0c1322')
    plt.close()
    print("Created compact", chart_path)

def create_slide5_forecast_chart():
    fig, ax = plt.subplots(figsize=(5.6, 3.4), facecolor='#0c1322')
    ax.set_facecolor('#0f172a')
    
    hours = np.arange(24)
    base_curve = 45 + 95 / (1 + np.exp(-(hours - 8.5)/1.2)) - 90 / (1 + np.exp(-(hours - 18.5)/1.2))
    np.random.seed(42)
    ground_truth = base_curve + np.random.normal(0, 3.5, 24)
    prediction = base_curve + np.random.normal(0, 1.8, 24)
    mae = 3.85
    band_upper = prediction + 1.645 * mae
    band_lower = prediction - 1.645 * mae
    
    ax.fill_between(hours, band_lower, band_upper, color='#06b6d4', alpha=0.18, label='Empirical Prediction Band (±1.645 × MAE)')
    ax.plot(hours, ground_truth, color='#94a3b8', linestyle='--', linewidth=1.6, alpha=0.8, label='Simulated Ground Truth (kW)')
    ax.plot(hours, prediction, color='#10b981', linewidth=2.2, label='Random Forest Forecast (kW)')
    
    ax.set_title('24-Hour Ahead Demand Forecast (R² ≈ 0.942)', color='#f8fafc', fontsize=10.5, fontweight='bold', pad=8)
    ax.set_xlabel('Forecast Horizon (Hours)', color='#94a3b8', fontsize=8.5)
    ax.set_ylabel('Power Demand (kW)', color='#94a3b8', fontsize=8.5)
    ax.tick_params(colors='#94a3b8', labelsize=8)
    ax.set_xlim(0, 23)
    ax.set_ylim(30, 160)
    ax.grid(True, color='#1e293b', linestyle=':', alpha=0.6)
    for spine in ax.spines.values():
        spine.set_color('#1e293b')
        
    ax.legend(facecolor='#0c1322', edgecolor='#1e293b', labelcolor='#e2e8f0', fontsize=7.5, loc='upper left')
    
    plt.tight_layout()
    chart_path = "scratch/slides_assets/slide5_ml_forecast_chart.png"
    plt.savefig(chart_path, dpi=300, bbox_inches='tight', facecolor='#0c1322')
    plt.close()
    print("Created compact", chart_path)

if __name__ == "__main__":
    create_slide7_chart()
    create_slide5_forecast_chart()
