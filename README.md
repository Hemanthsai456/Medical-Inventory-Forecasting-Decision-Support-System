# 💊 Medical Inventory Forecasting & Decision Support System

**ML-powered demand forecasting for medical inventory — turns 14 model comparisons and SHAP explainability into procurement decisions a hospital manager can actually act on.**

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)](https://hemanthsai-medical-inventory-decision-support.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Scikit--Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=flat-square)
![XGBoost](https://img.shields.io/badge/XGBoost-Boosting-red?style=flat-square)
![SHAP](https://img.shields.io/badge/SHAP-Explainable%20AI-purple?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

[**🌐 Try the live app**](https://hemanthsai-medical-inventory-decision-support.streamlit.app/) · [Repository](https://github.com/Hemanthsai456/Medical-Inventory-Forecasting-Decision-Support-System)

![Home page](https://github.com/Hemanthsai456/Medical-Inventory-Forecasting-Decision-Support-System/raw/main/images/home_page.png)

---

## The Problem

Medical inventory managers routinely overstock (tying up capital) or understock (risking stockouts) because demand forecasting is manual and reactive. Specifically, they deal with:

- Demand uncertainty with no data-driven forecast to plan against
- Overstocking and excess carrying costs
- Stockout risk on fast-moving items
- Manual, spreadsheet-based forecasting that doesn't scale
- Inefficient procurement planning
- Little visibility into *why* inventory behaves the way it does

This project replaces guesswork with a model that predicts demand, explains *why* it predicted that, flags inventory risk, and recommends what to procure next.

## Results

| Metric | Value |
|---|---|
| **Model** | Gradient Boosting Regressor (best of 14 models tested) |
| **R² Score** | **0.7978** |
| **RMSE** | 9.692 |
| **MAE** | 4.415 |

Benchmarked against Random Forest, XGBoost, and 11 voting/stacking ensembles — Gradient Boosting won on accuracy *and* generalization stability across demand categories.

## What It Does

- **Forecasts demand** from historical inventory/procurement data using the tuned Gradient Boosting model
- **Explains every prediction** with SHAP (global feature importance + per-prediction waterfall plots) — top drivers are opening stock, purchase quantity, and inventory value
- **Segments inventory** into fast-moving, low-demand, high-value, and bulk categories via K-Means clustering
- **Runs error diagnostics** — residual analysis, demand-group breakdowns, and outlier investigation to know where the model is (and isn't) reliable
- **Recommends procurement actions** — converts forecasts into risk flags and inventory planning decisions, not just numbers
- Ships as a deployed, multi-page **Streamlit** dashboard, not a notebook

## Key Insights from EDA

Before modeling, exploratory analysis on inventory and sales data surfaced several operational findings that shaped the rest of the project:

- Identified fast-moving vs. slow-moving products by comparing purchase and sales volume
- Flagged overstocked and high-inventory-exposure products through stock-vs-sales analysis
- Surfaced supplier/company-level sales performance differences
- Quantified inventory turnover to prioritize replenishment

These findings fed directly into feature engineering and later became the basis for the K-Means segmentation layer.

## Tech Stack

`Python` · `Pandas` / `NumPy` · `Scikit-Learn` · `XGBoost` · `SHAP` · `Plotly` / `Matplotlib` / `Seaborn` · `Streamlit` · deployed on **Streamlit Community Cloud**

## Workflow

```
Raw inventory data
        ↓
Data cleaning & validation
        ↓
Exploratory data analysis
        ↓
Feature engineering (+ leakage checks)
        ↓
14 models trained, tuned & compared
        ↓
Gradient Boosting selected as production model
        ↓
SHAP explainability
        ↓
K-Means inventory segmentation
        ↓
Procurement recommendations
        ↓
Deployed as a multi-page Streamlit app
```

## Project Structure

```text
src/
├── data_processing.py
├── eda.py
├── feature_engineering.py
├── modeling.py
├── error_analysis.py
├── explainability.py
├── clustering.py
└── model_persistence.py

notebooks/
├── 01_Medical_Inventory.ipynb
├── 02_model_development.ipynb
├── 03_error_analysis.ipynb
├── 04_explainability.ipynb
└── 05_clustering.ipynb

app.py + pages/     → Streamlit application
models/             → Trained model artifacts
```

---

## Technical Deep Dive

### Model Selection — 14 Models Benchmarked

Trained and tuned three tree-based models plus 11 voting/stacking ensembles, evaluated on R², RMSE, and MAE:

| Model Family | Models Tested |
|---|---|
| Tree-based | Random Forest, Gradient Boosting, XGBoost |
| Voting ensembles | 5 weighted combinations (e.g. `[1,1,1]`, `[2,5,3]`) of the tree-based models |
| Stacking ensembles | Linear Regression, Ridge, Lasso, Random Forest, Gradient Boosting, XGBoost as meta-learners |

**Gradient Boosting Regressor won** on all three metrics (R² 0.80, RMSE 9.69, MAE 4.42) and generalized more stably across demand categories than the ensembles — extra model complexity didn't buy extra accuracy here, which is itself a useful finding to report to stakeholders.

### Explainability (SHAP)

Used SHAP summary and waterfall plots to make the model's reasoning auditable — important in a healthcare-adjacent context where "trust the black box" isn't good enough. Top global drivers of predicted demand, in order:

1. Opening Stock (`OStk`)
2. Purchase Quantity (`PurTot`)
3. Inventory Value (`QohValue`)
4. Packing
5. Product-type features

Waterfall plots break down individual predictions so a procurement manager can see *why* the model flagged a specific product as high-risk, not just that it did.

### Data Leakage Checks

Before training, features were audited for **target leakage** — dropping/reworking any field that was mathematically derived from or directly encoded the target (e.g. quantities that only exist *after* a sale is recorded). Checked the remaining feature set for high correlation with the target beyond what's explainable by genuine predictive signal, and didn't find other leakage sources once the directly-derived fields were removed.

**Known limitation:** train/test splitting was not done on a temporal or grouped basis, so split-level leakage (e.g. the same product appearing in both sets) hasn't been explicitly ruled out — a fix to make the split time-aware is a natural next step.

![SHAP feature importance](https://github.com/Hemanthsai456/Medical-Inventory-Forecasting-Decision-Support-System/raw/main/images/EDA_images/stock_vs_sales.png)

### Error Analysis & Diagnostics

Went beyond aggregate metrics to find *where* the model fails:

- **Demand-group breakdown** — strong performance on low/medium-demand products; error grows on high-demand spikes
- **Residual analysis** — distribution and scatter checks confirmed generally stable, non-systematic error patterns
- **Outlier investigation** — used IQR-based detection + business-context validation on extreme values; confirmed they were real high-demand events, not data errors, and kept them in training rather than dropping them (a judgment call documented in the [Error Analysis Report](documentation/error_analysis_report.md))

### Inventory Segmentation (K-Means)

Clustered products into four operational groups — low-demand, fast-moving, high-value, and bulk/moderate-demand — so planning decisions aren't based on forecast alone. Segmentation adds business context the point-forecast can't: two products with similar predicted demand can need very different procurement strategies depending on value and turnover.

![Inventory segmentation](https://github.com/Hemanthsai456/Medical-Inventory-Forecasting-Decision-Support-System/raw/main/images/inventory_segmentation1.png)

### From Prediction to Decision

The app doesn't stop at a forecast number — it runs each prediction through a decision layer: demand classification → inventory risk assessment → procurement recommendation → simulated business impact. That's the "decision support" half of the project, documented in full in the [Business Impact Report](documentation/Business_Impact_Report.md).

![Prediction & decision support page](https://github.com/Hemanthsai456/Medical-Inventory-Forecasting-Decision-Support-System/raw/main/images/prediction_page.png)

---

## Streamlit Application

Everything above is shipped as one deployed, multi-page app rather than scattered notebooks:

| Page | What it does |
|---|---|
| 🏠 **Home** | Project overview and business framing |
| 📊 **Interactive Dashboard** | Executive KPIs, dynamic filters, company/product-level trend analysis (Plotly) |
| 🔮 **Prediction & Decision Support** | Takes inventory inputs → produces a sales forecast → classifies demand → assesses inventory risk → recommends a procurement action |
| 🤖 **Model Comparison** | All 14 trained models compared side by side on R², RMSE, MAE |
| 🧠 **Explainable AI** | SHAP summary and waterfall plots for global and per-prediction interpretation |
| 📦 **Inventory Segmentation** | K-Means cluster profiles and the strategy tied to each segment |
| 📉 **Error Analysis** | Residual plots, demand-group error breakdown, outlier investigation |
| ℹ️ **About** | Workflow and tech stack summary |

## Run It Locally

```bash
git clone https://github.com/Hemanthsai456/Medical-Inventory-Forecasting-Decision-Support-System.git
cd Medical-Inventory-Forecasting-Decision-Support-System
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Development workflows are organized across the notebooks in `notebooks/`.

## Data Privacy

This project was built on real-world medical inventory data belonging to the data owner, who asked that it not be shared publicly. In line with that:

- The raw dataset is **not included** in this repository
- Notebooks, trained models, dashboards, and visualizations are published with all business-sensitive/identifying information excluded
- Everything runnable here (code, app, docs) works without needing the original data

## Documentation

| Document | Covers |
|---|---|
| [Technical Architecture](documentation/Technical_Architecture.md) | System design, ML pipeline, and deployment overview |
| [Error Analysis Report](documentation/error_analysis_report.md) | Residuals, demand-group evaluation, and outlier investigation |
| [Business Impact Report](documentation/Business_Impact_Report.md) | Procurement workflows and the decision-support framework |

## What's Next

- Abalation and Feature Analysis
- Prediction usage tracking
- Deploy Model and Dockerize
- Seasonal demand forecasting
- Demand spike detection
- Forecast drift monitoring
- Time-aware train/test splitting to rule out split-level leakage
- Automated inventory policy recommendations
- Root-cause analysis for extreme forecasts
- Scenario / what-if simulation for inventory planning

---

**Charagundla Hemanth Sai** — AI & Data Science
[LinkedIn](https://www.linkedin.com/in/hemanth-sai-charagundla-4a8659376/)

[GitHub](https://github.com/Hemanthsai456)

hemanthsai.ch456@gmail.com
