import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    # 16:9 widescreen layout
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Professional Dark Theme Palette
    BG_COLOR = RGBColor(10, 15, 29)          # #0A0F1D Deep Navy Slate
    CARD_BG = RGBColor(17, 24, 39)          # #111827 Dark Slate
    CARD_BORDER = RGBColor(30, 41, 59)      # #1E293B Border
    CARD_BG_ALT = RGBColor(15, 23, 42)      # #0F172A
    
    PRIMARY_EMERALD = RGBColor(16, 185, 129)# #10B981 Emerald Green
    ACCENT_CYAN = RGBColor(6, 182, 212)     # #06B6D4 Cyan
    ACCENT_AMBER = RGBColor(245, 158, 11)   # #F59E0B Amber
    ACCENT_PURPLE = RGBColor(139, 92, 246)  # #8B5CF6 Purple
    ALERT_RED = RGBColor(239, 68, 68)       # #EF4444 Red
    ACCENT_BLUE = RGBColor(59, 130, 246)    # #3B82F6 Blue
    
    TEXT_WHITE = RGBColor(248, 250, 252)    # #F8FAFC
    TEXT_MUTED = RGBColor(148, 163, 184)    # #94A3B8
    TEXT_DIM = RGBColor(100, 116, 139)      # #64748B

    def set_slide_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_COLOR
        bg.line.fill.background()
        return bg

    def add_header(slide, title_text, category_text, badge_text=None, badge_color=ACCENT_CYAN):
        # Category
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(8.5), Inches(0.28))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        tf_cat.margin_left = tf_cat.margin_top = tf_cat.margin_right = tf_cat.margin_bottom = 0
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.size = Pt(9.5)
        p_cat.font.bold = True
        p_cat.font.color.rgb = ACCENT_CYAN
        p_cat.font.name = 'Segoe UI'

        # Main Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.68), Inches(8.8), Inches(0.55))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        tf_title.margin_left = tf_title.margin_top = tf_title.margin_right = tf_title.margin_bottom = 0
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(21)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_WHITE
        p_title.font.name = 'Segoe UI'

        # Optional Provenance / Status Badge
        if badge_text:
            badge_width = Inches(3.2)
            badge_shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.333), Inches(0.55), badge_width, Inches(0.42))
            badge_shape.fill.solid()
            badge_shape.fill.fore_color.rgb = RGBColor(15, 23, 42)
            badge_shape.line.color.rgb = badge_color
            badge_shape.line.width = Pt(1.2)
            
            tf_b = badge_shape.text_frame
            tf_b.vertical_anchor = MSO_ANCHOR.MIDDLE
            tf_b.margin_left = tf_b.margin_right = Inches(0.05)
            p_b = tf_b.paragraphs[0]
            p_b.alignment = PP_ALIGN.CENTER
            p_b.text = badge_text
            p_b.font.size = Pt(8.5)
            p_b.font.bold = True
            p_b.font.color.rgb = badge_color
            p_b.font.name = 'Segoe UI'

    def add_footer(slide, current_slide, total_slides=10):
        footer_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.05), Inches(11.733), Inches(0.28))
        tf = footer_box.text_frame
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = f"EcoSense AI • Intelligent Building Energy Optimizer  |  Yuva Yodha Energy Tech Hackathon 2026 (Smart Buildings)               Slide {current_slide} of {total_slides}"
        p.font.size = Pt(8.5)
        p.font.color.rgb = TEXT_DIM
        p.font.name = 'Segoe UI'

    def create_card_shape(slide, left, top, width, height, bg=CARD_BG, border=CARD_BORDER, border_width=1.0):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg
        card.line.color.rgb = border
        card.line.width = Pt(border_width)
        return card

    # =========================================================================
    # SLIDE 1: TITLE SLIDE
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1)

    # Top Hackathon Track Pill
    pill = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.9), Inches(5.0), Inches(0.38))
    pill.fill.solid()
    pill.fill.fore_color.rgb = PRIMARY_EMERALD
    pill.line.fill.background()
    p_tf = pill.text_frame
    p_tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p_p = p_tf.paragraphs[0]
    p_p.alignment = PP_ALIGN.CENTER
    p_p.text = "YUVA YODHA ENERGY TECH HACKATHON 2026  •  SMART BUILDINGS"
    p_p.font.size = Pt(9)
    p_p.font.bold = True
    p_p.font.color.rgb = RGBColor(10, 15, 29)
    p_p.font.name = 'Segoe UI'

    # Main Title
    t_box = s1.shapes.add_textbox(Inches(0.8), Inches(1.5), Inches(7.2), Inches(1.1))
    tf1 = t_box.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_top = tf1.margin_right = tf1.margin_bottom = 0
    p1 = tf1.paragraphs[0]
    p1.text = "EcoSense AI"
    p1.font.size = Pt(48)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_WHITE
    p1.font.name = 'Segoe UI'

    # Subtitle
    sub_box = s1.shapes.add_textbox(Inches(0.8), Inches(2.65), Inches(7.2), Inches(0.5))
    tf_sub = sub_box.text_frame
    tf_sub.word_wrap = True
    tf_sub.margin_left = tf_sub.margin_top = tf_sub.margin_right = tf_sub.margin_bottom = 0
    p_sub = tf_sub.paragraphs[0]
    p_sub.text = "Intelligent Building Energy Optimizer"
    p_sub.font.size = Pt(22)
    p_sub.font.bold = True
    p_sub.font.color.rgb = PRIMARY_EMERALD
    p_sub.font.name = 'Segoe UI'

    # Tagline
    tag_box = s1.shapes.add_textbox(Inches(0.8), Inches(3.3), Inches(7.2), Inches(0.5))
    tf_tag = tag_box.text_frame
    tf_tag.word_wrap = True
    tf_tag.margin_left = tf_tag.margin_top = tf_tag.margin_right = tf_tag.margin_bottom = 0
    p_tag = tf_tag.paragraphs[0]
    p_tag.text = "AI-Powered Energy Efficiency  •  Comfort Management  •  Peak Demand Shaving"
    p_tag.font.size = Pt(12)
    p_tag.font.color.rgb = TEXT_MUTED
    p_tag.font.name = 'Segoe UI'

    # Prototype Verification Card
    create_card_shape(s1, Inches(0.8), Inches(4.0), Inches(6.9), Inches(1.4), bg=CARD_BG_ALT, border=CARD_BORDER)
    tb_pr = s1.shapes.add_textbox(Inches(1.05), Inches(4.15), Inches(6.4), Inches(1.1))
    tf_pr = tb_pr.text_frame
    tf_pr.vertical_anchor = MSO_ANCHOR.TOP
    tf_pr.word_wrap = True
    tf_pr.margin_left = tf_pr.margin_top = tf_pr.margin_right = tf_pr.margin_bottom = 0

    p_pr1 = tf_pr.paragraphs[0]
    p_pr1.text = "PROTOTYPE SPECIFICATION & STATUS"
    p_pr1.font.size = Pt(9.5)
    p_pr1.font.bold = True
    p_pr1.font.color.rgb = ACCENT_CYAN
    p_pr1.font.name = 'Segoe UI'
    p_pr1.space_after = Pt(4)

    p_pr2 = tf_pr.add_paragraph()
    p_pr2.text = "• Fully functional software simulation prototype & analytics decision support platform\n• Evaluated on 5 commercial building zones (~2,300 m²) with 30-day simulated telemetry\n• Machine learning demand forecasting with multi-objective comfort and peak shaving"
    p_pr2.font.size = Pt(9)
    p_pr2.font.color.rgb = TEXT_MUTED
    p_pr2.font.name = 'Segoe UI'

    # Team Box
    create_card_shape(s1, Inches(0.8), Inches(5.6), Inches(6.9), Inches(1.1), bg=CARD_BG_ALT, border=CARD_BORDER)
    tb_t = s1.shapes.add_textbox(Inches(1.05), Inches(5.75), Inches(6.4), Inches(0.8))
    tf_t = tb_t.text_frame
    tf_t.vertical_anchor = MSO_ANCHOR.TOP
    tf_t.word_wrap = True
    tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0

    p_t1 = tf_t.paragraphs[0]
    p_t1.text = "TEAM MEMBERS"
    p_t1.font.size = Pt(9.5)
    p_t1.font.bold = True
    p_t1.font.color.rgb = PRIMARY_EMERALD
    p_t1.font.name = 'Segoe UI'
    p_t1.space_after = Pt(3)

    p_t2 = tf_t.add_paragraph()
    p_t2.text = "[Add team member names]"
    p_t2.font.size = Pt(12)
    p_t2.font.bold = True
    p_t2.font.color.rgb = TEXT_WHITE
    p_t2.font.name = 'Segoe UI'

    # Right Column: 3 Concept Cards
    hero_cards = [
        ("27.8% SIMULATED REDUCTION", PRIMARY_EMERALD, "Energy Efficiency", "Simulated electrical energy reduction vs. defined fixed-schedule baseline across 30 days."),
        ("23.2% PEAK DEMAND SHAVED", ACCENT_CYAN, "Peak Demand Clipping", "Predictive pre-cooling and load modulation to curb high-tariff commercial peak spikes."),
        ("COMFORT-AWARE CONTROL", ACCENT_AMBER, "Thermal Environment", "Strict temperature proxy bounds (22°C–26°C) enforced across all occupied zone hours.")
    ]

    for idx, (title, color, sub, body) in enumerate(hero_cards):
        y_pos = Inches(1.5) + idx * Inches(1.75)
        create_card_shape(s1, Inches(8.1), y_pos, Inches(4.433), Inches(1.55), bg=CARD_BG, border=color, border_width=1.2)
        tb_hc = s1.shapes.add_textbox(Inches(8.35), y_pos + Inches(0.2), Inches(3.95), Inches(1.15))
        tf_hc = tb_hc.text_frame
        tf_hc.vertical_anchor = MSO_ANCHOR.TOP
        tf_hc.word_wrap = True
        tf_hc.margin_left = tf_hc.margin_top = tf_hc.margin_right = tf_hc.margin_bottom = 0

        p_h1 = tf_hc.paragraphs[0]
        p_h1.text = title
        p_h1.font.size = Pt(15)
        p_h1.font.bold = True
        p_h1.font.color.rgb = color
        p_h1.font.name = 'Segoe UI'
        p_h1.space_after = Pt(2)

        p_h2 = tf_hc.add_paragraph()
        p_h2.text = sub.upper()
        p_h2.font.size = Pt(8.5)
        p_h2.font.bold = True
        p_h2.font.color.rgb = TEXT_WHITE
        p_h2.font.name = 'Segoe UI'
        p_h2.space_after = Pt(4)

        p_h3 = tf_hc.add_paragraph()
        p_h3.text = body
        p_h3.font.size = Pt(9)
        p_h3.font.color.rgb = TEXT_MUTED
        p_h3.font.name = 'Segoe UI'

    add_footer(s1, 1)

    # =========================================================================
    # SLIDE 2: THE PROBLEM
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2)
    add_header(s2, "The Problem: Buildings Waste Energy When Demand Changes", "The Commercial Building Dilemma")

    # Visual Flow Banner
    create_card_shape(s2, Inches(0.8), Inches(1.35), Inches(11.733), Inches(0.7), bg=CARD_BG_ALT, border=CARD_BORDER)
    tb_flow = s2.shapes.add_textbox(Inches(0.9), Inches(1.45), Inches(11.533), Inches(0.5))
    tf_fl = tb_flow.text_frame
    tf_fl.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf_fl.margin_left = tf_fl.margin_top = tf_fl.margin_right = tf_fl.margin_bottom = 0
    p_fl = tf_fl.paragraphs[0]
    p_fl.alignment = PP_ALIGN.CENTER
    p_fl.text = "Fixed Schedule   →   Over-Conditioning / Unnecessary Lighting   →   Energy Waste  +  Peak Demand  +  Comfort Trade-offs"
    p_fl.font.size = Pt(11.5)
    p_fl.font.bold = True
    p_fl.font.color.rgb = ACCENT_CYAN
    p_fl.font.name = 'Segoe UI'

    # 3 Problem Pillars
    p_w = Inches(3.75)
    p_gap = Inches(0.24)
    p_top = Inches(2.25)
    p_h = Inches(3.85)

    pillars = [
        ("1. ENERGY WASTE", ALERT_RED, "The Vacancy Paradox", [
            ("Rigid Timers:", "HVAC and lighting run full power on fixed schedules (07:00–19:00) regardless of actual zone occupancy."),
            ("Vacant Space:", "Hybrid work leaves conference rooms and entire wings empty 30–50% of the day while consuming full cooling power."),
            ("Avoidable Base Load:", "Overcooling unoccupied spaces drives massive, continuous utility energy waste.")
        ]),
        ("2. PEAK DEMAND SPIKES", ACCENT_AMBER, "Grid & Tariff Strain", [
            ("Afternoon Surge:", "Ambient heat gain and simultaneous building occupancy trigger severe peak demand spikes (kW) in early afternoon."),
            ("Demand Penalties:", "Commercial utilities impose steep Maximum Demand Charges based on monthly peak kW spikes."),
            ("Grid Inefficiency:", "Coincident peak demand forces utilities to dispatch expensive, carbon-intensive peaker plants.")
        ]),
        ("3. COMFORT TRADE-OFFS", ACCENT_CYAN, "Thermal Discontent", [
            ("Static Setpoints:", "Thermostats hold a flat setpoint (22°C) without adapting to localized solar gain or fluctuating occupant density."),
            ("Simultaneous Extremes:", "Causes simultaneous overcooling in empty zones (coats in summer) and stuffiness in crowded spaces."),
            ("Manual Tampering:", "Frustrated occupants manually adjust setpoints, exacerbating energy waste and system strain.")
        ])
    ]

    for idx, (title, color, sub, items) in enumerate(pillars):
        x = Inches(0.8) + idx * (p_w + p_gap)
        create_card_shape(s2, x, p_top, p_w, p_h, bg=CARD_BG, border=color, border_width=1.2)
        
        tb = s2.shapes.add_textbox(x + Inches(0.25), p_top + Inches(0.22), p_w - Inches(0.5), p_h - Inches(0.44))
        tf = tb.text_frame
        tf.vertical_anchor = MSO_ANCHOR.TOP
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p1 = tf.paragraphs[0]
        p1.text = title
        p1.font.size = Pt(13)
        p1.font.bold = True
        p1.font.color.rgb = color
        p1.font.name = 'Segoe UI'
        p1.space_after = Pt(2)

        p2 = tf.add_paragraph()
        p2.text = sub.upper()
        p2.font.size = Pt(8.5)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_WHITE
        p2.font.name = 'Segoe UI'
        p2.space_after = Pt(8)

        for heading, body in items:
            pb = tf.add_paragraph()
            pb.text = f"• {heading} {body}"
            pb.font.size = Pt(9.2)
            pb.font.color.rgb = TEXT_MUTED
            pb.font.name = 'Segoe UI'
            pb.space_after = Pt(6)

    # Bottom Takeaway Card
    create_card_shape(s2, Inches(0.8), Inches(6.28), Inches(11.733), Inches(0.55), bg=CARD_BG_ALT, border=CARD_BORDER)
    tb_ta = s2.shapes.add_textbox(Inches(1.0), Inches(6.36), Inches(11.333), Inches(0.4))
    tf_ta = tb_ta.text_frame
    tf_ta.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf_ta.margin_left = tf_ta.margin_top = tf_ta.margin_right = tf_ta.margin_bottom = 0
    p_ta = tf_ta.paragraphs[0]
    p_ta.text = "THE NEED: Building managers need an automated software layer to turn occupancy, environmental, and energy telemetry into actionable, comfort-safe operating decisions."
    p_ta.font.size = Pt(9.5)
    p_ta.font.bold = True
    p_ta.font.color.rgb = TEXT_WHITE
    p_ta.font.name = 'Segoe UI'

    add_footer(s2, 2)

    # =========================================================================
    # SLIDE 3: OUR SOLUTION
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3)
    add_header(s3, "Our Solution: EcoSense AI", "Closed-Loop Intelligent Control", badge_text="SOFTWARE SIMULATION PROTOTYPE", badge_color=ACCENT_CYAN)

    # Core Value Banner
    create_card_shape(s3, Inches(0.8), Inches(1.35), Inches(11.733), Inches(0.65), bg=CARD_BG_ALT, border=PRIMARY_EMERALD, border_width=1.2)
    tb_sb = s3.shapes.add_textbox(Inches(1.0), Inches(1.43), Inches(11.333), Inches(0.5))
    tf_sb = tb_sb.text_frame
    tf_sb.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf_sb.margin_left = tf_sb.margin_top = tf_sb.margin_right = tf_sb.margin_bottom = 0
    p_sb = tf_sb.paragraphs[0]
    p_sb.alignment = PP_ALIGN.CENTER
    p_sb.text = "\"An intelligent software layer for smarter building energy decisions.\""
    p_sb.font.size = Pt(14)
    p_sb.font.bold = True
    p_sb.font.color.rgb = PRIMARY_EMERALD
    p_sb.font.name = 'Segoe UI'

    # 5-Stage Closed-Loop Cards
    w3 = Inches(2.23)
    gap3 = Inches(0.14)
    top3 = Inches(2.2)
    h3 = Inches(3.9)

    stages = [
        ("1. SENSE", ACCENT_CYAN, "Telemetry Ingestion", [
            "Zone-level occupancy (headcount)",
            "Dry-bulb temperature (°C)",
            "Relative humidity & IAQ (CO₂)",
            "HVAC, lighting, & plug loads",
            "Simulated multi-zone telemetry"
        ]),
        ("2. PREDICT", ACCENT_PURPLE, "Machine Learning", [
            "Random Forest Regressor",
            "24-Hour lookahead horizon",
            "Diurnal pattern modeling",
            "Empirical prediction bands (±1.645 × MAE)",
            "Early peak surge alerts"
        ]),
        ("3. OPTIMIZE", PRIMARY_EMERALD, "Multi-Objective Solver", [
            "Simultaneous 3-way balance",
            "Minimize total electrical kWh",
            "Enforce comfort proxy (22°C–26°C)",
            "Clip peak demand spikes (<175 kW)",
            "Predictive thermal pre-cooling"
        ]),
        ("4. RECOMMEND", ACCENT_AMBER, "Actionable Advisories", [
            "Dynamic occupancy setbacks",
            "Daylight harvesting dimming",
            "Pre-cooling control triggers",
            "Quantified kWh & ₹ savings",
            "Human-in-the-loop decisions"
        ]),
        ("5. MEASURE", ACCENT_BLUE, "Transparent Metrics", [
            "Baseline vs. optimized engine",
            "Real-time cost avoidance",
            "Grid CO₂ abatement tracking",
            "Auditable data provenance",
            "Comfort compliance proxy %"
        ])
    ]

    for idx, (stage_name, color, subtitle, bullets) in enumerate(stages):
        x = Inches(0.8) + idx * (w3 + gap3)
        create_card_shape(s3, x, top3, w3, h3, bg=CARD_BG, border=color, border_width=1.2)

        tb = s3.shapes.add_textbox(x + Inches(0.16), top3 + Inches(0.2), w3 - Inches(0.32), h3 - Inches(0.4))
        tf = tb.text_frame
        tf.vertical_anchor = MSO_ANCHOR.TOP
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p1 = tf.paragraphs[0]
        p1.text = stage_name
        p1.font.size = Pt(13)
        p1.font.bold = True
        p1.font.color.rgb = color
        p1.font.name = 'Segoe UI'
        p1.space_after = Pt(2)

        p2 = tf.add_paragraph()
        p2.text = subtitle.upper()
        p2.font.size = Pt(8.5)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_WHITE
        p2.font.name = 'Segoe UI'
        p2.space_after = Pt(8)

        for b in bullets:
            pb = tf.add_paragraph()
            pb.text = f"• {b}"
            pb.font.size = Pt(9)
            pb.font.color.rgb = TEXT_MUTED
            pb.font.name = 'Segoe UI'
            pb.space_after = Pt(5)

    # Bottom Provenance Box
    create_card_shape(s3, Inches(0.8), Inches(6.3), Inches(11.733), Inches(0.52), bg=CARD_BG_ALT, border=CARD_BORDER)
    tb_pn = s3.shapes.add_textbox(Inches(1.0), Inches(6.38), Inches(11.333), Inches(0.4))
    tf_pn = tb_pn.text_frame
    tf_pn.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf_pn.margin_left = tf_pn.margin_top = tf_pn.margin_right = tf_pn.margin_bottom = 0
    p_pn = tf_pn.paragraphs[0]
    p_pn.text = "PROTOTYPE NOTICE: The current EcoSense AI prototype operates on high-resolution simulated multi-zone commercial building telemetry to prove algorithmic optimization feasibility prior to physical hardware retrofits."
    p_pn.font.size = Pt(8.8)
    p_pn.font.color.rgb = TEXT_MUTED
    p_pn.font.name = 'Segoe UI'

    add_footer(s3, 3)

    # =========================================================================
    # SLIDE 4: HOW IT WORKS (ARCHITECTURE)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4)
    add_header(s4, "From Building Data to Energy Decisions", "End-to-End System Architecture")

    b_w = Inches(2.75)
    b_gap = Inches(0.24)
    b_top = Inches(1.4)
    b_h = Inches(4.7)

    arch_blocks = [
        ("INPUT TELEMETRY", ACCENT_CYAN, "Simulated Building Signals", [
            "Occupancy (headcount per zone)",
            "Dry-bulb Temperature (°C)",
            "Relative Humidity (%)",
            "Indoor Air Quality (CO₂ ppm)",
            "HVAC electrical power (kW)",
            "Lighting load (kW)",
            "Plug & equipment load (kW)",
            "Historical demand timeseries"
        ]),
        ("AI / ML LAYER", ACCENT_PURPLE, "Predictive Engine", [
            "Time-series feature pipeline",
            "Lag-1h & Lag-24h power signals",
            "Diurnal calendar features",
            "Random Forest Regressor (N=100)",
            "24-Hour forward forecast",
            "Test R² ≈ 0.942, MAE ≈ 3.85 kW",
            "Approx. Empirical Prediction Band (±1.645 × MAE)",
            "Anticipates peak surge hours"
        ]),
        ("OPTIMIZATION ENGINE", PRIMARY_EMERALD, "Constraint Optimization", [
            "Multi-objective solver",
            "Dynamic occupancy setbacks",
            "Daylight harvesting dimming",
            "Predictive thermal pre-cooling",
            "Peak clipping threshold (<175 kW)",
            "Comfort boundary enforcement (22.0°C–26.0°C)",
            "Generates prioritized advisories",
            "Explainable savings breakdown"
        ]),
        ("DECISION COCKPIT", ACCENT_AMBER, "Human-in-the-Loop Cockpit", [
            "Real-time Facility Dashboard",
            "Multi-Zone Spatial Heatmap",
            "Interactive Scenario Lab (A/B/C/D)",
            "Baseline vs. Optimized Engine",
            "One-click Accept / Dismiss",
            "Illustrative Deployment ROI",
            "Transparent Limitations View",
            "FastAPI REST backend + Next.js"
        ])
    ]

    for idx, (title, color, sub, bullets) in enumerate(arch_blocks):
        x = Inches(0.8) + idx * (b_w + b_gap)
        create_card_shape(s4, x, b_top, b_w, b_h, bg=CARD_BG, border=color, border_width=1.2)

        tb = s4.shapes.add_textbox(x + Inches(0.2), b_top + Inches(0.2), b_w - Inches(0.4), b_h - Inches(0.4))
        tf = tb.text_frame
        tf.vertical_anchor = MSO_ANCHOR.TOP
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p1 = tf.paragraphs[0]
        p1.text = title
        p1.font.size = Pt(13)
        p1.font.bold = True
        p1.font.color.rgb = color
        p1.font.name = 'Segoe UI'
        p1.space_after = Pt(2)

        p2 = tf.add_paragraph()
        p2.text = sub.upper()
        p2.font.size = Pt(8.5)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_WHITE
        p2.font.name = 'Segoe UI'
        p2.space_after = Pt(8)

        for b in bullets:
            pb = tf.add_paragraph()
            pb.text = f"• {b}"
            pb.font.size = Pt(9)
            pb.font.color.rgb = TEXT_MUTED
            pb.font.name = 'Segoe UI'
            pb.space_after = Pt(5)

    # Bottom Pipeline Summary
    create_card_shape(s4, Inches(0.8), Inches(6.28), Inches(11.733), Inches(0.55), bg=CARD_BG_ALT, border=CARD_BORDER)
    tb_pb = s4.shapes.add_textbox(Inches(1.0), Inches(6.36), Inches(11.333), Inches(0.4))
    tf_pb = tb_pb.text_frame
    tf_pb.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf_pb.margin_left = tf_pb.margin_top = tf_pb.margin_right = tf_pb.margin_bottom = 0
    p_pb = tf_pb.paragraphs[0]
    p_pb.alignment = PP_ALIGN.CENTER
    p_pb.text = "DATA PIPELINE: Telemetry Ingestion → Feature Pipeline → Random Forest Forecast → Multi-Objective Optimizer → Decision Cockpit"
    p_pb.font.size = Pt(9.5)
    p_pb.font.bold = True
    p_pb.font.color.rgb = TEXT_WHITE
    p_pb.font.name = 'Segoe UI'

    add_footer(s4, 4)

    # =========================================================================
    # SLIDE 5: AI / TECHNICAL APPROACH
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5)
    add_header(s5, "Technical Approach: Data, ML & Optimization", "Core Algorithms & Scientific Rigor")

    left_w = Inches(5.6)

    # 3 Layers on Left
    l_configs = [
        ("1. DATA & SIMULATION FOUNDATION", ACCENT_CYAN, Inches(1.35), Inches(1.5), [
            "30 days continuous hourly simulated building data (720 records, PRNG seed=42)",
            "5 distinct commercial zones (~2,300 m²): Lobby, Office Floor, Meeting Room, Conference Room, Cafeteria",
            "Deterministic thermodynamics modeling diurnal ambient temp, solar heat, & occupant heat loads"
        ]),
        ("2. MACHINE LEARNING FORECASTING", ACCENT_PURPLE, Inches(2.95), Inches(1.6), [
            "Algorithm: RandomForestRegressor (100 estimators, max depth 12)",
            "Anti-Leakage: Strict 80/20 chronological train-test split (no future lookahead)",
            "Prototype Metrics (Test set): R² ≈ 0.942 | MAE ≈ 3.85 kW | RMSE ≈ 5.21 kW",
            "Uncertainty Spread: Approximate Empirical Prediction Band (±1.645 × MAE)"
        ]),
        ("3. MULTI-OBJECTIVE OPTIMIZATION", PRIMARY_EMERALD, Inches(4.65), Inches(1.5), [
            "Objective Concept: Balance Energy Efficiency + Comfort Proxy + Peak Demand",
            "Comfort Target: Enforces strict temperature envelope 22.0°C – 26.0°C",
            "Peak Shaving: Proactive thermal pre-cooling when forecast exceeds 175 kW threshold",
            "Zone Actions: Setback unoccupied rooms to 25.5°C; harvest daylight for lighting"
        ])
    ]

    for title, color, top_pos, height_pos, bullets in l_configs:
        create_card_shape(s5, Inches(0.8), top_pos, left_w, height_pos, bg=CARD_BG, border=color, border_width=1.1)
        tb = s5.shapes.add_textbox(Inches(1.0), top_pos + Inches(0.14), left_w - Inches(0.4), height_pos - Inches(0.28))
        tf = tb.text_frame
        tf.vertical_anchor = MSO_ANCHOR.TOP
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p1 = tf.paragraphs[0]
        p1.text = title
        p1.font.size = Pt(11)
        p1.font.bold = True
        p1.font.color.rgb = color
        p1.font.name = 'Segoe UI'
        p1.space_after = Pt(4)

        for b in bullets:
            pb = tf.add_paragraph()
            pb.text = f"• {b}"
            pb.font.size = Pt(8.5)
            pb.font.color.rgb = TEXT_MUTED
            pb.font.name = 'Segoe UI'
            pb.space_after = Pt(2.5)

    # Right Column: Matplotlib Forecast Chart Image
    create_card_shape(s5, Inches(6.65), Inches(1.35), Inches(5.883), Inches(4.8), bg=CARD_BG, border=CARD_BORDER)
    c5_path = "scratch/slides_assets/slide5_ml_forecast_chart.png"
    if os.path.exists(c5_path):
        s5.shapes.add_picture(c5_path, Inches(6.8), Inches(1.5), width=Inches(5.58))

    # Bottom Concept formula
    create_card_shape(s5, Inches(0.8), Inches(6.3), Inches(11.733), Inches(0.52), bg=CARD_BG_ALT, border=CARD_BORDER)
    tb_fb = s5.shapes.add_textbox(Inches(1.0), Inches(6.38), Inches(11.333), Inches(0.4))
    tf_fb = tb_fb.text_frame
    tf_fb.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf_fb.margin_left = tf_fb.margin_top = tf_fb.margin_right = tf_fb.margin_bottom = 0
    p_fb = tf_fb.paragraphs[0]
    p_fb.alignment = PP_ALIGN.CENTER
    p_fb.text = "CORE OBJECTIVE FORMULA:  Minimize [ Total Electrical kWh ]  Subject to:  22°C ≤ T_zone ≤ 26°C  AND  Peak Demand ≤ 175 kW"
    p_fb.font.size = Pt(9.5)
    p_fb.font.bold = True
    p_fb.font.color.rgb = PRIMARY_EMERALD
    p_fb.font.name = 'Segoe UI'

    add_footer(s5, 5)

    # =========================================================================
    # SLIDE 6: PRODUCT / USER JOURNEY
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6)
    add_header(s6, "A Building Manager's Decision Journey", "Operator Experience & Cockpit Workflow")

    steps = [
        ("1. Open Dashboard", "Glances at live power, simulated cost avoidance, and comfort compliance KPIs."),
        ("2. View Current Energy", "Inspects diurnal 24h demand curve and zone-level power distribution."),
        ("3. Check Forecast", "Evaluates 24-hr ML demand curve to anticipate afternoon peak spikes."),
        ("4. Identify High Zones", "Locates over-conditioned zones via spatial 5-zone interactive heatmap."),
        ("5. Review AI Actions", "Inspects contextual advisories with quantified electrical kWh savings."),
        ("6. Accept or Dismiss", "Operator approves recommendations via one-click human-in-the-loop controls."),
        ("7. Compare Scenarios", "Explores 4 automation tiers (Baseline vs. Occupancy vs. Full EcoSense)."),
        ("8. Measure Impact", "Audits comfort compliance % and models economics in Deployment Calculator.")
    ]

    card_w6 = Inches(2.78)
    card_h6 = Inches(1.9)
    gap_x6 = Inches(0.2)
    gap_y6 = Inches(0.2)

    for idx, (step_title, step_desc) in enumerate(steps):
        row = idx // 4
        col = idx % 4
        x = Inches(0.8) + col * (card_w6 + gap_x6)
        y = Inches(1.4) + row * (card_h6 + gap_y6)

        color_border = PRIMARY_EMERALD if idx in [0, 4, 6] else CARD_BORDER
        create_card_shape(s6, x, y, card_w6, card_h6, bg=CARD_BG, border=color_border, border_width=1.2)

        tb = s6.shapes.add_textbox(x + Inches(0.2), y + Inches(0.2), card_w6 - Inches(0.4), card_h6 - Inches(0.4))
        tf = tb.text_frame
        tf.vertical_anchor = MSO_ANCHOR.TOP
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p1 = tf.paragraphs[0]
        p1.text = step_title
        p1.font.size = Pt(12)
        p1.font.bold = True
        p1.font.color.rgb = ACCENT_CYAN if idx in [0, 4, 6] else TEXT_WHITE
        p1.font.name = 'Segoe UI'
        p1.space_after = Pt(6)

        p2 = tf.add_paragraph()
        p2.text = step_desc
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = TEXT_MUTED
        p2.font.name = 'Segoe UI'

    # Implemented Prototype Pages Card
    create_card_shape(s6, Inches(0.8), Inches(5.6), Inches(11.733), Inches(1.2), bg=CARD_BG_ALT, border=CARD_BORDER)
    tb_pb = s6.shapes.add_textbox(Inches(1.05), Inches(5.72), Inches(11.233), Inches(0.95))
    tf_pb = tb_pb.text_frame
    tf_pb.vertical_anchor = MSO_ANCHOR.TOP
    tf_pb.word_wrap = True
    tf_pb.margin_left = tf_pb.margin_top = tf_pb.margin_right = tf_pb.margin_bottom = 0

    p_pb1 = tf_pb.paragraphs[0]
    p_pb1.text = "IMPLEMENTED PROTOTYPE PAGES & CAPABILITIES"
    p_pb1.font.size = Pt(9.5)
    p_pb1.font.bold = True
    p_pb1.font.color.rgb = PRIMARY_EMERALD
    p_pb1.font.name = 'Segoe UI'
    p_pb1.space_after = Pt(3)

    p_pb2 = tf_pb.add_paragraph()
    p_pb2.text = "• Dashboard (/dashboard): Real-time operations cockpit, active telemetry, comfort compliance gauge, live advisories\n• Multi-Zone Map (/zones): 5 commercial zones with thermal load, headcount occupancy, and IAQ metrics\n• Scenario Lab (/scenarios): Interactive what-if sandbox testing setpoint offsets, occupancy sensitivity, & solar gain\n• Simulation (/simulation): 30-day continuous baseline vs. EcoSense evaluation | Deployment (/deployment): Illustrative ROI"
    p_pb2.font.size = Pt(8.8)
    p_pb2.font.color.rgb = TEXT_MUTED
    p_pb2.font.name = 'Segoe UI'

    add_footer(s6, 6)

    # =========================================================================
    # SLIDE 7: SIMULATION RESULTS (VERY IMPORTANT)
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7)
    add_header(s7, "Simulation Results: Baseline vs. EcoSense", "Prototype Performance Evaluation", badge_text="SIMULATION RESULT — NOT MEASURED REAL DATA", badge_color=ACCENT_AMBER)

    # Subtitle Context
    ctx_box = s7.shapes.add_textbox(Inches(0.8), Inches(1.22), Inches(11.733), Inches(0.3))
    tf_ctx = ctx_box.text_frame
    tf_ctx.margin_left = tf_ctx.margin_top = tf_ctx.margin_right = tf_ctx.margin_bottom = 0
    p_ctx = tf_ctx.paragraphs[0]
    p_ctx.text = "The prototype simulation evaluates a 27.8% energy reduction versus the defined fixed-schedule baseline across 30 days."
    p_ctx.font.size = Pt(10.5)
    p_ctx.font.bold = True
    p_ctx.font.color.rgb = PRIMARY_EMERALD
    p_ctx.font.name = 'Segoe UI'

    # 4 Key Metrics Cards
    m_w = Inches(2.78)
    m_gap = Inches(0.2)
    m_top = Inches(1.58)
    m_h = Inches(1.5)

    metrics = [
        ("ENERGY SAVED", "15,816.3 kWh", "27.8% Simulated Reduction", "Baseline: 56,961.7 kWh  |  Optimized: 41,145.4 kWh", PRIMARY_EMERALD),
        ("PEAK SHAVED", "45.3 kW", "23.2% Peak Shaved", "Baseline: 195.4 kW  |  Optimized: 150.1 kW", ACCENT_CYAN),
        ("COST SAVING", "₹134,433", "Simulated Cost Avoidance", "Baseline: ₹484,170  |  Optimized: ₹349,738 (@₹8.50/kWh)", ACCENT_AMBER),
        ("CO₂ ABATED", "12,969.4 kg", "Simulated Emissions Cut", "Grid Factor: 0.82 kg CO₂/kWh (CEA Baseline)", RGBColor(168, 85, 247))
    ]

    for idx, (label, val, highlight, details, color) in enumerate(metrics):
        x = Inches(0.8) + idx * (m_w + m_gap)
        create_card_shape(s7, x, m_top, m_w, m_h, bg=CARD_BG, border=color, border_width=1.2)

        tb = s7.shapes.add_textbox(x + Inches(0.18), m_top + Inches(0.14), m_w - Inches(0.36), m_h - Inches(0.28))
        tf = tb.text_frame
        tf.vertical_anchor = MSO_ANCHOR.TOP
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p1 = tf.paragraphs[0]
        p1.text = label
        p1.font.size = Pt(8.5)
        p1.font.bold = True
        p1.font.color.rgb = TEXT_MUTED
        p1.font.name = 'Segoe UI'
        p1.space_after = Pt(1)

        p2 = tf.add_paragraph()
        p2.text = val
        p2.font.size = Pt(19)
        p2.font.bold = True
        p2.font.color.rgb = color
        p2.font.name = 'Segoe UI'
        p2.space_after = Pt(1)

        p3 = tf.add_paragraph()
        p3.text = highlight
        p3.font.size = Pt(9)
        p3.font.bold = True
        p3.font.color.rgb = TEXT_WHITE
        p3.font.name = 'Segoe UI'
        p3.space_after = Pt(2)

        p4 = tf.add_paragraph()
        p4.text = details
        p4.font.size = Pt(7.5)
        p4.font.color.rgb = TEXT_DIM
        p4.font.name = 'Segoe UI'

    # Matplotlib 3-subplot comparison chart
    create_card_shape(s7, Inches(0.8), Inches(3.2), Inches(11.733), Inches(3.05), bg=CARD_BG, border=CARD_BORDER)
    c7_path = "scratch/slides_assets/slide7_comparison_chart.png"
    if os.path.exists(c7_path):
        s7.shapes.add_picture(c7_path, Inches(0.95), Inches(3.28), width=Inches(11.433))

    # Bottom Comfort Compliance Note
    create_card_shape(s7, Inches(0.8), Inches(6.38), Inches(11.733), Inches(0.48), bg=CARD_BG_ALT, border=CARD_BORDER)
    tb_s7 = s7.shapes.add_textbox(Inches(1.0), Inches(6.46), Inches(11.333), Inches(0.35))
    tf_s7 = tb_s7.text_frame
    tf_s7.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf_s7.margin_left = tf_s7.margin_top = tf_s7.margin_right = tf_s7.margin_bottom = 0
    p_s7 = tf_s7.paragraphs[0]
    p_s7.text = "COMFORT COMPLIANCE PROXY: 89.6% of occupied hours strictly within 22.0°C–26.0°C temperature target  |  Zero extreme comfort violations"
    p_s7.font.size = Pt(8.8)
    p_s7.font.bold = True
    p_s7.font.color.rgb = TEXT_MUTED
    p_s7.font.name = 'Segoe UI'

    add_footer(s7, 7)

    # =========================================================================
    # SLIDE 8: INNOVATION
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8)
    add_header(s8, "What Makes EcoSense AI Different?", "Innovation & Key Differentiators")

    pillars8 = [
        ("1. TRI-FACTOR BALANCE", PRIMARY_EMERALD, "Energy + Comfort + Peak", 
         "Unlike conventional energy tools that optimize kWh in isolation, EcoSense simultaneously balances energy conservation, occupant comfort (22°C–26°C), and coincident peak demand penalties."),
        
        ("2. PREDICTIVE + ACTIONABLE", ACCENT_CYAN, "Forecast-Driven", 
         "Moves beyond backward-looking submeter dashboards. Anticipates building cooling load 24 hours ahead using Random Forest and triggers automated pre-cooling before peak tariffs hit."),
        
        ("3. ZONE-AWARE ADAPTATION", ACCENT_PURPLE, "Spatial Intelligence", 
         "Applies independent setback and ventilation logic across distinct zone archetypes (Lobby, Meeting Room, Open Office, Cafeteria) based on real-time occupancy rather than whole-building averages."),
        
        ("4. SCENARIO AUDITING", ACCENT_AMBER, "Decision Sandbox", 
         "Empowers managers to compare 4 progressive tiers of building intelligence:\n• A: Fixed Baseline\n• B: Occupancy Control\n• C: Occupancy + Forecast\n• D: Full EcoSense"),
        
        ("5. SCIENTIFIC HONESTY", ACCENT_BLUE, "Auditable Assumptions", 
         "No black boxes. Every calculation explicitly documents data provenance (SIMULATED DATA, MODEL PREDICTION), tariff rates (₹8.50/kWh), and grid emission factors (0.82 kg/kWh).")
    ]

    card_w8 = Inches(2.23)
    gap8 = Inches(0.14)
    top8 = Inches(1.4)
    h8 = Inches(4.7)

    for idx, (title, color, sub, body) in enumerate(pillars8):
        x = Inches(0.8) + idx * (card_w8 + gap8)
        create_card_shape(s8, x, top8, card_w8, h8, bg=CARD_BG, border=color, border_width=1.2)

        tb = s8.shapes.add_textbox(x + Inches(0.16), top8 + Inches(0.2), card_w8 - Inches(0.32), h8 - Inches(0.4))
        tf = tb.text_frame
        tf.vertical_anchor = MSO_ANCHOR.TOP
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p1 = tf.paragraphs[0]
        p1.text = title
        p1.font.size = Pt(11)
        p1.font.bold = True
        p1.font.color.rgb = color
        p1.font.name = 'Segoe UI'
        p1.space_after = Pt(2)

        p2 = tf.add_paragraph()
        p2.text = sub.upper()
        p2.font.size = Pt(8.5)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_WHITE
        p2.font.name = 'Segoe UI'
        p2.space_after = Pt(8)

        p3 = tf.add_paragraph()
        p3.text = body
        p3.font.size = Pt(8.8)
        p3.font.color.rgb = TEXT_MUTED
        p3.font.name = 'Segoe UI'

    # Bottom summary box
    create_card_shape(s8, Inches(0.8), Inches(6.28), Inches(11.733), Inches(0.55), bg=CARD_BG_ALT, border=CARD_BORDER)
    tb_s8b = s8.shapes.add_textbox(Inches(1.0), Inches(6.36), Inches(11.333), Inches(0.4))
    tf_s8b = tb_s8b.text_frame
    tf_s8b.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf_s8b.margin_left = tf_s8b.margin_top = tf_s8b.margin_right = tf_s8b.margin_bottom = 0
    p_s8b = tf_s8b.paragraphs[0]
    p_s8b.alignment = PP_ALIGN.CENTER
    p_s8b.text = "COMPETITIVE EDGE: EcoSense bridges the gap between passive IoT monitoring dashboards and costly full BMS overhauls by providing an intelligent software supervisory layer."
    p_s8b.font.size = Pt(9.5)
    p_s8b.font.bold = True
    p_s8b.font.color.rgb = PRIMARY_EMERALD
    p_s8b.font.name = 'Segoe UI'

    add_footer(s8, 8)

    # =========================================================================
    # SLIDE 9: EXPECTED IMPACT & ROADMAP
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9)
    add_header(s9, "Expected Impact & Path to Real Buildings", "Value Proposition & Implementation Roadmap")

    col_w9 = Inches(5.7)
    col_h9 = Inches(4.7)

    # LEFT COLUMN: Expected Impact Areas
    create_card_shape(s9, Inches(0.8), Inches(1.4), col_w9, col_h9, bg=CARD_BG, border=PRIMARY_EMERALD, border_width=1.2)
    tb_imp = s9.shapes.add_textbox(Inches(1.05), Inches(1.6), col_w9 - Inches(0.5), col_h9 - Inches(0.4))
    tf_imp = tb_imp.text_frame
    tf_imp.vertical_anchor = MSO_ANCHOR.TOP
    tf_imp.word_wrap = True
    tf_imp.margin_left = tf_imp.margin_top = tf_imp.margin_right = tf_imp.margin_bottom = 0

    p_ih = tf_imp.paragraphs[0]
    p_ih.text = "EXPECTED IMPACT AREAS"
    p_ih.font.size = Pt(13)
    p_ih.font.bold = True
    p_ih.font.color.rgb = PRIMARY_EMERALD
    p_ih.font.name = 'Segoe UI'
    p_ih.space_after = Pt(8)

    impact_points = [
        ("Energy Efficiency:", "Reduce unnecessary HVAC, lighting, and auxiliary power consumption by 20–28% in commercial spaces through occupancy setbacks."),
        ("Peak Demand Management:", "Clip coincident peak demand by 15–25% via predictive pre-cooling, avoiding expensive utility maximum demand charges."),
        ("Occupant Comfort Assurance:", "Maintain steady thermal proxy adherence (22°C–26°C), avoiding overcooling and eliminating occupant discomfort complaints."),
        ("Operational Productivity:", "Deliver high-confidence, actionable advisories to facility managers rather than overwhelming them with raw, uncurated sensor streams.")
    ]

    for title, desc in impact_points:
        p_pt = tf_imp.add_paragraph()
        p_pt.text = f"• {title} {desc}"
        p_pt.font.size = Pt(9.2)
        p_pt.font.color.rgb = TEXT_MUTED
        p_pt.font.name = 'Segoe UI'
        p_pt.space_after = Pt(8)

    # RIGHT COLUMN: Phased Implementation Roadmap
    create_card_shape(s9, Inches(6.833), Inches(1.4), col_w9, col_h9, bg=CARD_BG, border=ACCENT_CYAN, border_width=1.2)
    tb_rd = s9.shapes.add_textbox(Inches(7.083), Inches(1.6), col_w9 - Inches(0.5), col_h9 - Inches(0.4))
    tf_rd = tb_rd.text_frame
    tf_rd.vertical_anchor = MSO_ANCHOR.TOP
    tf_rd.word_wrap = True
    tf_rd.margin_left = tf_rd.margin_top = tf_rd.margin_right = tf_rd.margin_bottom = 0

    p_rh = tf_rd.paragraphs[0]
    p_rh.text = "IMPLEMENTATION ROADMAP"
    p_rh.font.size = Pt(13)
    p_rh.font.bold = True
    p_rh.font.color.rgb = ACCENT_CYAN
    p_rh.font.name = 'Segoe UI'
    p_rh.space_after = Pt(8)

    roadmap_steps = [
        ("PHASE 1 — CURRENT PROTOTYPE (COMPLETED)", "Validated software simulation engine, Scikit-Learn 24h demand forecasting, multi-objective optimization, and Next.js / FastAPI decision cockpit."),
        ("PHASE 2 — PILOT HARDWARE INTEGRATION", "Deploy wireless IoT sensor overlays (LoRaWAN / Zigbee headcount occupancy, temperature, IAQ) and connect smart main-panel energy sub-meters."),
        ("PHASE 3 — BMS SUPERVISORY INTEGRATION", "Interface via standard BACnet/IP and Modbus protocols to automate thermostat setpoints and lighting relays with human-in-the-loop override."),
        ("PHASE 4 — CONTINUOUS & GRID-INTERACTIVE (GEB)", "Continuous model adaptation from real building telemetry, multi-facility portfolio aggregation, and automated demand response (ADR) grid participation.")
    ]

    for title, desc in roadmap_steps:
        p_st = tf_rd.add_paragraph()
        p_st.text = f"• {title}\n  {desc}"
        p_st.font.size = Pt(8.8)
        p_st.font.color.rgb = TEXT_MUTED
        p_st.font.name = 'Segoe UI'
        p_st.space_after = Pt(6)

    # Bottom Callout Box
    create_card_shape(s9, Inches(0.8), Inches(6.28), Inches(11.733), Inches(0.55), bg=CARD_BG_ALT, border=CARD_BORDER)
    tb_s9b = s9.shapes.add_textbox(Inches(1.0), Inches(6.36), Inches(11.333), Inches(0.4))
    tf_s9b = tb_s9b.text_frame
    tf_s9b.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf_s9b.margin_left = tf_s9b.margin_top = tf_s9b.margin_right = tf_s9b.margin_bottom = 0
    p_s9b = tf_s9b.paragraphs[0]
    p_s9b.text = "DISTINCTION: Phase 1 (Simulation Prototype) is fully functional and runnable today. Phases 2–4 represent the technical deployment path to real-world commercial buildings."
    p_s9b.font.size = Pt(9.5)
    p_s9b.font.bold = True
    p_s9b.font.color.rgb = TEXT_WHITE
    p_s9b.font.name = 'Segoe UI'

    add_footer(s9, 9)

    # =========================================================================
    # SLIDE 10: TEAM / CLOSING
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_background(s10)

    # Top Pill
    s10_pill = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.8), Inches(5.0), Inches(0.38))
    s10_pill.fill.solid()
    s10_pill.fill.fore_color.rgb = PRIMARY_EMERALD
    s10_pill.line.fill.background()
    s10_ptf = s10_pill.text_frame
    s10_ptf.vertical_anchor = MSO_ANCHOR.MIDDLE
    s10_pp = s10_ptf.paragraphs[0]
    s10_pp.alignment = PP_ALIGN.CENTER
    s10_pp.text = "YUVA YODHA ENERGY TECH HACKATHON 2026  •  SMART BUILDINGS"
    s10_pp.font.size = Pt(9)
    s10_pp.font.bold = True
    s10_pp.font.color.rgb = RGBColor(10, 15, 29)
    s10_pp.font.name = 'Segoe UI'

    # Title & Subtitle
    t_box10 = s10.shapes.add_textbox(Inches(0.8), Inches(1.3), Inches(11.733), Inches(1.1))
    tf10 = t_box10.text_frame
    tf10.margin_left = tf10.margin_top = tf10.margin_right = tf10.margin_bottom = 0
    p10 = tf10.paragraphs[0]
    p10.text = "Building Smarter, Not Just Using Less"
    p10.font.size = Pt(36)
    p10.font.bold = True
    p10.font.color.rgb = TEXT_WHITE
    p10.font.name = 'Segoe UI'

    p10_sub = tf10.add_paragraph()
    p10_sub.text = "EcoSense AI  •  Intelligent Building Energy Optimizer"
    p10_sub.font.size = Pt(20)
    p10_sub.font.bold = True
    p10_sub.font.color.rgb = PRIMARY_EMERALD
    p10_sub.font.name = 'Segoe UI'

    # Quote Box
    create_card_shape(s10, Inches(0.8), Inches(2.6), Inches(11.733), Inches(1.1), bg=CARD_BG_ALT, border=PRIMARY_EMERALD, border_width=1.2)
    tb_q = s10.shapes.add_textbox(Inches(1.1), Inches(2.72), Inches(11.133), Inches(0.85))
    tf_q = tb_q.text_frame
    tf_q.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf_q.margin_left = tf_q.margin_top = tf_q.margin_right = tf_q.margin_bottom = 0
    p_q = tf_q.paragraphs[0]
    p_q.alignment = PP_ALIGN.CENTER
    p_q.text = "\"Turning building data into smarter energy decisions — balancing efficiency, comfort, and peak demand.\""
    p_q.font.size = Pt(16)
    p_q.font.bold = True
    p_q.font.color.rgb = TEXT_WHITE
    p_q.font.name = 'Segoe UI'

    # Lower Grid: Team Placeholder (Left) & Prototype Verification (Right)
    col_w10 = Inches(5.7)
    col_h10 = Inches(2.7)

    create_card_shape(s10, Inches(0.8), Inches(3.95), col_w10, col_h10, bg=CARD_BG, border=ACCENT_CYAN, border_width=1.2)
    tb_tc = s10.shapes.add_textbox(Inches(1.05), Inches(4.15), col_w10 - Inches(0.5), col_h10 - Inches(0.4))
    tf_tc = tb_tc.text_frame
    tf_tc.vertical_anchor = MSO_ANCHOR.TOP
    tf_tc.word_wrap = True
    tf_tc.margin_left = tf_tc.margin_top = tf_tc.margin_right = tf_tc.margin_bottom = 0

    p_tc1 = tf_tc.paragraphs[0]
    p_tc1.text = "TEAM MEMBERS"
    p_tc1.font.size = Pt(13)
    p_tc1.font.bold = True
    p_tc1.font.color.rgb = ACCENT_CYAN
    p_tc1.font.name = 'Segoe UI'
    p_tc1.space_after = Pt(4)

    p_tc2 = tf_tc.add_paragraph()
    p_tc2.text = "[Add team member names]"
    p_tc2.font.size = Pt(14)
    p_tc2.font.bold = True
    p_tc2.font.color.rgb = TEXT_WHITE
    p_tc2.font.name = 'Segoe UI'
    p_tc2.space_after = Pt(8)

    p_tc3 = tf_tc.add_paragraph()
    p_tc3.text = "Roles & Focus:\n• Software & Data Engineering  • Machine Learning & Optimization\n• Building Systems Modeling  • Full-Stack Cockpit UI"
    p_tc3.font.size = Pt(9.5)
    p_tc3.font.color.rgb = TEXT_MUTED
    p_tc3.font.name = 'Segoe UI'

    create_card_shape(s10, Inches(6.833), Inches(3.95), col_w10, col_h10, bg=CARD_BG, border=ACCENT_AMBER, border_width=1.2)
    tb_sc = s10.shapes.add_textbox(Inches(7.083), Inches(4.15), col_w10 - Inches(0.5), col_h10 - Inches(0.4))
    tf_sc = tb_sc.text_frame
    tf_sc.vertical_anchor = MSO_ANCHOR.TOP
    tf_sc.word_wrap = True
    tf_sc.margin_left = tf_sc.margin_top = tf_sc.margin_right = tf_sc.margin_bottom = 0

    p_sc1 = tf_sc.paragraphs[0]
    p_sc1.text = "PROTOTYPE VERIFICATION & SUMMARY"
    p_sc1.font.size = Pt(13)
    p_sc1.font.bold = True
    p_sc1.font.color.rgb = ACCENT_AMBER
    p_sc1.font.name = 'Segoe UI'
    p_sc1.space_after = Pt(6)

    status_items = [
        "Current Prototype: Software-based simulation & decision-support platform",
        "Verified Architecture: FastAPI async backend + Next.js interactive cockpit",
        "Scientific Honesty: All simulation figures explicitly labeled with zero fabricated claims",
        "Deterministic PRNG Seed: #42  |  Test Suite: 23/23 tests passed (100%)"
    ]

    for item in status_items:
        psi = tf_sc.add_paragraph()
        psi.text = f"• {item}"
        psi.font.size = Pt(9.2)
        psi.font.color.rgb = TEXT_MUTED
        psi.font.name = 'Segoe UI'
        psi.space_after = Pt(3.5)

    add_footer(s10, 10)

    # Save presentation
    output_pptx = "EcoSense_AI_Yuva_Yodha_Hackathon_2026.pptx"
    prs.save(output_pptx)
    print(f"Presentation saved successfully as '{output_pptx}' with {len(prs.slides)} slides.")

if __name__ == "__main__":
    create_deck()
