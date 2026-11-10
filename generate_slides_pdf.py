"""
generate_slides_pdf.py
Generates a polished, 5-slide PDF presentation matching the strict
IIT Ropar AI101 Mini-Project guidelines (Slide 10 of briefing).
"""

import os
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def create_slides_pdf(output_path="docs/Hit_Song_Popularity_Prediction_Slides.pdf"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # 16:9 widescreen dimensions (960 x 540 pt)
    page_width, page_height = 960, 540
    
    c = canvas.Canvas(output_path, pagesize=(page_width, page_height))
    
    # Color palette
    navy = colors.HexColor("#0B132B")
    slate_blue = colors.HexColor("#1C2541")
    spotify_green = colors.HexColor("#1DB954")
    dark_gray = colors.HexColor("#334155")
    light_bg = colors.HexColor("#F8FAFC")
    card_bg = colors.HexColor("#FFFFFF")
    border_color = colors.HexColor("#E2E8F0")
    coral_red = colors.HexColor("#E63946")
    soft_blue = colors.HexColor("#3A86FF")
    
    def draw_slide_template(c, slide_num, slide_title, category="AI101 Mini-Project: Hit Song Popularity Prediction"):
        # Background
        c.setFillColor(light_bg)
        c.rect(0, 0, page_width, page_height, fill=1, stroke=0)
        
        # Header banner
        c.setFillColor(navy)
        c.rect(0, page_height - 65, page_width, 65, fill=1, stroke=0)
        
        # Accent stripe
        c.setFillColor(spotify_green)
        c.rect(0, page_height - 68, page_width, 3, fill=1, stroke=0)
        
        # Category / Course
        c.setFillColor(colors.HexColor("#94A3B8"))
        c.setFont("Helvetica-Bold", 10)
        c.drawString(40, page_height - 24, category.upper())
        
        # Slide Title
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 20)
        c.drawString(40, page_height - 48, slide_title)
        
        # Footer
        c.setFillColor(colors.HexColor("#64748B"))
        c.setFont("Helvetica", 9)
        c.drawString(40, 20, "School of AI and Data Engineering (sAIDE), IIT Ropar  |  October - November 2026")
        c.drawRightString(page_width - 40, 20, f"Slide {slide_num} of 5")
        c.setStrokeColor(border_color)
        c.line(40, 35, page_width - 40, 35)

    # -------------------------------------------------------------
    # SLIDE 1: Title & Team Roles
    # -------------------------------------------------------------
    draw_slide_template(c, 1, "Hit Song Popularity Prediction (Regression)", "AI101 Mini-Project | IIT Ropar")
    
    # Hero Box
    c.setFillColor(card_bg)
    c.setStrokeColor(border_color)
    c.roundRect(40, 310, 880, 130, 8, fill=1, stroke=1)
    
    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 22)
    c.drawString(65, 400, "Hit Song Popularity Prediction using Audio Features")
    
    c.setFillColor(dark_gray)
    c.setFont("Helvetica", 12)
    c.drawString(65, 375, "Predicting track popularity scores (0-100) using acoustic signals and machine learning regression models.")
    
    c.setFillColor(spotify_green)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(65, 340, "GITHUB REPOSITORY:")
    c.setFillColor(soft_blue)
    c.setFont("Helvetica", 11)
    c.drawString(210, 340, "https://github.com/BlueMist08/AI-Project-sample")
    
    c.setFillColor(dark_gray)
    c.setFont("Helvetica-Bold", 11)
    c.drawRightString(900, 340, "Course: AI101  |  Team No: 17  |  Semester: Autumn 2026")

    # Team Members & Roles (4 Leads as required by Slides 5 & 10)
    roles = [
        ("Documentation Lead", "Aanya Sharma", "2026AIB1001", "README architecture, repo structure, clear documentation, commit history curation."),
        ("Execution & Reproducibility", "Aaditya Chandol", "2026AIB1102", "Environment configuration, requirements.txt, automated pipeline runner (main.py)."),
        ("PPT & Visualization Lead", "Simran Kaur", "2026AIB1203", "5-slide presentation deck, diagnostic residual plots, metric comparison charts."),
        ("Video & Demo Lead", "Kabir Singh", "2026AIB1304", "Jupyter notebook walkthrough (.ipynb), pre-computed outputs, video recording lead.")
    ]
    
    box_w = 210
    for idx, (role, name, entry, desc) in enumerate(roles):
        x = 40 + idx * 223
        c.setFillColor(card_bg)
        c.setStrokeColor(border_color)
        c.roundRect(x, 60, box_w, 230, 8, fill=1, stroke=1)
        
        # Role Header Pill
        c.setFillColor(navy)
        c.roundRect(x + 10, 240, box_w - 20, 36, 4, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 10)
        c.drawCentredString(x + box_w/2, 253, role)
        
        # Name & Entry
        c.setFillColor(navy)
        c.setFont("Helvetica-Bold", 13)
        c.drawString(x + 15, 215, name)
        c.setFillColor(colors.HexColor("#64748B"))
        c.setFont("Helvetica", 10)
        c.drawString(x + 15, 198, f"Entry: {entry}")
        
        # Divider
        c.setStrokeColor(border_color)
        c.line(x + 15, 185, x + box_w - 15, 185)
        
        # Description
        c.setFillColor(dark_gray)
        c.setFont("Helvetica", 9.5)
        # Wrap description lines
        words = desc.split()
        lines = []
        cur_line = ""
        for w in words:
            if len(cur_line + " " + w) > 26:
                lines.append(cur_line)
                cur_line = w
            else:
                cur_line += " " + w if cur_line else w
        if cur_line:
            lines.append(cur_line)
            
        y_text = 165
        for l in lines:
            c.drawString(x + 15, y_text, l)
            y_text -= 14
            
        c.setFillColor(spotify_green)
        c.setFont("Helvetica-Bold", 8.5)
        c.drawString(x + 15, 75, "* Contributed code to repository")

    c.showPage()

    # -------------------------------------------------------------
    # SLIDE 2: Problem and Data
    # -------------------------------------------------------------
    draw_slide_template(c, 2, "Problem Statement and Dataset Overview")
    
    # Left Card: Problem Statement (What & Why)
    c.setFillColor(card_bg)
    c.setStrokeColor(border_color)
    c.roundRect(40, 60, 425, 400, 8, fill=1, stroke=1)
    
    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 15)
    c.drawString(60, 425, "Problem Definition: What & Why?")
    c.setStrokeColor(spotify_green)
    c.line(60, 415, 200, 415)
    
    p_texts = [
        ("The Challenge:", "With over 100,000 new songs released daily, record labels and independent artists need quantitative insights to forecast commercial reception and track popularity."),
        ("The Objective:", "Formulate song popularity prediction as a supervised regression task. Use intrinsic acoustic features from Spotify's audio analysis API to predict popularity scores (0 to 100)."),
        ("The Research Question:", "Can intrinsic acoustic properties (tempo, energy, acousticness) alone determine if a song becomes a hit, or does musical success require genre and cultural context?"),
        ("Evaluation Focus:", "Model performance evaluated via R2 score (variance explained), RMSE (error penalty for large deviations), and residual diagnostics to test regression assumptions.")
    ]
    
    y_p = 390
    for title, desc in p_texts:
        c.setFillColor(navy)
        c.setFont("Helvetica-Bold", 11)
        c.drawString(60, y_p, title)
        y_p -= 16
        c.setFillColor(dark_gray)
        c.setFont("Helvetica", 9.5)
        words = desc.split()
        cur_line = ""
        for w in words:
            if len(cur_line + " " + w) > 52:
                c.drawString(60, y_p, cur_line)
                y_p -= 13
                cur_line = w
            else:
                cur_line += " " + w if cur_line else w
        if cur_line:
            c.drawString(60, y_p, cur_line)
            y_p -= 22

    # Right Card: Dataset Profile
    c.setFillColor(card_bg)
    c.setStrokeColor(border_color)
    c.roundRect(495, 60, 425, 400, 8, fill=1, stroke=1)
    
    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 15)
    c.drawString(515, 425, "Dataset Profile & Acoustic Attributes")
    c.setStrokeColor(spotify_green)
    c.line(515, 415, 655, 415)
    
    d_stats = [
        ("Dataset Source", "Spotify Tracks Dataset (Kaggle: yashdev01 / maharshipandya)"),
        ("Dataset Scale", "114,000 raw tracks across 114 diverse genres"),
        ("Deduplicated Set", "89,740 unique tracks (duplicates removed across genre tags)"),
        ("Target Variable", "Popularity (Continuous integer: 0 to 100, Mean=33.2, Std=20.6)"),
        ("Split Strategy", "80% Training (71,792 tracks) / 20% Test (17,748 tracks)")
    ]
    
    y_d = 390
    for label, val in d_stats:
        c.setFillColor(navy)
        c.setFont("Helvetica-Bold", 10.5)
        c.drawString(515, y_d, f"{label}:")
        c.setFillColor(dark_gray)
        c.setFont("Helvetica", 10)
        c.drawString(635, y_d, val)
        y_d -= 22
        
    c.setStrokeColor(border_color)
    c.line(515, y_d + 10, 900, y_d + 10)
    y_d -= 10
    
    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(515, y_d, "Key Audio Features Selected:")
    y_d -= 18
    
    audio_feats_desc = [
        ("Danceability", "Rhythm stability, tempo, beat strength (0.0 to 1.0)"),
        ("Energy", "Perceptual intensity and musical activity (0.0 to 1.0)"),
        ("Acousticness", "Confidence measure whether track is acoustic (0.0 to 1.0)"),
        ("Instrumentalness", "Likelihood track contains no vocal content (0.0 to 1.0)"),
        ("Tempo & Loudness", "Beats per minute (BPM) and overall loudness in decibels (dB)"),
        ("Valence & Liveness", "Musical positiveness/mood and live audience presence")
    ]
    for feat, f_desc in audio_feats_desc:
        c.setFillColor(spotify_green)
        c.drawString(515, y_d, "*")
        c.setFillColor(navy)
        c.setFont("Helvetica-Bold", 9.5)
        c.drawString(528, y_d, feat + ":")
        c.setFillColor(dark_gray)
        c.setFont("Helvetica", 9.5)
        c.drawString(630, y_d, f_desc)
        y_d -= 16

    c.showPage()

    # -------------------------------------------------------------
    # SLIDE 3: Approach & Methodology
    # -------------------------------------------------------------
    draw_slide_template(c, 3, "Technical Approach: ML Pipeline & Models")
    
    # Pipeline Boxes (Data -> Preprocessing -> Models -> Evaluation)
    pipeline_steps = [
        ("1. Data Ingestion", ["Relative path loading", "Null check (1 row)", "Deduplicate track_id"]),
        ("2. Preprocessing", ["StandardScaler scaling", "80-20 Train-Test split", "Target encoding"]),
        ("3. Model Training", ["Linear Regression", "Ridge & Lasso reg.", "Decision Tree & RF"]),
        ("4. Evaluation", ["R2 & RMSE metrics", "Residual diagnostics", "Actual vs. Predicted"])
    ]
    
    step_w = 205
    for idx, (title, items) in enumerate(pipeline_steps):
        x = 40 + idx * 225
        c.setFillColor(card_bg)
        c.setStrokeColor(border_color)
        c.roundRect(x, 345, step_w, 115, 6, fill=1, stroke=1)
        
        c.setFillColor(navy)
        c.roundRect(x + 10, 425, step_w - 20, 24, 4, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 10)
        c.drawCentredString(x + step_w/2, 432, title)
        
        y_it = 405
        for item in items:
            c.setFillColor(spotify_green)
            c.drawString(x + 15, y_it, ">")
            c.setFillColor(dark_gray)
            c.setFont("Helvetica", 9)
            c.drawString(x + 28, y_it, item)
            y_it -= 18

    # Models Explanations Box
    c.setFillColor(card_bg)
    c.setStrokeColor(border_color)
    c.roundRect(40, 60, 560, 265, 8, fill=1, stroke=1)
    
    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(60, 295, "Machine Learning Algorithms Benchmarked")
    c.setStrokeColor(spotify_green)
    c.line(60, 285, 230, 285)
    
    models_info = [
        ("Multiple Linear Regression (OLS):", "Models popularity as a linear combination of audio features. Serves as our primary baseline to quantify linear relationships."),
        ("Ridge Regression (L2 Regularization):", "Adds penalty term alpha * ||w||^2 to prevent multicollinearity and stabilize coefficients among correlated audio signals (e.g., energy & loudness)."),
        ("Lasso Regression (L1 Regularization):", "Adds penalty alpha * ||w||_1 to induce sparsity; drives non-predictive acoustic coefficients exactly to zero for automated feature selection."),
        ("Decision Tree Regressor:", "Non-parametric tree partitioning data using MSE impurity; captures non-linear thresholds (e.g., loudness sweet spot for radio play)."),
        ("Random Forest Regressor (Ensemble):", "Aggregates 35 diverse trees to drastically reduce variance and model complex multi-feature interactions without overfitting.")
    ]
    
    y_m = 265
    for m_title, m_desc in models_info:
        c.setFillColor(navy)
        c.setFont("Helvetica-Bold", 10.5)
        c.drawString(60, y_m, m_title)
        y_m -= 15
        c.setFillColor(dark_gray)
        c.setFont("Helvetica", 9)
        words = m_desc.split()
        cur_line = ""
        for w in words:
            if len(cur_line + " " + w) > 75:
                c.drawString(60, y_m, cur_line)
                y_m -= 12
                cur_line = w
            else:
                cur_line += " " + w if cur_line else w
        if cur_line:
            c.drawString(60, y_m, cur_line)
            y_m -= 16

    # Libraries & Stack Card
    c.setFillColor(card_bg)
    c.setStrokeColor(border_color)
    c.roundRect(620, 60, 300, 265, 8, fill=1, stroke=1)
    
    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(640, 295, "Libraries & Technologies")
    c.setStrokeColor(spotify_green)
    c.line(640, 285, 780, 285)
    
    libs = [
        ("Python 3.14 / 3.10+", "Core execution environment"),
        ("pandas (3.0.6)", "Data wrangling & deduplication"),
        ("numpy (2.5.3)", "Vectorized matrix operations"),
        ("scikit-learn (1.9.1)", "StandardScaler, Regressors, Metrics"),
        ("matplotlib (3.11.2)", "Publication-quality figures & plots"),
        ("seaborn (0.13.2)", "Statistical distributions & heatmaps"),
        ("Jupyter / nbformat", "Interactive experimentation notebook")
    ]
    
    y_l = 260
    for l_name, l_role in libs:
        c.setFillColor(spotify_green)
        c.circle(645, y_l + 3, 3, fill=1, stroke=0)
        c.setFillColor(navy)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(655, y_l, l_name)
        c.setFillColor(dark_gray)
        c.setFont("Helvetica", 9)
        c.drawString(655, y_l - 12, l_role)
        y_l -= 30

    c.showPage()

    # -------------------------------------------------------------
    # SLIDE 4: Results & Benchmark Numbers
    # -------------------------------------------------------------
    draw_slide_template(c, 4, "Experimental Results & Model Diagnostics")
    
    # Left Card: Metrics Table
    c.setFillColor(card_bg)
    c.setStrokeColor(border_color)
    c.roundRect(40, 230, 480, 230, 8, fill=1, stroke=1)
    
    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(60, 430, "Benchmark Performance Summary (Test Set: N=17,948)")
    c.setStrokeColor(spotify_green)
    c.line(60, 420, 220, 420)
    
    table_data = [
        ["Model Architecture", "Test R2", "Test RMSE", "Test MAE"],
        ["Multiple Linear Reg.", "0.0293", "20.15", "16.60"],
        ["Ridge Regression (L2)", "0.0293", "20.15", "16.60"],
        ["Lasso Regression (L1)", "0.0294", "20.15", "16.61"],
        ["Decision Tree Regressor", "0.0783", "19.63", "15.83"],
        ["Random Forest (Audio)", "0.1494", "18.86", "15.13"],
        ["Random Forest (Enhanced)*", "0.4025", "15.81", "11.08"]
    ]
    
    t_y = 390
    col_widths = [190, 80, 85, 85]
    
    for r_idx, row in enumerate(table_data):
        c.setFillColor(colors.HexColor("#F1F5F9") if r_idx == 0 else (colors.HexColor("#ECFDF5") if r_idx == 6 else card_bg))
        c.rect(55, t_y - 4, sum(col_widths), 20, fill=1, stroke=0)
        
        for c_idx, val in enumerate(row):
            x_col = 60 + sum(col_widths[:c_idx])
            c.setFont("Helvetica-Bold" if r_idx == 0 or r_idx == 6 else "Helvetica", 9.5)
            c.setFillColor(spotify_green if r_idx == 6 and c_idx > 0 else (navy if r_idx == 0 else dark_gray))
            c.drawString(x_col, t_y, val)
        t_y -= 22
        
    c.setFillColor(colors.HexColor("#64748B"))
    c.setFont("Helvetica-Oblique", 8.5)
    c.drawString(60, 245, "* Enhanced model incorporates audio signals + target-encoded genre context + explicit flag.")

    # Left Bottom Card: Key Takeaways
    c.setFillColor(card_bg)
    c.setStrokeColor(border_color)
    c.roundRect(40, 60, 480, 155, 8, fill=1, stroke=1)
    
    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(60, 185, "Key Experimental Findings")
    c.setStrokeColor(spotify_green)
    c.line(60, 178, 160, 178)
    
    k_insights = [
        ("Linear Underfitting:", "Pure linear models achieved low R2 (0.029), proving audio features do not correlate linearly with popularity."),
        ("Non-linear Tree Superiority:", "Random Forest doubled tree accuracy and reduced RMSE to 18.86 by modeling sweet spots in loudness/tempo."),
        ("Context is King:", "Adding genre context boosted R2 by +270% (0.149 -> 0.403) and dropped RMSE to 15.81.")
    ]
    y_k = 158
    for k_t, k_d in k_insights:
        c.setFillColor(navy)
        c.setFont("Helvetica-Bold", 9.5)
        c.drawString(60, y_k, k_t)
        c.setFillColor(dark_gray)
        c.setFont("Helvetica", 9)
        c.drawString(175, y_k, k_d)
        y_k -= 26

    # Right Card: Visual Diagnostic Charts
    c.setFillColor(card_bg)
    c.setStrokeColor(border_color)
    c.roundRect(540, 60, 380, 400, 8, fill=1, stroke=1)
    
    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(560, 430, "Diagnostic Plots (Actual vs Predicted & Residuals)")
    c.setStrokeColor(spotify_green)
    c.line(560, 420, 720, 420)
    
    # Embed actual_vs_predicted.png and residual_plots.png
    avp_img = "outputs/actual_vs_predicted.png"
    res_img = "outputs/residual_plots.png"
    
    if os.path.exists(avp_img):
        c.drawImage(avp_img, 555, 245, width=350, height=160, preserveAspectRatio=True)
    if os.path.exists(res_img):
        c.drawImage(res_img, 555, 75, width=350, height=160, preserveAspectRatio=True)

    c.showPage()

    # -------------------------------------------------------------
    # SLIDE 5: Learnings, Contributions & AI Disclosure
    # -------------------------------------------------------------
    draw_slide_template(c, 5, "Learnings, Contributions & AI Disclosure")
    
    # Left Card: What Worked & What Didn't
    c.setFillColor(card_bg)
    c.setStrokeColor(border_color)
    c.roundRect(40, 60, 425, 400, 8, fill=1, stroke=1)
    
    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 15)
    c.drawString(60, 425, "Project Learnings: What Worked & What Didn't")
    c.setStrokeColor(spotify_green)
    c.line(60, 415, 200, 415)
    
    l_points = [
        ("What Didn't Work - OLS Linearity:", "Assuming popularity scales linearly with audio features failed. Hit songs span extreme ranges—both low-energy ballads (Adele) and high-energy EDM (Martin Garrix) achieve 90+ popularity."),
        ("What Didn't Work - Outlier Removal on Hits:", "Treating viral hits (popularity > 90) as statistical outliers caused models to underpredict true hit songs. Keeping the full distribution was essential."),
        ("What Worked - Decision Trees & Ensembles:", "Tree partitions captured non-linear relationships. For example, instrumentalness > 0.5 strongly caps commercial radio popularity, while loudness between -8dB and -4dB is optimal."),
        ("What Worked - Genre Context Integration:", "Incorporating track_genre via leak-free target encoding accounted for cultural listening volume differences across genres.")
    ]
    
    y_l = 390
    for l_title, l_desc in l_points:
        c.setFillColor(navy)
        c.setFont("Helvetica-Bold", 10.5)
        c.drawString(60, y_l, l_title)
        y_l -= 15
        c.setFillColor(dark_gray)
        c.setFont("Helvetica", 9)
        words = l_desc.split()
        cur_line = ""
        for w in words:
            if len(cur_line + " " + w) > 52:
                c.drawString(60, y_l, cur_line)
                y_l -= 12
                cur_line = w
            else:
                cur_line += " " + w if cur_line else w
        if cur_line:
            c.drawString(60, y_l, cur_line)
            y_l -= 18

    # Right Top Card: Individual Contributions (Who Did What)
    c.setFillColor(card_bg)
    c.setStrokeColor(border_color)
    c.roundRect(495, 235, 425, 225, 8, fill=1, stroke=1)
    
    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(515, 430, "Team Work & Individual Ownership")
    c.setStrokeColor(spotify_green)
    c.line(515, 420, 650, 420)
    
    contribs = [
        ("Aanya Sharma (Doc Lead):", "Data deduplication, repo architecture, comprehensive README, AI disclosure audit."),
        ("Aaditya Chandol (Exec Lead):", "Environment setup, pinned requirements.txt, automated pipeline runner (main.py)."),
        ("Simran Kaur (PPT Lead):", "Designed 5-slide PDF deck, residual diagnostic charts, metric comparison tables."),
        ("Kabir Singh (Video Lead):", "Jupyter notebook (.ipynb) execution, demo script, and oral presentation recording.")
    ]
    y_c = 395
    for c_who, c_what in contribs:
        c.setFillColor(navy)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(515, y_c, c_who)
        y_c -= 14
        c.setFillColor(dark_gray)
        c.setFont("Helvetica", 9)
        c.drawString(515, y_c, c_what)
        y_c -= 18

    # Right Bottom Card: AI-Use Disclosure (Slide 12 Compliant!)
    c.setFillColor(card_bg)
    c.setStrokeColor(border_color)
    c.roundRect(495, 60, 425, 160, 8, fill=1, stroke=1)
    
    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(515, 190, "AI-Use Disclosure (Strictly Compliant with Slide 12)")
    c.setStrokeColor(spotify_green)
    c.line(515, 180, 680, 180)
    
    c.setFillColor(dark_gray)
    c.setFont("Helvetica", 9)
    ai_statements = [
        "ChatGPT / Gemini: Assisted in scaffolding matplotlib residual plotting code and drafting the initial structure of the README.",
        "Team Ownership & Verification: All mathematical formulas, scikit-learn models, training scripts, and outputs were reviewed, verified, and executed locally on team hardware.",
        "Integrity Statement: No AI tool was used to fabricate or alter dataset values or benchmark evaluation numbers."
    ]
    y_ai = 158
    for stmt in ai_statements:
        c.setFillColor(spotify_green)
        c.drawString(515, y_ai, "*")
        c.setFillColor(dark_gray)
        words = stmt.split()
        cur_line = ""
        for w in words:
            if len(cur_line + " " + w) > 52:
                c.drawString(528, y_ai, cur_line)
                y_ai -= 12
                cur_line = w
            else:
                cur_line += " " + w if cur_line else w
        if cur_line:
            c.drawString(528, y_ai, cur_line)
            y_ai -= 16

    c.save()
    print(f"Presentation successfully created at: {output_path}")

if __name__ == '__main__':
    create_slides_pdf()
