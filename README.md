# Hit Song Popularity Prediction (Regression)

> Predicts a music track's commercial popularity score (0–100) from acoustic features using Multiple Linear Regression, Ridge, Lasso, and Tree-based Ensembles.

[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.14-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Course](https://img.shields.io/badge/AI101-IIT%20Ropar-navy.svg)](#)

---

## 1. Team and Roles

| Member | Entry No. | Role & Primary Responsibility | GitHub Handle |
| :--- | :--- | :--- | :--- |
| **Aaditya Chandol** | `2026AIB1102` | **Execution & Reproducibility Lead** (`requirements.txt`, `src/main.py` pipeline) | `@BlueMist08` |
| **Aanya Sharma** | `2026AIB1001` | **Documentation Lead** (README, repo architecture, guidelines compliance) | `@aanya-sharma` |
| **Simran Kaur** | `2026AIB1203` | **PPT & Visualization Lead** (5-slide PDF deck, residual & diagnostic charts) | `@simran-kaur` |
| **Kabir Singh** | `2026AIB1304` | **Video & Demonstration Lead** (Notebook execution, demo presentation) | `@kabir-singh` |

> *All four members actively wrote and contributed code to the repository across data preprocessing, modeling, evaluation, and documentation.*

---

## 2. Project Structure

```
hit-song-popularity-prediction/
├── data/
│   └── dataset.csv              # Spotify Tracks Dataset (~89,740 deduplicated tracks)
├── docs/
│   └── Hit_Song_Popularity_Prediction_Slides.pdf   # Exactly 5 slides presentation (PDF)
├── notebooks/
│   └── Hit_Song_Popularity_Prediction.ipynb       # Fully executed notebook with pre-rendered outputs
├── outputs/
│   ├── actual_vs_predicted.png  # Multi-panel actual vs predicted popularity comparison
│   ├── correlation_matrix.png   # Pearson correlation heatmap of audio features
│   ├── feature_importance.png   # Decision Tree Gini feature importance
│   ├── linear_reg_coefficients.png # Standardized OLS linear regression weights
│   ├── metrics_summary.csv      # Benchmarking metrics table (R2, RMSE, MAE)
│   └── residual_plots.png       # Residuals vs fitted values & error distributions
├── src/
│   ├── __init__.py              # Package marker
│   ├── preprocess.py            # Deduplication, missing values, scaling & train-test split
│   ├── models.py                # Linear Regression, Ridge, Lasso, Decision Tree & RF
│   ├── evaluate.py              # Metrics computation (R2, RMSE, MAE) & plotting utilities
│   └── main.py                  # Single-command end-to-end execution script
├── .gitignore                   # Standard Python gitignore
├── generate_notebook.py         # Notebook compilation & kernel execution automation
├── generate_slides_pdf.py       # 5-Slide PDF generator script (ReportLab)
├── requirements.txt             # Pinned library dependencies for reproducibility
├── VIDEO_SCRIPT.md              # 5-minute timed speaking script for oral demonstration
└── README.md                    # Project documentation (what the TA reads first)
```

---

## 3. Setup & Environment

Tested on **Python 3.10, 3.11, and 3.14** across Windows, macOS, and Linux.

### Step 1: Clone the repository
```bash
git clone https://github.com/BlueMist08/AI-Project-sample.git
cd AI-Project-sample
```

### Step 2: Create and activate a virtual environment
- **On Windows (PowerShell):**
  ```powershell
  # If PowerShell script execution is restricted, run this once:
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

  python -m venv venv
  venv\Scripts\activate
  ```
- **On Windows (Command Prompt - cmd):**
  ```cmd
  python -m venv venv
  venv\Scripts\activate.bat
  ```
- **On macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### Step 3: Install pinned dependencies
```bash
pip install -r requirements.txt
```

---

## 4. Steps to Run (Exact Commands)

### Command 1: Run End-to-End Pipeline
Executes the full pipeline: loads data, cleans duplicate tracks, runs all 5 regression models, outputs performance tables, and exports all figures to `outputs/`:
```bash
python src/main.py
```
*Expected runtime: under 40 seconds.*

### Command 2: Launch Interactive Jupyter Notebook
Open the notebook with all pre-computed cells, markdown interpretations, and interactive code:
```bash
jupyter notebook notebooks/Hit_Song_Popularity_Prediction.ipynb
```

### Command 3 (Optional): Re-generate 5-Slide PDF Presentation
To re-build `docs/Hit_Song_Popularity_Prediction_Slides.pdf` from source:
```bash
python generate_slides_pdf.py
```

---

## 5. Expected Output

When running `python src/main.py`, the terminal displays:

```text
===========================================================================
AI101 PROJECT: HIT SONG POPULARITY PREDICTION (REGRESSION)
===========================================================================

[1/5] Loading and cleaning dataset from: data\dataset.csv
      Raw dataset shape: (114000, 21)
      Cleaned dataset shape (after deduplication): (89740, 20)
      Target: popularity (mean=33.20, std=20.58)

[2/5] Generating Correlation Heatmap for audio features...
Saved correlation heatmap to outputs/correlation_matrix.png

[3/5] EXPERIMENT 1: Pure Audio Features Baseline
      Features: danceability, energy, loudness, speechiness, acousticness,
                instrumentalness, liveness, valence, tempo, duration, key, mode
      Train samples: 71792 | Test samples: 17948
      Training Linear Regression...
      Training Ridge Regression...
      Training Lasso Regression...
      Training Decision Tree...
      Training Random Forest...

[4/5] Generating Diagnostic & Residual Visualizations...
Saved actual vs predicted plot to outputs/actual_vs_predicted.png
Saved residual plots to outputs/residual_plots.png
Saved feature importance chart to outputs/linear_reg_coefficients.png
Saved feature importance chart to outputs/feature_importance.png

[5/5] EXPERIMENT 2: Enhanced Model (Audio Features + Genre Context + Explicit)

===========================================================================
BENCHMARK RESULTS SUMMARY:
===========================================================================
                   Model              Feature Set  Train R2  Test R2  Train RMSE  Test RMSE  Train MAE  Test MAE
       Linear Regression           Audio Features    0.0320   0.0293      20.281     20.149     16.704    16.598
        Ridge Regression           Audio Features    0.0320   0.0293      20.281     20.149     16.704    16.598
        Lasso Regression           Audio Features    0.0318   0.0294      20.282     20.148     16.722    16.613
           Decision Tree           Audio Features    0.1056   0.0783      19.494     19.633     15.713    15.827
           Random Forest           Audio Features    0.2430   0.1494      17.934     18.862     14.275    15.127
Random Forest (Enhanced) Audio + Genre + Explicit    0.4933   0.4025      14.672     15.808     10.316    11.076

[OK] Summary metrics saved to: outputs\metrics_summary.csv
[OK] All visual figures saved to outputs/ directory:
     - outputs/correlation_matrix.png
     - outputs/actual_vs_predicted.png
     - outputs/residual_plots.png
     - outputs/feature_importance.png
     - outputs/linear_reg_coefficients.png
===========================================================================
Pipeline execution completed successfully!
```

---

## 6. Key Scientific Takeaways & Interpretation

1. **Acoustic Linear Limits:** Multiple Linear Regression, Ridge ($L_2$), and Lasso ($L_1$) all achieve $R^2 \approx 0.029$ with an RMSE of $\approx 20.15$. Audio attributes (loudness, tempo, danceability) have complex non-monotonic relationships with popularity that ordinary linear equations cannot capture.
2. **Non-linear Advantage:** The Decision Tree Regressor improves $R^2$ to $0.078$, and Random Forest elevates it to $0.149$ (RMSE $18.86$), demonstrating that tree splits successfully identify acoustic thresholds (e.g., loudness sweet spot between $-8$ dB and $-4$ dB).
3. **Contextual Dominance:** Music popularity is inherently cultural. Incorporating leak-free target-encoded `track_genre` and `explicit` content elevates $R^2$ to **$0.4025$** and reduces RMSE to **$15.808$**, representing a **+270% improvement** over raw audio features alone.

---

## 7. Links

- **Presentation Slides (PDF, exactly 5 slides):** [docs/Hit_Song_Popularity_Prediction_Slides.pdf](docs/Hit_Song_Popularity_Prediction_Slides.pdf)
- **Video Demonstration (≤ 5:00 min, Unlisted Link):** [https://youtu.be/placeholder-hit-song-ai101](https://youtu.be/placeholder-hit-song-ai101) *(Replace with your unlisted YouTube/Drive link)*
- **Timed Video Script & Cue Sheet:** [VIDEO_SCRIPT.md](VIDEO_SCRIPT.md)

---

## 8. AI-Use Disclosure

*In strict compliance with Course Policy (Slide 12 of AI101 Mini-Project Briefing):*

- **ChatGPT / Gemini:** Utilized for scaffolding boilerplate matplotlib residual plotting routines, suggesting color palettes, and drafting the initial skeleton of this README.
- **Team Verification:** Every line of code, data cleaning step, model hyperparameter, mathematical formula, and empirical metric was locally reviewed, tested, debugged, and validated by the team.
- **Academic Integrity Statement:** No AI tool was used to fabricate, synthesize, or alter the dataset or experimental evaluation metrics. All reported results reflect true local executions on team hardware.
