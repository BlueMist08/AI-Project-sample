# 5-Minute Video Presentation Script
**Course:** AI101 - Data Science and AI Essentials with Python, sAIDE, IIT Ropar  
**Project:** Hit Song Popularity Prediction (Regression)  
**Target Duration:** Exactly 4:30 to 5:00 minutes (Strict maximum: 5:00)  
**Recommended Tools:** OBS Studio, Google Meet, Zoom, or Microsoft Teams (Record meeting with shared screen)

---

## **Video Timeline Summary**
| Timestamp | Segment | Speaker | Visual on Screen |
| :--- | :--- | :--- | :--- |
| **0:00 – 0:30** | Team Intro & Roles | **Aanya Sharma** (Doc Lead) | Slide 1 (Title & Team Roles) |
| **0:30 – 1:30** | Problem Statement & Approach | **Simran Kaur** (PPT Lead) | Slide 2 (Problem & Data) & Slide 3 (Approach) |
| **1:30 – 3:30** | Live Demonstration & Code Walkthrough | **Aaditya Chandol** (Exec Lead) & **Kabir Singh** (Video Lead) | Terminal (`python src/main.py`) & Jupyter Notebook |
| **3:30 – 4:30** | Benchmark Results & Residual Analysis | **Simran Kaur** (PPT Lead) | Slide 4 (Results & Diagnostic Charts) |
| **4:30 – 5:00** | Key Learnings, Roles & AI Disclosure | **Kabir Singh** (Video Lead) | Slide 5 (Learnings & AI Disclosure) |

---

## **Detailed Speaking Script (Line-by-Line)**

### **Segment 1: Team Introduction & Roles (0:00 – 0:30)**
**Visual:** Show Slide 1 (*Hit Song Popularity Prediction: Title & Team Table*).  
**Speaker:** **Aanya Sharma** (Documentation Lead)

> *"Hello respected professors and TAs. We are Team 17 from AI101: Data Science and AI Essentials with Python at the School of AI and Data Engineering, IIT Ropar.*  
> *Our project is **Hit Song Popularity Prediction using Regression**.*  
> *Before we dive in, let us introduce our four leads:*  
> *- I am **Aanya Sharma**, the Documentation Lead, responsible for GitHub curation, repository structure, and the project README.*  
> *- **Aaditya Chandol** is our Execution and Reproducibility Lead, overseeing environment dependencies, requirements, and the clean pipeline runner.*  
> *- **Simran Kaur** is our PPT and Visualization Lead, who engineered our 5-slide deck and diagnostic plots.*  
> *- And **Kabir Singh** is our Video and Demonstration Lead, presenting our Jupyter Notebook and live run.*  
> *All four of us contributed actively to writing and committing code in our repository. I will now hand over to Simran to explain our problem statement and dataset."*

---

### **Segment 2: Problem Statement & Approach (0:30 – 1:30)**
**Visual:** Switch to Slide 2 (*Problem Definition and Dataset Overview*), then Slide 3 (*ML Pipeline*).  
**Speaker:** **Simran Kaur** (PPT & Visualization Lead)

> *(On Slide 2)*  
> *"Thank you, Aanya. In today's music streaming ecosystem, over 100,000 new songs are uploaded daily. Our goal is to predict a song's popularity score—a continuous target ranging from 0 to 100—using raw audio characteristics extracted from the Spotify Web API.*  
> *We analyzed the Spotify Tracks Dataset containing 114,000 tracks across 114 genres. After dropping 24,000 duplicate tracks across genre tags, our deduplicated dataset contains 89,740 unique songs.*  
> *Our core question is: Can intrinsic acoustic signals—such as danceability, energy, loudness, tempo, acousticness, and instrumentalness—accurately forecast a track's commercial success?*  
> 
> *(Switch to Slide 3)*  
> *To investigate this, we designed a rigorous machine learning pipeline:*  
> *First, we standardize continuous acoustic signals using scikit-learn's `StandardScaler` to prevent feature dominance.*  
> *Second, we split data into an 80% training set and a 20% test set with a fixed random seed for strict reproducibility.*  
> *Third, we benchmark multiple regression algorithms spanning linear and non-linear paradigms: Multiple Linear Regression as our OLS baseline, Ridge Regression with L2 regularization, Lasso Regression with L1 sparsity, Decision Tree Regressor, and Random Forest Regressor.*  
> *Now, Aaditya and Kabir will demonstrate our code running live from the repo."*

