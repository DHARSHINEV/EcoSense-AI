import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def build_presentation():
    prs = Presentation()
    # 16:9 widescreen layout
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Professional Dark Theme Palette
    BG_COLOR = RGBColor(10, 15, 29)            # #0A0F1D Deep Navy Slate
    CARD_BG = RGBColor(17, 24, 39)            # #111827 Dark Slate Card
    CARD_BORDER = RGBColor(30, 41, 59)        # #1E293B Border
    CARD_BORDER_ACCENT = RGBColor(51, 65, 85) # #334155
    CARD_BG_ALT = RGBColor(15, 23, 42)        # #0F172A Alt Card
    
    PRIMARY_EMERALD = RGBColor(16, 185, 129)  # #10B981 Emerald Green (Energy)
    ACCENT_CYAN = RGBColor(6, 182, 212)       # #06B6D4 Cyan (Tech/Predictive)
    ACCENT_AMBER = RGBColor(245, 158, 11)     # #F59E0B Amber (Cost)
    ACCENT_BLUE = RGBColor(59, 130, 246)      # #3B82F6 Blue
    
    TEXT_WHITE = RGBColor(248, 250, 252)      # #F8FAFC Pure/White
    TEXT_MUTED = RGBColor(148, 163, 184)      # #94A3B8 Muted Light
    TEXT_DIM = RGBColor(100, 116, 139)        # #64748B Dim Slate

    def set_slide_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_COLOR
        bg.line.fill.background()
        return bg

    def add_header(slide, title_text, category_text, badge_text="SMART BUILDINGS TRACK", badge_color=ACCENT_CYAN):
        # Category Tracker
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.42), Inches(8.5), Inches(0.28))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        tf_cat.margin_left = tf_cat.margin_top = tf_cat.margin_right = tf_cat.margin_bottom = 0
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = ACCENT_CYAN
        p_cat.font.name = 'Segoe UI'

        # Main Slide Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.70), Inches(8.5), Inches(0.55))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        tf_title.margin_left = tf_title.margin_top = tf_title.margin_right = tf_title.margin_bottom = 0
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_WHITE
        p_title.font.name = 'Segoe UI'

        # Right Header Badge
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

    def create_card(slide, left, top, width, height, bg=CARD_BG, border=CARD_BORDER, border_width=1.0):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg
        card.line.color.rgb = border
        card.line.width = Pt(border_width)
        return card

    # =========================================================================
    # SLIDE 1: COVER
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide1)

    cat_box = slide1.shapes.add_textbox(Inches(0.8), Inches(0.55), Inches(9.0), Inches(0.3))
    tf_c = cat_box.text_frame
    tf_c.margin_left = tf_c.margin_top = tf_c.margin_right = tf_c.margin_bottom = 0
    p_c = tf_c.paragraphs[0]
    p_c.text = "YUVA YODHA ENERGY TECH HACKATHON 2026 • CHALLENGE: SMART BUILDINGS"
    p_c.font.size = Pt(10)
    p_c.font.bold = True
    p_c.font.color.rgb = ACCENT_CYAN
    p_c.font.name = 'Segoe UI'

    b1 = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.533), Inches(0.55), Inches(3.0), Inches(0.42))
    b1.fill.solid()
    b1.fill.fore_color.rgb = RGBColor(15, 23, 42)
    b1.line.color.rgb = PRIMARY_EMERALD
    b1.line.width = Pt(1.2)
    tf_b1 = b1.text_frame
    tf_b1.vertical_anchor = MSO_ANCHOR.MIDDLE
    p_b1 = tf_b1.paragraphs[0]
    p_b1.alignment = PP_ALIGN.CENTER
    p_b1.text = "PROTOTYPE PITCH DECK"
    p_b1.font.size = Pt(9)
    p_b1.font.bold = True
    p_b1.font.color.rgb = PRIMARY_EMERALD
    p_b1.font.name = 'Segoe UI'

    title_box = slide1.shapes.add_textbox(Inches(0.8), Inches(1.15), Inches(11.733), Inches(0.95))
    tf_t = title_box.text_frame
    tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
    p_t = tf_t.paragraphs[0]
    p_t.text = "ECOSENSE AI"
    p_t.font.size = Pt(46)
    p_t.font.bold = True
    p_t.font.color.rgb = TEXT_WHITE
    p_t.font.name = 'Segoe UI'

    sub_box = slide1.shapes.add_textbox(Inches(0.8), Inches(2.15), Inches(11.733), Inches(0.45))
    tf_s = sub_box.text_frame
    tf_s.margin_left = tf_s.margin_top = tf_s.margin_right = tf_s.margin_bottom = 0
    p_s = tf_s.paragraphs[0]
    p_s.text = "Intelligent Building Energy Optimizer"
    p_s.font.size = Pt(22)
    p_s.font.bold = True
    p_s.font.color.rgb = PRIMARY_EMERALD
    p_s.font.name = 'Segoe UI'

    pill_data = [
        "AI-Powered Energy Efficiency",
        "Comfort-Aware Optimization",
        "Peak-Demand Management"
    ]
    pill_w = Inches(3.7)
    for i, pill in enumerate(pill_data):
        px = Inches(0.8) + i * Inches(4.0)
        p_card = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, px, Inches(2.8), pill_w, Inches(0.48))
        p_card.fill.solid()
        p_card.fill.fore_color.rgb = CARD_BG
        p_card.line.color.rgb = CARD_BORDER
        p_card.line.width = Pt(1.0)
        tf_pc = p_card.text_frame
        tf_pc.vertical_anchor = MSO_ANCHOR.MIDDLE
        p_pc = tf_pc.paragraphs[0]
        p_pc.alignment = PP_ALIGN.CENTER
        p_pc.text = pill
        p_pc.font.size = Pt(11)
        p_pc.font.bold = True
        p_pc.font.color.rgb = ACCENT_CYAN
        p_pc.font.name = 'Segoe UI'

    flow_bg = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(3.55), Inches(11.733), Inches(1.85))
    flow_bg.fill.solid()
    flow_bg.fill.fore_color.rgb = RGBColor(12, 19, 36)
    flow_bg.line.color.rgb = CARD_BORDER
    flow_bg.line.width = Pt(1.2)

    flow_nodes = [
        ("BUILDING", "Commercial Spaces &\nActive Thermal Zones", ACCENT_BLUE),
        ("SENSORS / DATA", "Occupancy, Temperature,\nIAQ & Power Telemetry", ACCENT_CYAN),
        ("AI ENGINE", "Random Forest 24h Ahead\nDemand Forecasting", PRIMARY_EMERALD),
        ("OPTIMIZED CONTROL", "Peak Shaving, Comfort Guard\n& Dynamic Setbacks", ACCENT_AMBER)
    ]
    node_w = Inches(2.4)
    for i, (ntitle, ndesc, ncolor) in enumerate(flow_nodes):
        nx = Inches(1.1) + i * Inches(2.9)
        nbox = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, nx, Inches(3.78), node_w, Inches(1.4))
        nbox.fill.solid()
        nbox.fill.fore_color.rgb = CARD_BG
        nbox.line.color.rgb = ncolor
        nbox.line.width = Pt(1.5)
        tf_nb = nbox.text_frame
        tf_nb.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf_nb.margin_top = tf_nb.margin_bottom = Inches(0.08)
        
        p1 = tf_nb.paragraphs[0]
        p1.alignment = PP_ALIGN.CENTER
        p1.text = ntitle
        p1.font.size = Pt(12)
        p1.font.bold = True
        p1.font.color.rgb = ncolor
        p1.font.name = 'Segoe UI'
        
        p2 = tf_nb.add_paragraph()
        p2.alignment = PP_ALIGN.CENTER
        p2.text = ndesc
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = TEXT_MUTED
        p2.font.name = 'Segoe UI'

        if i < 3:
            arrow_x = nx + node_w + Inches(0.08)
            abox = slide1.shapes.add_textbox(arrow_x, Inches(4.2), Inches(0.35), Inches(0.5))
            tf_a = abox.text_frame
            tf_a.margin_left = tf_a.margin_top = tf_a.margin_right = tf_a.margin_bottom = 0
            pa = tf_a.paragraphs[0]
            pa.text = "➔"
            pa.font.size = Pt(18)
            pa.font.bold = True
            pa.font.color.rgb = PRIMARY_EMERALD
            pa.alignment = PP_ALIGN.CENTER

    team_card = create_card(slide1, Inches(0.8), Inches(5.65), Inches(6.5), Inches(1.15))
    tf_tc = team_card.text_frame
    tf_tc.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf_tc.margin_left = Inches(0.3)
    p_t1 = tf_tc.paragraphs[0]
    p_t1.text = "TEAM NOVA  •  Yuva Yodha Energy Tech Hackathon 2026"
    p_t1.font.size = Pt(12)
    p_t1.font.bold = True
    p_t1.font.color.rgb = TEXT_WHITE
    p_t1.font.name = 'Segoe UI'

    p_t2 = tf_tc.add_paragraph()
    p_t2.text = "Team Lead: Dharshine V  |  vdharshine19@gmail.com"
    p_t2.font.size = Pt(11)
    p_t2.font.color.rgb = ACCENT_CYAN
    p_t2.font.name = 'Segoe UI'

    status_card = create_card(slide1, Inches(7.5), Inches(5.65), Inches(5.033), Inches(1.15))
    tf_sc = status_card.text_frame
    tf_sc.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf_sc.margin_left = Inches(0.3)
    p_s1 = tf_sc.paragraphs[0]
    p_s1.text = "CURRENT STATUS"
    p_s1.font.size = Pt(10)
    p_s1.font.bold = True
    p_s1.font.color.rgb = PRIMARY_EMERALD
    p_s1.font.name = 'Segoe UI'

    p_s2 = tf_sc.add_paragraph()
    p_s2.text = "Functional software simulation and energy decision-support prototype"
    p_s2.font.size = Pt(10)
    p_s2.font.color.rgb = TEXT_MUTED
    p_s2.font.name = 'Segoe UI'

    add_footer(slide1, 1)

    # =========================================================================
    # SLIDE 2: THE PROBLEM
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide2)
    add_header(slide2, "THE PROBLEM", "THE COMMERCIAL BUILDING CHALLENGE", "PROBLEM STATEMENT", RGBColor(239, 68, 68))

    hl_card = create_card(slide2, Inches(0.8), Inches(1.35), Inches(11.733), Inches(0.72), bg=RGBColor(15, 23, 42), border=RGBColor(40, 50, 70))
    tf_hl = hl_card.text_frame
    tf_hl.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf_hl.margin_left = Inches(0.3)
    p_hl = tf_hl.paragraphs[0]
    p_hl.text = "BUILDINGS OFTEN RUN ON FIXED SCHEDULES — BUT BUILDING CONDITIONS KEEP CHANGING."
    p_hl.font.size = Pt(15.5)
    p_hl.font.bold = True
    p_hl.font.color.rgb = TEXT_WHITE
    p_hl.font.name = 'Segoe UI'

    vstrip = create_card(slide2, Inches(0.8), Inches(2.2), Inches(11.733), Inches(0.9), bg=RGBColor(12, 19, 36), border=CARD_BORDER)
    chain = [
        ("FIXED SCHEDULE", ACCENT_BLUE),
        ("VACANT / PARTIAL SPACES", ACCENT_CYAN),
        ("UNNECESSARY HVAC + LIGHTING", ACCENT_AMBER),
        ("ENERGY WASTE + PEAK SPIKES", RGBColor(239, 68, 68))
    ]
    for i, (c_text, c_col) in enumerate(chain):
        cx = Inches(1.0) + i * Inches(2.85)
        cbox = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, Inches(2.32), Inches(2.35), Inches(0.65))
        cbox.fill.solid()
        cbox.fill.fore_color.rgb = CARD_BG
        cbox.line.color.rgb = c_col
        cbox.line.width = Pt(1.2)
        tf_cb = cbox.text_frame
        tf_cb.vertical_anchor = MSO_ANCHOR.MIDDLE
        p_cb = tf_cb.paragraphs[0]
        p_cb.alignment = PP_ALIGN.CENTER
        p_cb.text = c_text
        p_cb.font.size = Pt(9.5)
        p_cb.font.bold = True
        p_cb.font.color.rgb = c_col
        p_cb.font.name = 'Segoe UI'

        if i < 3:
            ax = cx + Inches(2.35) + Inches(0.08)
            arr = slide2.shapes.add_textbox(ax, Inches(2.4), Inches(0.35), Inches(0.4))
            tf_a = arr.text_frame
            tf_a.margin_left = tf_a.margin_top = tf_a.margin_right = tf_a.margin_bottom = 0
            pa = tf_a.paragraphs[0]
            pa.text = "➔"
            pa.font.size = Pt(14)
            pa.font.bold = True
            pa.font.color.rgb = PRIMARY_EMERALD

    card_w = Inches(3.73)
    p_data = [
        ("01", "ENERGY WASTE", "Unnecessary HVAC & lighting operation", [
            "HVAC and lighting run full blast regardless of real headcount",
            "Meeting rooms and empty zones conditioned on rigid timers",
            "Avoidable baseload drives significant continuous energy loss"
        ], PRIMARY_EMERALD),
        ("02", "PEAK DEMAND", "Simultaneous loads create demand spikes", [
            "Midday outdoor heat combined with occupancy spikes grid draw",
            "Commercial utilities levy steep Maximum Demand charges",
            "Unmanaged coincidence creates expensive electrical spikes"
        ], ACCENT_CYAN),
        ("03", "COMFORT MISMATCH", "Static settings fail to adapt to occupancy", [
            "Thermostats hold a flat setpoint regardless of zone density",
            "Leads to simultaneous overcooling in empty rooms & stuffiness",
            "Occupant dissatisfaction leads to manual setpoint tampering"
        ], ACCENT_BLUE)
    ]

    for i, (num, ptitle, psub, bullets, pcolor) in enumerate(p_data):
        px = Inches(0.8) + i * Inches(4.0)
        c = create_card(slide2, px, Inches(3.25), card_w, Inches(2.8))
        tf = c.text_frame
        tf.margin_left = tf.margin_right = Inches(0.28)
        tf.margin_top = Inches(0.25)
        
        p0 = tf.paragraphs[0]
        p0.text = f"{num}  |  {ptitle}"
        p0.font.size = Pt(13)
        p0.font.bold = True
        p0.font.color.rgb = pcolor
        p0.font.name = 'Segoe UI'

        p1 = tf.add_paragraph()
        p1.text = psub
        p1.font.size = Pt(10.5)
        p1.font.bold = True
        p1.font.color.rgb = TEXT_WHITE
        p1.font.name = 'Segoe UI'

        for b in bullets:
            pb = tf.add_paragraph()
            pb.text = f"•  {b}"
            pb.font.size = Pt(9.5)
            pb.font.color.rgb = TEXT_MUTED
            pb.font.name = 'Segoe UI'

    callout = create_card(slide2, Inches(0.8), Inches(6.2), Inches(11.733), Inches(0.65), bg=RGBColor(12, 19, 36), border=CARD_BORDER)
    tf_call = callout.text_frame
    tf_call.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf_call.margin_left = Inches(0.3)
    p_call = tf_call.paragraphs[0]
    p_call.alignment = PP_ALIGN.CENTER
    p_call.text = "\"Building managers need smarter, data-driven operating decisions.\""
    p_call.font.size = Pt(13.5)
    p_call.font.bold = True
    p_call.font.italic = True
    p_call.font.color.rgb = PRIMARY_EMERALD
    p_call.font.name = 'Segoe UI'

    add_footer(slide2, 2)

    # =========================================================================
    # SLIDE 3: OUR SOLUTION
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide3)
    add_header(slide3, "OUR SOLUTION", "INTELLIGENT ENERGY PLATFORM", "SOLUTION OVERVIEW", PRIMARY_EMERALD)

    stmt_card = create_card(slide3, Inches(0.8), Inches(1.35), Inches(11.733), Inches(0.85), bg=RGBColor(15, 23, 42), border=RGBColor(16, 185, 129))
    tf_st = stmt_card.text_frame
    tf_st.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf_st.margin_left = Inches(0.3)
    p_st = tf_st.paragraphs[0]
    p_st.alignment = PP_ALIGN.CENTER
    p_st.text = "ECOSENSE AI TURNS BUILDING DATA INTO ACTIONABLE ENERGY DECISIONS."
    p_st.font.size = Pt(17)
    p_st.font.bold = True
    p_st.font.color.rgb = TEXT_WHITE
    p_st.font.name = 'Segoe UI'

    steps = [
        ("1", "SENSE", "Occupancy + environmental + energy data", [
            "Zone occupancy (headcount)",
            "Indoor temp (°C) & humidity",
            "HVAC, lighting, & plug power"
        ], ACCENT_BLUE),
        ("2", "PREDICT", "24-hour demand forecast", [
            "Random Forest regression",
            "Diurnal pattern modeling",
            "Empirical prediction bands"
        ], ACCENT_CYAN),
        ("3", "OPTIMIZE", "Energy + comfort + peak demand", [
            "Simultaneous 3-way balance",
            "Strict 22°C–26°C comfort target",
            "Peak limit clipping (≤175 kW)"
        ], PRIMARY_EMERALD),
        ("4", "RECOMMEND", "Actionable operating suggestions", [
            "Dynamic occupancy setbacks",
            "Daylight harvesting dimming",
            "Thermal pre-cooling triggers"
        ], ACCENT_AMBER),
        ("5", "MEASURE", "Baseline vs optimized performance", [
            "Transparent savings analytics",
            "Real-time kWh & ₹ tracking",
            "Continuous comfort logging"
        ], RGBColor(168, 85, 247))
    ]

    card_w5 = Inches(2.23)
    gap5 = Inches(0.14)
    for i, (num, stitle, sline, sbullets, scolor) in enumerate(steps):
        sx = Inches(0.8) + i * (card_w5 + gap5)
        c5 = create_card(slide3, sx, Inches(2.4), card_w5, Inches(3.6), border=scolor, border_width=1.2)
        tf5 = c5.text_frame
        tf5.margin_left = tf5.margin_right = Inches(0.18)
        tf5.margin_top = Inches(0.2)
        
        p_num = tf5.paragraphs[0]
        p_num.text = f"STEP {num}"
        p_num.font.size = Pt(10)
        p_num.font.bold = True
        p_num.font.color.rgb = scolor
        p_num.font.name = 'Segoe UI'

        p_tit = tf5.add_paragraph()
        p_tit.text = stitle
        p_tit.font.size = Pt(15)
        p_tit.font.bold = True
        p_tit.font.color.rgb = TEXT_WHITE
        p_tit.font.name = 'Segoe UI'

        p_ln = tf5.add_paragraph()
        p_ln.text = sline
        p_ln.font.size = Pt(9.5)
        p_ln.font.bold = True
        p_ln.font.color.rgb = scolor
        p_ln.font.name = 'Segoe UI'

        for sb in sbullets:
            psb = tf5.add_paragraph()
            psb.text = f"• {sb}"
            psb.font.size = Pt(8.5)
            psb.font.color.rgb = TEXT_MUTED
            psb.font.name = 'Segoe UI'

    bot_card = create_card(slide3, Inches(0.8), Inches(6.2), Inches(11.733), Inches(0.65), bg=RGBColor(12, 19, 36), border=CARD_BORDER)
    tf_bc = bot_card.text_frame
    tf_bc.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf_bc.margin_left = Inches(0.3)
    p_bc = tf_bc.paragraphs[0]
    p_bc.alignment = PP_ALIGN.CENTER
    p_bc.text = "CURRENT PROTOTYPE: Software simulation + decision support"
    p_bc.font.size = Pt(12)
    p_bc.font.bold = True
    p_bc.font.color.rgb = PRIMARY_EMERALD
    p_bc.font.name = 'Segoe UI'

    add_footer(slide3, 3)

    # =========================================================================
    # SLIDE 4: HOW ECOSENSE AI WORKS (FIXED ALIGNMENT)
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide4)
    add_header(slide4, "HOW ECOSENSE AI WORKS", "SYSTEM ARCHITECTURE & PIPELINE", "4-LAYER STACK", ACCENT_CYAN)

    sub_c4 = create_card(slide4, Inches(0.8), Inches(1.35), Inches(11.733), Inches(0.52), bg=RGBColor(15, 23, 42), border=CARD_BORDER)
    tf_s4 = sub_c4.text_frame
    tf_s4.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf_s4.margin_left = Inches(0.3)
    p_s4 = tf_s4.paragraphs[0]
    p_s4.alignment = PP_ALIGN.CENTER
    p_s4.text = "From raw telemetry → prediction → optimized decision"
    p_s4.font.size = Pt(13)
    p_s4.font.bold = True
    p_s4.font.color.rgb = ACCENT_CYAN
    p_s4.font.name = 'Segoe UI'

    layers = [
        ("LAYER 1: BUILDING DATA", "Occupancy • Temperature • Humidity • IAQ • HVAC • Lighting • Plug Loads", 
         "Collects multi-zone telemetry across 5 building zones (~2,300 m²) with real-time signal validation.", ACCENT_BLUE),
        ("LAYER 2: AI FORECAST", "Random Forest Regressor • 24-Hour Energy Demand Prediction", 
         "Predicts whole-building power draw (kW) with R² ≈ 0.942 and empirical prediction bands (±1.645 × MAE).", ACCENT_CYAN),
        ("LAYER 3: OPTIMIZATION ENGINE", "Energy + Comfort + Peak Demand Multi-Objective Balance", 
         "Calculates setpoint offsets, shifts loads before peak hours, and enforces 22°C–26°C comfort boundaries.", PRIMARY_EMERALD),
        ("LAYER 4: DECISION COCKPIT", "Interactive Dashboard • Zone Analytics • Scenario Lab • Recommendations", 
         "Delivers explainable operating recommendations to facility managers with quantified kWh and ₹ impact.", ACCENT_AMBER)
    ]

    for i, (ltitle, lcore, ldesc, lcolor) in enumerate(layers):
        ly = Inches(2.02) + i * Inches(1.18)
        lcard = create_card(slide4, Inches(0.8), ly, Inches(11.733), Inches(1.02), border=lcolor, border_width=1.2)
        tf_l = lcard.text_frame
        tf_l.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf_l.margin_left = Inches(0.35)
        tf_l.margin_right = Inches(0.35)

        p_lt = tf_l.paragraphs[0]
        p_lt.alignment = PP_ALIGN.LEFT
        p_lt.text = ltitle
        p_lt.font.size = Pt(11)
        p_lt.font.bold = True
        p_lt.font.color.rgb = lcolor
        p_lt.font.name = 'Segoe UI'

        p_lc = tf_l.add_paragraph()
        p_lc.alignment = PP_ALIGN.LEFT
        p_lc.text = lcore
        p_lc.font.size = Pt(11.5)
        p_lc.font.bold = True
        p_lc.font.color.rgb = TEXT_WHITE
        p_lc.font.name = 'Segoe UI'

        p_ld = tf_l.add_paragraph()
        p_ld.alignment = PP_ALIGN.LEFT
        p_ld.text = ldesc
        p_ld.font.size = Pt(9.5)
        p_ld.font.color.rgb = TEXT_MUTED
        p_ld.font.name = 'Segoe UI'

        if i < 3:
            arr_y = ly + Inches(1.02)
            abox = slide4.shapes.add_textbox(Inches(6.45), arr_y - Inches(0.04), Inches(0.5), Inches(0.22))
            tf_a = abox.text_frame
            tf_a.margin_left = tf_a.margin_top = tf_a.margin_right = tf_a.margin_bottom = 0
            pa = tf_a.paragraphs[0]
            pa.text = "▼"
            pa.font.size = Pt(9)
            pa.font.color.rgb = PRIMARY_EMERALD
            pa.alignment = PP_ALIGN.CENTER

    add_footer(slide4, 4)

    # =========================================================================
    # SLIDE 5: WHAT WE ACTUALLY BUILT (ACTUAL LOADED DASHBOARD SCREENSHOT)
    # =========================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide5)
    add_header(slide5, "WHAT WE ACTUALLY BUILT", "WORKING SOFTWARE PROTOTYPE", "LIVE DEMO READY", PRIMARY_EMERALD)

    sub_c5 = create_card(slide5, Inches(0.8), Inches(1.32), Inches(11.733), Inches(0.48), bg=RGBColor(15, 23, 42), border=CARD_BORDER)
    tf_s5 = sub_c5.text_frame
    tf_s5.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf_s5.margin_left = Inches(0.3)
    p_s5 = tf_s5.paragraphs[0]
    p_s5.text = "A fully functional software simulation prototype & analytics decision support platform."
    p_s5.font.size = Pt(11.5)
    p_s5.font.bold = True
    p_s5.font.color.rgb = PRIMARY_EMERALD
    p_s5.font.name = 'Segoe UI'

    # Left: Actual Screenshot of Dashboard (Use fully rendered v2 screenshot!)
    screen_path = "scratch/slides_assets/screenshot_dashboard_v2.png"
    if not os.path.exists(screen_path):
        screen_path = "scratch/slides_assets/screenshot_dashboard.png"

    if os.path.exists(screen_path):
        frame = create_card(slide5, Inches(0.8), Inches(1.92), Inches(7.3), Inches(4.35), bg=RGBColor(12, 19, 36), border=CARD_BORDER_ACCENT, border_width=1.5)
        slide5.shapes.add_picture(screen_path, Inches(0.9), Inches(2.02), Inches(7.1), Inches(4.15))
    else:
        fb = create_card(slide5, Inches(0.8), Inches(1.92), Inches(7.3), Inches(4.35))
        tf_fb = fb.text_frame
        tf_fb.vertical_anchor = MSO_ANCHOR.MIDDLE
        p_fb = tf_fb.paragraphs[0]
        p_fb.alignment = PP_ALIGN.CENTER
        p_fb.text = "EcoSense AI Dashboard Screenshot"
        p_fb.font.size = Pt(14)
        p_fb.font.color.rgb = TEXT_WHITE

    caps = [
        ("DASHBOARD", "Monitor simulated building performance", "Live 24h demand timeseries, current zone telemetry, and active optimization status.", PRIMARY_EMERALD),
        ("ZONE ANALYTICS", "Inspect 5 building zones", "Granular occupancy, dry-bulb temp, relative humidity, and power breakdown per zone.", ACCENT_CYAN),
        ("SCENARIO LAB", "Compare optimization strategies", "Test Comfort-First, Aggressive Energy, and Peak-Shaving operational trade-offs.", ACCENT_AMBER),
        ("SIMULATION", "Baseline vs EcoSense evaluation", "Side-by-side verification of fixed schedule vs intelligent optimized control.", ACCENT_BLUE)
    ]

    for i, (ctitle, csub, cdesc, ccolor) in enumerate(caps):
        cy = Inches(1.92) + i * Inches(1.08)
        ccard = create_card(slide5, Inches(8.3), cy, Inches(4.233), Inches(0.98), border=ccolor, border_width=1.2)
        tf_c = ccard.text_frame
        tf_c.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf_c.margin_left = Inches(0.2)
        tf_c.margin_right = Inches(0.2)

        p_ct = tf_c.paragraphs[0]
        p_ct.text = ctitle
        p_ct.font.size = Pt(11)
        p_ct.font.bold = True
        p_ct.font.color.rgb = ccolor
        p_ct.font.name = 'Segoe UI'

        p_cs = tf_c.add_paragraph()
        p_cs.text = csub
        p_cs.font.size = Pt(9.5)
        p_cs.font.bold = True
        p_cs.font.color.rgb = TEXT_WHITE
        p_cs.font.name = 'Segoe UI'

        p_cd = tf_c.add_paragraph()
        p_cd.text = cdesc
        p_cd.font.size = Pt(8.5)
        p_cd.font.color.rgb = TEXT_MUTED
        p_cd.font.name = 'Segoe UI'

    tech_card = create_card(slide5, Inches(0.8), Inches(6.38), Inches(11.733), Inches(0.52), bg=RGBColor(12, 19, 36), border=CARD_BORDER)
    tf_tc = tech_card.text_frame
    tf_tc.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf_tc.margin_left = Inches(0.3)
    p_tc = tf_tc.paragraphs[0]
    p_tc.alignment = PP_ALIGN.CENTER
    p_tc.text = "Technology Stack: Next.js (React)  •  FastAPI  •  Python  •  scikit-learn"
    p_tc.font.size = Pt(11)
    p_tc.font.bold = True
    p_tc.font.color.rgb = ACCENT_CYAN
    p_tc.font.name = 'Segoe UI'

    add_footer(slide5, 5)

    # =========================================================================
    # SLIDE 6: THE AI ENGINE
    # =========================================================================
    slide6 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide6)
    add_header(slide6, "THE AI ENGINE", "PREDICTIVE MODELING & MULTI-OBJECTIVE TARGETS", "RANDOM FOREST REGRESSOR", ACCENT_CYAN)

    pipe_card = create_card(slide6, Inches(0.8), Inches(1.35), Inches(6.8), Inches(0.75), bg=RGBColor(15, 23, 42), border=CARD_BORDER)
    tf_p = pipe_card.text_frame
    tf_p.vertical_anchor = MSO_ANCHOR.MIDDLE
    p_p = tf_p.paragraphs[0]
    p_p.alignment = PP_ALIGN.CENTER
    p_p.text = "SIMULATED DATA ➔ FEATURE ENGINEERING ➔ RANDOM FOREST ➔ 24-HR FORECAST ➔ OPTIMIZATION"
    p_p.font.size = Pt(9.5)
    p_p.font.bold = True
    p_p.font.color.rgb = ACCENT_CYAN
    p_p.font.name = 'Segoe UI'

    chart_path = "scratch/slides_assets/slide5_ml_forecast_chart.png"
    if os.path.exists(chart_path):
        slide6.shapes.add_picture(chart_path, Inches(0.8), Inches(2.22), Inches(6.8), Inches(4.1))
    else:
        fc = create_card(slide6, Inches(0.8), Inches(2.22), Inches(6.8), Inches(4.1))
        tf_fc = fc.text_frame
        tf_fc.vertical_anchor = MSO_ANCHOR.MIDDLE
        p_fc = tf_fc.paragraphs[0]
        p_fc.alignment = PP_ALIGN.CENTER
        p_fc.text = "24-Hour Demand Forecast Chart"
        p_fc.font.size = Pt(14)
        p_fc.font.color.rgb = TEXT_WHITE

    m_card = create_card(slide6, Inches(7.8), Inches(1.35), Inches(4.733), Inches(2.7), border=PRIMARY_EMERALD, border_width=1.2)
    tf_m = m_card.text_frame
    tf_m.margin_left = tf_m.margin_right = Inches(0.3)
    tf_m.margin_top = Inches(0.2)

    p_mt = tf_m.paragraphs[0]
    p_mt.text = "MODEL ACCURACY METRICS"
    p_mt.font.size = Pt(11)
    p_mt.font.bold = True
    p_mt.font.color.rgb = PRIMARY_EMERALD
    p_mt.font.name = 'Segoe UI'

    p_r2 = tf_m.add_paragraph()
    p_r2.text = "R² ≈ 0.942  (94.2% Variance Explained)"
    p_r2.font.size = Pt(15)
    p_r2.font.bold = True
    p_r2.font.color.rgb = TEXT_WHITE
    p_r2.font.name = 'Segoe UI'

    p_mae = tf_m.add_paragraph()
    p_mae.text = "MAE ≈ 3.85 kW  (Mean Absolute Error)"
    p_mae.font.size = Pt(13)
    p_mae.font.bold = True
    p_mae.font.color.rgb = ACCENT_CYAN
    p_mae.font.name = 'Segoe UI'

    p_rmse = tf_m.add_paragraph()
    p_rmse.text = "RMSE ≈ 5.21 kW  (Root Mean Squared Error)"
    p_rmse.font.size = Pt(13)
    p_rmse.font.bold = True
    p_rmse.font.color.rgb = ACCENT_CYAN
    p_rmse.font.name = 'Segoe UI'

    p_note = tf_m.add_paragraph()
    p_note.text = "Chronological 80/20 train-test split on 30-day simulated telemetry."
    p_note.font.size = Pt(9)
    p_note.font.italic = True
    p_note.font.color.rgb = TEXT_MUTED
    p_note.font.name = 'Segoe UI'

    opt_card = create_card(slide6, Inches(7.8), Inches(4.2), Inches(4.733), Inches(2.12), border=ACCENT_AMBER, border_width=1.2)
    tf_o = opt_card.text_frame
    tf_o.margin_left = tf_o.margin_right = Inches(0.3)
    tf_o.margin_top = Inches(0.2)

    p_ot = tf_o.paragraphs[0]
    p_ot.text = "OPTIMIZATION TARGETS"
    p_ot.font.size = Pt(11)
    p_ot.font.bold = True
    p_ot.font.color.rgb = ACCENT_AMBER
    p_ot.font.name = 'Segoe UI'

    targets = [
        "Energy: Minimize active power consumption across all zones",
        "Comfort: Maintain 22°C – 26°C occupied indoor temperature",
        "Peak Demand: Keep whole-building draw ≤ 175 kW threshold"
    ]
    for tg in targets:
        ptg = tf_o.add_paragraph()
        ptg.text = f"• {tg}"
        ptg.font.size = Pt(9.5)
        ptg.font.color.rgb = TEXT_MUTED
        ptg.font.name = 'Segoe UI'

    fn_box = slide6.shapes.add_textbox(Inches(0.8), Inches(6.42), Inches(11.733), Inches(0.3))
    tf_fn = fn_box.text_frame
    tf_fn.margin_left = tf_fn.margin_top = tf_fn.margin_right = tf_fn.margin_bottom = 0
    p_fn = tf_fn.paragraphs[0]
    p_fn.text = "Approximate empirical prediction band defined as forecast ± 1.645 × MAE."
    p_fn.font.size = Pt(8.5)
    p_fn.font.italic = True
    p_fn.font.color.rgb = TEXT_DIM
    p_fn.font.name = 'Segoe UI'

    add_footer(slide6, 6)

    # =========================================================================
    # SLIDE 7: WHAT DID THE PROTOTYPE SHOW?
    # =========================================================================
    slide7 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide7)
    add_header(slide7, "WHAT DID THE PROTOTYPE SHOW?", "SIMULATION RESULTS & PERFORMANCE EVALUATION", "SIMULATION RESULT", PRIMARY_EMERALD)

    card_w7 = Inches(3.73)
    
    ecard = create_card(slide7, Inches(0.8), Inches(1.35), card_w7, Inches(1.85), border=PRIMARY_EMERALD, border_width=1.5)
    tf_e = ecard.text_frame
    tf_e.margin_left = tf_e.margin_right = Inches(0.25)
    tf_e.margin_top = Inches(0.18)
    
    pe_num = tf_e.paragraphs[0]
    pe_num.text = "27.8%"
    pe_num.font.size = Pt(36)
    pe_num.font.bold = True
    pe_num.font.color.rgb = PRIMARY_EMERALD
    pe_num.font.name = 'Segoe UI'

    pe_lbl = tf_e.add_paragraph()
    pe_lbl.text = "SIMULATED ENERGY REDUCTION"
    pe_lbl.font.size = Pt(10.5)
    pe_lbl.font.bold = True
    pe_lbl.font.color.rgb = TEXT_WHITE
    pe_lbl.font.name = 'Segoe UI'

    pe_val = tf_e.add_paragraph()
    pe_val.text = "Baseline: 56,961.7 kWh  ➔  EcoSense: 41,145.4 kWh\nSaved: 15,816.3 kWh across 30 days"
    pe_val.font.size = Pt(9)
    pe_val.font.color.rgb = TEXT_MUTED
    pe_val.font.name = 'Segoe UI'

    pcard = create_card(slide7, Inches(4.8), Inches(1.35), card_w7, Inches(1.85), border=ACCENT_CYAN, border_width=1.5)
    tf_p = pcard.text_frame
    tf_p.margin_left = tf_p.margin_right = Inches(0.25)
    tf_p.margin_top = Inches(0.18)

    pp_num = tf_p.paragraphs[0]
    pp_num.text = "23.2%"
    pp_num.font.size = Pt(36)
    pp_num.font.bold = True
    pp_num.font.color.rgb = ACCENT_CYAN
    pp_num.font.name = 'Segoe UI'

    pp_lbl = tf_p.add_paragraph()
    pp_lbl.text = "SIMULATED PEAK SHAVED"
    pp_lbl.font.size = Pt(10.5)
    pp_lbl.font.bold = True
    pp_lbl.font.color.rgb = TEXT_WHITE
    pp_lbl.font.name = 'Segoe UI'

    pp_val = tf_p.add_paragraph()
    pp_val.text = "Baseline: 195.4 kW  ➔  EcoSense: 150.1 kW\nShaved: 45.3 kW (Kept ≤ 175 kW threshold)"
    pp_val.font.size = Pt(9)
    pp_val.font.color.rgb = TEXT_MUTED
    pp_val.font.name = 'Segoe UI'

    ccard = create_card(slide7, Inches(8.8), Inches(1.35), card_w7, Inches(1.85), border=ACCENT_AMBER, border_width=1.5)
    tf_c = ccard.text_frame
    tf_c.margin_left = tf_c.margin_right = Inches(0.25)
    tf_c.margin_top = Inches(0.18)

    pc_num = tf_c.paragraphs[0]
    pc_num.text = "₹134,433"
    pc_num.font.size = Pt(36)
    pc_num.font.bold = True
    pc_num.font.color.rgb = ACCENT_AMBER
    pc_num.font.name = 'Segoe UI'

    pc_lbl = tf_c.add_paragraph()
    pc_lbl.text = "SIMULATED 30-DAY COST DIFFERENCE"
    pc_lbl.font.size = Pt(10.5)
    pc_lbl.font.bold = True
    pc_lbl.font.color.rgb = TEXT_WHITE
    pc_lbl.font.name = 'Segoe UI'

    pc_val = tf_c.add_paragraph()
    pc_val.text = "Baseline: ₹484,170  ➔  EcoSense: ₹349,738\nCalculated at commercial tariff ₹8.50/kWh"
    pc_val.font.size = Pt(9)
    pc_val.font.color.rgb = TEXT_MUTED
    pc_val.font.name = 'Segoe UI'

    chart7_path = "scratch/slides_assets/slide7_comparison_chart.png"
    if os.path.exists(chart7_path):
        slide7.shapes.add_picture(chart7_path, Inches(0.8), Inches(3.35), Inches(11.733), Inches(2.75))
    else:
        fc7 = create_card(slide7, Inches(0.8), Inches(3.35), Inches(11.733), Inches(2.75))
        tf_fc7 = fc7.text_frame
        tf_fc7.vertical_anchor = MSO_ANCHOR.MIDDLE
        p_fc7 = tf_fc7.paragraphs[0]
        p_fc7.alignment = PP_ALIGN.CENTER
        p_fc7.text = "Baseline vs EcoSense Simulation Comparison Chart"
        p_fc7.font.size = Pt(14)
        p_fc7.font.color.rgb = TEXT_WHITE

    disc_card = create_card(slide7, Inches(0.8), Inches(6.25), Inches(11.733), Inches(0.62), bg=RGBColor(12, 19, 36), border=CARD_BORDER)
    tf_dc = disc_card.text_frame
    tf_dc.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf_dc.margin_left = Inches(0.3)
    p_dc = tf_dc.paragraphs[0]
    p_dc.alignment = PP_ALIGN.CENTER
    p_dc.text = "SIMULATION RESULT — NOT MEASURED REAL-WORLD BUILDING DATA  |  Compared with defined fixed-schedule baseline across 5 simulated zones (~2,300 m²)"
    p_dc.font.size = Pt(10)
    p_dc.font.bold = True
    p_dc.font.color.rgb = PRIMARY_EMERALD
    p_dc.font.name = 'Segoe UI'

    add_footer(slide7, 7)

    # =========================================================================
    # SLIDE 8: WHY ECOSENSE AI?
    # =========================================================================
    slide8 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide8)
    add_header(slide8, "WHY ECOSENSE AI?", "COMPETITIVE DIFFERENTIATION & CORE VALUE", "WHY WE WIN", PRIMARY_EMERALD)

    q_data = [
        ("01", "ENERGY + COMFORT + PEAK", "Optimizes all three instead of energy alone.", [
            "Traditional systems often cut energy by sacrificing occupant comfort.",
            "EcoSense AI strictly guards the 22°C–26°C comfort boundary.",
            "Simultaneously manages peak demand charges (≤ 175 kW threshold)."
        ], PRIMARY_EMERALD),
        ("02", "PREDICTIVE DEMAND FORECASTING", "Forecasts demand before peak periods arrive.", [
            "Proactively anticipates afternoon thermal and occupancy surges.",
            "Enables smart pre-cooling during low-tariff, low-demand morning hours.",
            "Prevents reactive throttling when peak demand penalties kick in."
        ], ACCENT_CYAN),
        ("03", "ZONE-AWARE INTELLIGENCE", "Different zones receive different recommendations.", [
            "Evaluates conference rooms, cafeteria, and open offices individually.",
            "Applies dynamic setbacks only to vacant or partially occupied zones.",
            "Eliminates clumsy whole-building blanket setpoint adjustments."
        ], ACCENT_BLUE),
        ("04", "ACTIONABLE & EXPLAINABLE", "Turns predictions into clear operating recommendations.", [
            "Delivers quantified kWh and cost savings for every proposed action.",
            "Provides transparent rationale for facility manager verification.",
            "Keeps humans in the loop for safe, accountable supervisory control."
        ], ACCENT_AMBER)
    ]

    qw = Inches(5.72)
    qh = Inches(2.25)
    for i, (qnum, qtitle, qsub, qbullets, qcolor) in enumerate(q_data):
        col = i % 2
        row = i // 2
        qx = Inches(0.8) + col * Inches(6.013)
        qy = Inches(1.4) + row * Inches(2.4)

        qc = create_card(slide8, qx, qy, qw, qh, border=qcolor, border_width=1.2)
        tf_q = qc.text_frame
        tf_q.margin_left = tf_q.margin_right = Inches(0.28)
        tf_q.margin_top = Inches(0.2)

        p_qt = tf_q.paragraphs[0]
        p_qt.text = f"{qnum}  |  {qtitle}"
        p_qt.font.size = Pt(12.5)
        p_qt.font.bold = True
        p_qt.font.color.rgb = qcolor
        p_qt.font.name = 'Segoe UI'

        p_qs = tf_q.add_paragraph()
        p_qs.text = qsub
        p_qs.font.size = Pt(10.5)
        p_qs.font.bold = True
        p_qs.font.color.rgb = TEXT_WHITE
        p_qs.font.name = 'Segoe UI'

        for qb in qbullets:
            pqb = tf_q.add_paragraph()
            pqb.text = f"•  {qb}"
            pqb.font.size = Pt(9)
            pqb.font.color.rgb = TEXT_MUTED
            pqb.font.name = 'Segoe UI'

    bot8 = create_card(slide8, Inches(0.8), Inches(6.3), Inches(11.733), Inches(0.55), bg=RGBColor(15, 23, 42), border=CARD_BORDER)
    tf_b8 = bot8.text_frame
    tf_b8.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf_b8.margin_left = Inches(0.3)
    p_b8 = tf_b8.paragraphs[0]
    p_b8.alignment = PP_ALIGN.CENTER
    p_b8.text = "\"Not just a dashboard. A decision-support layer for smarter buildings.\""
    p_b8.font.size = Pt(13)
    p_b8.font.bold = True
    p_b8.font.color.rgb = PRIMARY_EMERALD
    p_b8.font.name = 'Segoe UI'

    add_footer(slide8, 8)

    # =========================================================================
    # SLIDE 9: FROM PROTOTYPE TO REAL BUILDINGS (REFINED SPACING)
    # =========================================================================
    slide9 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide9)
    add_header(slide9, "FROM PROTOTYPE TO REAL BUILDINGS", "IMPLEMENTATION ROADMAP & VALUE REALIZATION", "4-PHASE ROADMAP", ACCENT_CYAN)

    road_steps = [
        ("NOW", "SOFTWARE PROTOTYPE", "Simulation + ML + optimization + dashboard", [
            "30-day multi-zone simulation",
            "Random Forest demand forecasting",
            "Multi-objective optimization cockpit"
        ], PRIMARY_EMERALD),
        ("NEXT", "SENSOR PILOT", "Occupancy + temperature + IAQ + energy meters", [
            "IoT sensor deployment in 1 zone",
            "Validate ground-truth thermal inertia",
            "Refine empirical prediction models"
        ], ACCENT_CYAN),
        ("THEN", "BMS INTEGRATION", "HVAC + lighting supervisory control", [
            "BACnet / Modbus protocol bridge",
            "Automated setpoint recommendations",
            "Supervised closed-loop control"
        ], ACCENT_BLUE),
        ("SCALE", "MULTI-BUILDING FLEET", "Continuous learning + portfolio management", [
            "Cross-building knowledge transfer",
            "Enterprise portfolio dashboard",
            "Grid interactive demand response"
        ], ACCENT_AMBER)
    ]

    rw = Inches(2.78)
    rg = Inches(0.2)
    for i, (phase, rtitle, rsub, rbullets, rcol) in enumerate(road_steps):
        rx = Inches(0.8) + i * (rw + rg)
        rc = create_card(slide9, rx, Inches(1.35), rw, Inches(3.1), border=rcol, border_width=1.2)
        tf_r = rc.text_frame
        tf_r.margin_left = tf_r.margin_right = Inches(0.2)
        tf_r.margin_top = Inches(0.18)

        p_ph = tf_r.paragraphs[0]
        p_ph.text = phase
        p_ph.font.size = Pt(10.5)
        p_ph.font.bold = True
        p_ph.font.color.rgb = rcol
        p_ph.font.name = 'Segoe UI'

        p_rt = tf_r.add_paragraph()
        p_rt.text = rtitle
        p_rt.font.size = Pt(12)
        p_rt.font.bold = True
        p_rt.font.color.rgb = TEXT_WHITE
        p_rt.font.name = 'Segoe UI'

        p_rs = tf_r.add_paragraph()
        p_rs.text = rsub
        p_rs.font.size = Pt(9)
        p_rs.font.bold = True
        p_rs.font.color.rgb = rcol
        p_rs.font.name = 'Segoe UI'

        for rb in rbullets:
            prb = tf_r.add_paragraph()
            prb.text = f"• {rb}"
            prb.font.size = Pt(8.5)
            prb.font.color.rgb = TEXT_MUTED
            prb.font.name = 'Segoe UI'

    val_card = create_card(slide9, Inches(0.8), Inches(4.65), Inches(11.733), Inches(1.95), bg=RGBColor(12, 19, 36), border=CARD_BORDER)
    tf_v = val_card.text_frame
    tf_v.margin_left = tf_v.margin_right = Inches(0.35)
    tf_v.margin_top = Inches(0.18)

    p_vt = tf_v.paragraphs[0]
    p_vt.alignment = PP_ALIGN.LEFT
    p_vt.text = "EXPECTED OPERATIONAL VALUE"
    p_vt.font.size = Pt(11)
    p_vt.font.bold = True
    p_vt.font.color.rgb = PRIMARY_EMERALD
    p_vt.font.name = 'Segoe UI'

    val_pillars = [
        ("ENERGY", "Reduce unnecessary consumption during low/zero occupancy hours.", PRIMARY_EMERALD),
        ("PEAK DEMAND", "Reduce avoidable afternoon demand spikes to curb maximum demand charges.", ACCENT_CYAN),
        ("COMFORT", "Strictly maintain 22°C–26°C target across all occupied spaces.", ACCENT_BLUE),
        ("OPERATIONS", "Equip facility managers with actionable, explainable operational guidance.", ACCENT_AMBER)
    ]
    for vname, vdesc, vcol in val_pillars:
        pv = tf_v.add_paragraph()
        pv.alignment = PP_ALIGN.LEFT
        pv.text = f"• {vname}: {vdesc}"
        pv.font.size = Pt(9.5)
        pv.font.color.rgb = TEXT_MUTED
        pv.font.name = 'Segoe UI'

    fn9_box = slide9.shapes.add_textbox(Inches(0.8), Inches(6.65), Inches(11.733), Inches(0.25))
    tf_fn9 = fn9_box.text_frame
    tf_fn9.margin_left = tf_fn9.margin_top = tf_fn9.margin_right = tf_fn9.margin_bottom = 0
    p_fn9 = tf_fn9.paragraphs[0]
    p_fn9.text = "Roadmap represents planned progression. Future phases require physical hardware pilots and BMS integration."
    p_fn9.font.size = Pt(8.5)
    p_fn9.font.italic = True
    p_fn9.font.color.rgb = TEXT_DIM
    p_fn9.font.name = 'Segoe UI'

    add_footer(slide9, 9)

    # =========================================================================
    # SLIDE 10: CONCLUSION & VISION (NO OVERLAP, ZERO CLIPPING)
    # =========================================================================
    slide10 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide10)
    add_header(slide10, "BUILDING SMARTER, NOT JUST USING LESS", "YUVA YODHA ENERGY TECH HACKATHON 2026", "CONCLUSION & VISION", PRIMARY_EMERALD)

    # Hero Center Container - Adjusted height and clean hierarchy
    hero_card = create_card(slide10, Inches(0.8), Inches(1.35), Inches(11.733), Inches(4.0), bg=RGBColor(12, 19, 36), border=PRIMARY_EMERALD, border_width=1.5)
    
    # Text box for top half of hero container
    hero_tb = slide10.shapes.add_textbox(Inches(1.0), Inches(1.5), Inches(11.333), Inches(1.9))
    tf_h = hero_tb.text_frame
    tf_h.word_wrap = True
    tf_h.margin_left = tf_h.margin_top = tf_h.margin_right = tf_h.margin_bottom = 0

    ph1 = tf_h.paragraphs[0]
    ph1.alignment = PP_ALIGN.CENTER
    ph1.text = "ECOSENSE AI"
    ph1.font.size = Pt(36)
    ph1.font.bold = True
    ph1.font.color.rgb = PRIMARY_EMERALD
    ph1.font.name = 'Segoe UI'

    ph2 = tf_h.add_paragraph()
    ph2.alignment = PP_ALIGN.CENTER
    ph2.text = "Intelligent Building Energy Optimizer"
    ph2.font.size = Pt(18)
    ph2.font.bold = True
    ph2.font.color.rgb = ACCENT_CYAN
    ph2.font.name = 'Segoe UI'

    ph3 = tf_h.add_paragraph()
    ph3.alignment = PP_ALIGN.CENTER
    ph3.text = "\"Turning building data into smarter energy decisions.\""
    ph3.font.size = Pt(15.5)
    ph3.font.italic = True
    ph3.font.bold = True
    ph3.font.color.rgb = TEXT_WHITE
    ph3.font.name = 'Segoe UI'

    # 3 Summary Result Badges in Hero Card - Positioned cleanly below text with NO overlap
    res_badges = [
        ("27.8%", "Simulated Energy Reduction", PRIMARY_EMERALD),
        ("23.2%", "Simulated Peak Shaved", ACCENT_CYAN),
        ("22°C–26°C", "Strict Comfort Target Guard", ACCENT_AMBER)
    ]
    for i, (bnum, blbl, bcol) in enumerate(res_badges):
        bx = Inches(1.5) + i * Inches(3.6)
        bshape = slide10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, bx, Inches(3.95), Inches(3.2), Inches(1.15))
        bshape.fill.solid()
        bshape.fill.fore_color.rgb = CARD_BG
        bshape.line.color.rgb = bcol
        bshape.line.width = Pt(1.4)
        tf_bs = bshape.text_frame
        tf_bs.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf_bs.margin_top = tf_bs.margin_bottom = Inches(0.08)
        
        p1 = tf_bs.paragraphs[0]
        p1.alignment = PP_ALIGN.CENTER
        p1.text = bnum
        p1.font.size = Pt(22)
        p1.font.bold = True
        p1.font.color.rgb = bcol
        p1.font.name = 'Segoe UI'

        p2 = tf_bs.add_paragraph()
        p2.alignment = PP_ALIGN.CENTER
        p2.text = blbl
        p2.font.size = Pt(9.5)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_WHITE
        p2.font.name = 'Segoe UI'

    # Bottom Row: Team Info & Status
    tcard10 = create_card(slide10, Inches(0.8), Inches(5.55), Inches(6.5), Inches(1.3))
    tf_t10 = tcard10.text_frame
    tf_t10.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf_t10.margin_left = Inches(0.3)

    pt1 = tf_t10.paragraphs[0]
    pt1.text = "TEAM NOVA  •  Yuva Yodha Energy Tech Hackathon 2026"
    pt1.font.size = Pt(12)
    pt1.font.bold = True
    pt1.font.color.rgb = TEXT_WHITE
    pt1.font.name = 'Segoe UI'

    pt2 = tf_t10.add_paragraph()
    pt2.text = "Team Lead: Dharshine V  |  vdharshine19@gmail.com"
    pt2.font.size = Pt(11)
    pt2.font.bold = True
    pt2.font.color.rgb = ACCENT_CYAN
    pt2.font.name = 'Segoe UI'

    pt3 = tf_t10.add_paragraph()
    pt3.text = "Challenge: Smart Buildings"
    pt3.font.size = Pt(9.5)
    pt3.font.color.rgb = TEXT_MUTED
    pt3.font.name = 'Segoe UI'

    scard10 = create_card(slide10, Inches(7.5), Inches(5.55), Inches(5.033), Inches(1.3))
    tf_s10 = scard10.text_frame
    tf_s10.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf_s10.margin_left = Inches(0.3)

    ps1 = tf_s10.paragraphs[0]
    ps1.text = "CURRENT STATUS"
    ps1.font.size = Pt(11)
    ps1.font.bold = True
    ps1.font.color.rgb = PRIMARY_EMERALD
    ps1.font.name = 'Segoe UI'

    ps2 = tf_s10.add_paragraph()
    ps2.text = "Functional software simulation and decision-support prototype."
    ps2.font.size = Pt(10)
    ps2.font.color.rgb = TEXT_WHITE
    ps2.font.name = 'Segoe UI'

    ps3 = tf_s10.add_paragraph()
    ps3.text = "Evaluated on 5 commercial zones with 30-day deterministic telemetry."
    ps3.font.size = Pt(9)
    ps3.font.color.rgb = TEXT_MUTED
    ps3.font.name = 'Segoe UI'

    add_footer(slide10, 10)

    # Save presentation
    output_filename = "EcoSense_AI_Yuva_Yodha_Hackathon_2026_FINAL.pptx"
    prs.save(output_filename)
    print(f"Successfully generated {output_filename}")

if __name__ == "__main__":
    build_presentation()