---

### **Segment 3: Live Code Demonstration & Notebook Walkthrough (1:30 – 3:30)**
**Visual:** Share terminal screen showing repository folder, run command, then switch to `Hit_Song_Popularity_Prediction.ipynb`.  
**Speaker 1:** **Aaditya Chandol** (Execution Lead) [1:30 – 2:30]

> *(In Terminal)*  
> *"Thanks, Simran. As the Execution Lead, ensuring fresh-clone reproducibility was my top priority.*  
> *Here you can see our clean repository structure: our dataset lives in `data/`, modular code in `src/`, notebooks in `notebooks/`, and generated outputs in `outputs/`.*  
> *To run our entire pipeline end-to-end, a TA or evaluator only needs to run one command:*  
> *(Type and run)* `python src/main.py`  
> *(Point at terminal output)*  
> *As you can see, the script automatically loads the data, cleans duplicates, computes correlations, trains all five regression models, prints our benchmark evaluation table, and exports all figures in under 45 seconds using relative paths."*

**Speaker 2:** **Kabir Singh** (Video & Demo Lead) [2:30 – 3:30]

> *(Switch to Jupyter Notebook: `Hit_Song_Popularity_Prediction.ipynb`)*  
> *"Now let's examine our interactive Jupyter Notebook where all cells and visualizations are pre-computed.*  
> *In Section 4, our correlation heatmap reveals crucial domain insights: loudness has the highest positive correlation with popularity (+0.07), while instrumentalness has the strongest negative correlation (-0.13), indicating commercial listeners heavily prefer vocal-driven music.*  
> *In Section 7 and 8, we compare feature weights. Notice how our Decision Tree and Random Forest non-parametrically split on loudness and tempo thresholds.*  
> *In Section 9, we inspect our residual plots. Rather than a purely homoscedastic band, the residuals show higher variance in the mid-popularity range (30-50), which directly motivates our enhanced feature modeling where we integrate genre context."*

---

### **Segment 4: Results & Benchmark Numbers (3:30 – 4:30)**
**Visual:** Switch to Slide 4 (*Experimental Results & Model Diagnostics*).  
**Speaker:** **Simran Kaur** (PPT & Visualization Lead)

> *"Returning to our quantitative results on our 17,948-track test set:*  
> *- Multiple Linear Regression achieved an $R^2$ of **0.029** and an RMSE of **20.15**.*  
> *- Ridge and Lasso regressions produced virtually identical metrics ($R^2 \approx 0.029$), demonstrating that collinearity was not the bottleneck; rather, the underlying relationship is fundamentally non-linear.*  
> *- Moving to tree models, our Decision Tree Regressor increased $R^2$ to **0.078**.*  
> *- Random Forest further doubled this, achieving $R^2 = \mathbf{0.149}$ and reducing RMSE to **18.86**.*  
> *- Finally, in Experiment 2, when we incorporated track genre context via leak-free target encoding, our Random Forest surged to an $R^2$ of **0.403** and an RMSE of **15.81**—a nearly 3x increase in predictive capability!*  
> *Our diagnostic scatter plots on the right confirm that while acoustic features establish a baseline, cultural and genre categorization is essential for commercial popularity."*

---

### **Segment 5: Learnings, Contributions & AI-Use Disclosure (4:30 – 5:00)**
**Visual:** Switch to Slide 5 (*Learnings, Contributions & AI Disclosure*).  
**Speaker:** **Kabir Singh** (Video & Demo Lead)

> *"To conclude with our key learnings and reflections:*  
> *First, what didn't work was assuming linear relationships between audio attributes and hit potential. Viral songs encompass both quiet acoustic ballads and high-octane electronic tracks.*  
> *Second, what worked remarkably was non-linear ensemble modeling and contextual feature enrichment.*  
> *Regarding individual contributions:*  
> *- Aanya led our repository structure and README documentation;*  
> *- Aaditya engineered the execution pipeline and environment reproducibility;*  
> *- Simran produced our 5 slides and diagnostic visual analytics;*  
> *- And I led our notebook execution and video presentation.*  
> *Finally, as disclosed on Slide 5 and in our README, we utilized AI assistants (ChatGPT and Gemini) for brainstorming residual plotting boilerplate and proofreading documentation. All underlying mathematical models, scikit-learn code, and empirical results were rigorously evaluated, verified, and executed locally by our team.*  
> *Thank you for your time, and we look forward to your questions!"*
