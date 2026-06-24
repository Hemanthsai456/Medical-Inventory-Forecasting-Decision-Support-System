# 💊 Medical Inventory Forecasting & Decision Support System

## 🚀 Live Demo

🔗 Streamlit Application:

https://hemanthsai-medical-inventory-decision-support.streamlit.app/

🔗 GitHub Repository:

https://github.com/Hemanthsai456/Medical-Inventory-Forecasting-Decision-Support-System

---

## 📚 Project Documentation

This project includes detailed technical and business documentation:

- Technical Architecture Report
- Error Analysis Report
- Business Impact Report
- Model Performance Report

These reports provide additional insight into model behavior, forecasting performance, business workflows, and system architecture.

---

## 📌 Project Overview

Medical Inventory Forecasting & Decision Support System is an end-to-end Machine Learning and Analytics project developed to forecast medical inventory sales and support inventory management decisions through data-driven insights.

The project combines predictive modeling, interactive analytics dashboards, explainable AI, inventory segmentation, and business recommendation systems into a complete decision-support application.

The final solution helps identify demand patterns, inventory risks, procurement opportunities, and sales drivers while improving forecasting accuracy and inventory planning.

The project integrates:

* Exploratory Data Analysis (EDA)
* Interactive Analytics Dashboard
* Executive KPI Monitoring
* Sales Forecasting using Machine Learning
* Feature Importance Analysis
* Explainable AI (SHAP)
* Business Recommendation Engine
* Demand Classification
* Inventory Risk Assessment
* Inventory Turnover Analysis
* K-Means Inventory Segmentation
* Interactive Streamlit Deployment

<p align="center">
  <img src="images\home_page.png" width="100%">
</p>

---

## 🎯 Problem Statement

Medical inventory management is a critical operational challenge where inaccurate forecasting can directly impact product availability, inventory costs, and business performance.

Organizations frequently struggle to maintain optimal inventory levels due to fluctuating demand patterns and procurement uncertainty.

### Business Challenges

* Overstocking increases inventory carrying costs and capital lock-in.
* Understocking leads to missed sales opportunities and customer dissatisfaction.
* Demand forecasting is difficult using manual estimation techniques.
* Inventory behavior varies significantly across products and suppliers.
* Inventory managers often lack visibility into demand drivers and stock risks.

### Project Objectives

* Predict total sales (`SaleTot`) using machine learning.
* Identify the most influential inventory variables affecting demand.
* Explain model predictions using SHAP Explainable AI.
* Categorize products into inventory segments using clustering.
* Support inventory planning through actionable business recommendations.
* Provide interactive analytics for operational decision-making.

---

## ⚙️ Technology Stack

### Programming & Data Processing

* Python
* Pandas
* NumPy

### Data Visualization

* Plotly
* Matplotlib
* Seaborn

### Machine Learning

* Scikit-Learn
* XGBoost

### Explainable AI

* SHAP

### Interactive Application

* Streamlit

### Version Control

* Git
* GitHub

### Deployment

* Streamlit Community Cloud

---

## 🔄 Project Workflow

```text
Medical Inventory Data
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis
        ↓
Feature Engineering
        ↓
Model Training
        ↓
Hyperparameter Tuning
        ↓
Model Evaluation
        ↓
Model Comparison
        ↓
Feature Importance Analysis
        ↓
SHAP Explainability
        ↓
K-Means Clustering
        ↓
Interactive Dashboard Development
        ↓
Business Recommendation Engine
        ↓
Streamlit Deployment

```

---
## 📈 Exploratory Data Analysis

Exploratory Data Analysis (EDA) was performed to understand inventory behavior, identify demand patterns, evaluate supplier performance, and uncover opportunities for inventory optimization.

### Key Analyses

* Fast Moving Products
* High Turnover Companies
* Inventory Hoarding Analysis
* Purchase vs Sales Analysis
* Stock vs Sales Analysis
* Inventory Value Distribution
* Inventory Exposure Analysis
* Overstocked Product Identification

### Business Insights

* Fast-moving products were identified for replenishment planning.
* Overstocked inventory was detected for cost reduction opportunities.
* Supplier performance patterns were analyzed.
* Inventory utilization trends were discovered.
* High inventory exposure products were identified for monitoring.
* Demand concentration patterns were uncovered.

---

## 📊 Interactive Analytics Dashboard

The original static EDA reports were transformed into an interactive analytics dashboard using Plotly and Streamlit.

The dashboard allows users to dynamically explore inventory behavior through filters, KPIs, and interactive visualizations.

### Dashboard Features

#### Executive KPI Monitoring

* Total Products
* Total Companies
* Total Sales Units
* Inventory Value
* Inventory Turnover
* Stock-to-Sales Ratio
* Overstock Risk Indicators

#### Interactive Analytics

* Dynamic Company Filtering
* Product Type Filtering
* Product-Level Analysis
* Interactive Plotly Charts
* Inventory Distribution Analysis
* Inventory Exposure Analysis

#### Executive Insights

* Fastest Moving Products
* Top Performing Companies
* Inventory Exposure Monitoring
* Executive Summary & Action Recommendations

### Business Value

* Faster operational analysis
* Improved inventory visibility
* Better procurement planning
* Enhanced inventory risk monitoring
* Data-driven decision support

---

## 🤖 Machine Learning Models Evaluated

Multiple machine learning and ensemble learning approaches were evaluated to identify the most effective model for medical inventory sales forecasting.

### Tree-Based Models

* Random Forest Regressor
* Gradient Boosting Regressor
* XGBoost Regressor

### Voting Ensembles

* Voting [1,1,1]
* Voting [1,3,2]
* Voting [1,4,2]
* Voting [1,5,3]
* Voting [2,5,3]

### Stacking Ensembles

* Stacking LR
* Stacking Ridge
* Stacking Lasso
* Stacking RF
* Stacking GBR
* Stacking XGB

### Model Evaluation Metrics

* R² Score
* RMSE
* MAE

A total of **14 machine learning and ensemble models** were trained, tuned, and evaluated.

The final production model was selected based on predictive accuracy, error minimization, and generalization performance.

---

## 🏆 Final Model Performance

### Selected Model

**Gradient Boosting Regressor**

| Metric | Value |
|----------|----------|
| R² Score | 0.7978 |
| RMSE | 9.692 |
| MAE | 4.415 |

### Why Gradient Boosting?

* Highest R² Score
* Lowest RMSE
* Lowest MAE
* Strong Generalization Performance
* Stable Forecasting Behavior
* Consistent Prediction Accuracy

The Gradient Boosting Regressor consistently outperformed all competing models and was selected as the final production model for deployment.

---

## 📉 Error Analysis

Model evaluation extended beyond traditional performance metrics to understand forecasting behavior across different demand scenarios.

### Key Findings

- Low and medium demand products achieved strong prediction accuracy.
- Prediction error increased for high-demand products and demand spikes.
- Most large prediction errors occurred during extreme inventory situations.
- Residual analysis showed generally stable prediction behavior across the majority of observations.

### Error Analysis Components

- Demand Group Performance Analysis
- Top 20 Prediction Error Investigation
- Residual Distribution Analysis
- Actual vs Predicted Evaluation
- Model Limitation Assessment

These analyses helped validate model reliability and identify opportunities for future forecasting improvements.

---

## 📌 Feature Importance Analysis

Feature importance analysis was performed using the final tuned Gradient Boosting Regressor to understand which variables most strongly influenced sales predictions.

### Most Influential Features

1. OStk (Opening Stock)
2. PurTot (Purchase Total)
3. QohValue (Inventory Value)
4. Packing
5. Product Type Features

### Key Findings

* Inventory-related variables contributed the majority of predictive power.
* Opening Stock emerged as the strongest sales predictor.
* Purchase Quantity significantly influenced demand forecasts.
* Product category information provided additional predictive value.
* Inventory behavior was a stronger predictor than product classification alone.

These findings helped validate the model's learning behavior and business relevance.

---

## 🧠 Explainable AI (SHAP)

SHAP (SHapley Additive exPlanations) was implemented to improve model transparency and explain prediction behavior.

### Implemented Explainability Techniques

* SHAP Summary Plot
* SHAP Waterfall Plot
* Feature Ranking Analysis
* Business-Oriented Interpretation

### Explainability Objectives

* Understand global model behavior.
* Explain individual predictions.
* Identify the strongest demand drivers.
* Improve stakeholder trust in forecasts.

### Key Insights

* Opening Stock (OStk) is the strongest predictor of future sales.
* Purchase Quantity (PurTot) significantly influences forecasting behavior.
* Inventory-related variables dominate model decisions.
* Product-type variables provide secondary predictive influence.

### Business Value

Explainability enables inventory managers to understand why forecasts are generated and which operational factors drive predicted demand.

---

## 📦 Inventory Segmentation

K-Means Clustering was applied to identify groups of products with similar inventory and sales characteristics.

This unsupervised machine learning approach enables inventory managers to better understand inventory behavior and develop targeted inventory strategies.

### Cluster Profiles

#### Cluster 0 – Low-Demand Products

* Low sales volume
* Slow inventory turnover
* Lower replenishment priority
* Requires periodic monitoring

#### Cluster 1 – Fast-Moving Products

* High sales volume
* Frequent stock movement
* Strong customer demand
* High replenishment priority

#### Cluster 2 – High-Value Products

* High inventory value
* Significant financial exposure
* Requires careful inventory monitoring
* Important for inventory optimization

#### Cluster 3 – Bulk & Moderate-Demand Products

* Moderate sales demand
* Larger inventory quantities
* Supports routine inventory operations
* Occasional high-volume transactions

### Business Value

* Inventory Optimization
* Demand Forecasting Support
* Better Stock Planning
* Resource Allocation
* Inventory Risk Reduction
* Segment-Based Inventory Strategies

The clustering process successfully identified four distinct inventory groups, enabling more targeted inventory management decisions.

---

---

## Inventory Segmentation page

<p align="center">
  <img src="images\inventory_segmentation1.png" width="100%">
</p>

<p align="center">
  <img src="images\inventory_segmentation2.png" width="100%">
</p>

<p align="center">
  <img src="images\inventory_segmentation3.png" width="100%">
</p>

---

## 🚀 Streamlit Dashboard

The project was deployed as a multi-page interactive Streamlit application that combines analytics, forecasting, explainability, and inventory segmentation into a single business-focused platform.

### Dashboard Pages

* Home
* Interactive Analytics Dashboard
* Sales Prediction
* Model Comparison
* Explainable AI (SHAP)
* Inventory Segmentation
* About

### Dashboard Capabilities

#### Interactive Analytics Dashboard

* Executive KPI Monitoring
* Interactive Plotly Visualizations
* Dynamic Filtering
* Inventory Exposure Analysis
* Executive Business Insights

#### Sales Prediction Engine

* Sales Forecasting
* Demand Classification
* Inventory Risk Assessment
* Business Recommendation Engine
* Inventory Turnover Analysis

### Decision Support Workflow

Inventory Data
↓
Sales Prediction
↓
Demand Classification
↓
Inventory Risk Assessment
↓
Procurement Recommendation
↓
Inventory Planning Decision

The application converts machine learning forecasts into operational recommendations, enabling inventory managers to move from prediction to action.

#### Explainable AI

* SHAP Summary Analysis
* SHAP Waterfall Analysis
* Feature Ranking
* Business Interpretation

#### Inventory Segmentation

* K-Means Clustering
* Cluster Profiling
* Inventory Categorization

The deployed application transforms machine learning outputs into actionable inventory management insights.

---

## 📂 Repository Structure

```text
Medical-Inventory-Sales-Prediction/

├── app.py
├── pages/
│   ├── 1_Home.py
│   ├── 2_EDA_Dashboard.py
│   ├── 3_Prediction.py
│   ├── 4_Model_Comparison.py
│   ├── 5_Explainable_AI.py
│   ├── 6_Error Analysis.py
│   ├── 7_Inventory_Segmentation.py
│   └── 8_About.py
│
├── utils/
│   ├── prediction.py
│   └── history.py
│
├── models/
│   ├── medical_inventory_gb_model.pkl
│   ├── model_columns.pkl
│   └── dashboard_data.pkl
├── documentation/
│   ├── error_analysis/
│   ├── Business_Impact_Report.md
│   └── Technical_Architecture.md
│
├── images/
├── notebooks/
├── requirements.txt
└── README.md

```
---

## 📦 Pretrained Models

The repository includes pre-trained model files required for inference and dashboard functionality.

---

## 🔮 Prediction Recommendation Engine

The prediction module extends beyond forecasting by translating model outputs into inventory management recommendations.

<p align="center">
  <img src="images\prediction_page.png" width="100%">
</p>

### Prediction Features

* Sales Forecasting
* Demand Classification
* Inventory Risk Assessment
* Inventory Turnover Analysis
* Business Recommendations

### Demand Categories

* High Demand
* Medium Demand
* Low Demand

### Inventory Risk Categories

* Stockout Risk
* Balanced Inventory
* Overstock Risk

### Business Recommendations

The application automatically generates inventory management recommendations based on predicted demand and inventory conditions.

Examples include:

* Increase procurement
* Maintain inventory levels
* Monitor inventory closely
* Reduce future purchases

This transforms the project from a forecasting model into a business decision-support system.

---

## 🚀 Future Improvements

Potential future enhancements include:

### Backend & Data Engineering

* SQLite Integration
* PostgreSQL Migration
* Prediction Monitoring
* Data Versioning

### API Development

* FastAPI Integration
* Prediction API Endpoints
* Analytics API Services

### MLOps

* Docker Containerization
* CI/CD Automation
* Model Monitoring
* Automated Testing

### Cloud Deployment

* AWS Deployment
* Azure Deployment
* GCP Deployment

### Explainability Enhancements

* Interactive SHAP Visualizations
* User-Specific Prediction Explanations
* Dynamic Explainability Dashboards

These improvements were intentionally left outside the current project scope to maintain focus on the core machine learning and analytics solution.

---

## ⭐ Project Highlights

* End-to-End Machine Learning Pipeline
* Real-World Medical Inventory Forecasting Use Case
* 14 Machine Learning & Ensemble Model Comparisons
* Hyperparameter Tuning & Model Selection
* Gradient Boosting Regressor Deployment
* Interactive Analytics Dashboard
* Executive KPI Monitoring
* Demand Classification Framework
* Inventory Risk Assessment Engine
* Procurement Recommendation System
* Inventory Turnover Analysis
* Model-Assisted Decision Support Workflow
* Business Impact Simulation
* Error Analysis & Model Diagnostics
* Demand Group Performance Analysis
* Residual Analysis & Prediction Error Investigation
* SHAP Explainable AI
* Feature Importance Analysis
* K-Means Inventory Segmentation
* Cluster Profiling & Inventory Strategy Analysis
* Multi-Page Streamlit Application
* Streamlit Cloud Deployment
* Technical Architecture Documentation
* Business Impact Documentation
* Error Analysis Documentation
* Confidential Real-World Dataset Handling
* Business Decision Support Analytics
* Portfolio-Ready Production Deployment

---

## 🚀 Installation & Usage

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Hemanthsai456/Medical-Inventory-Sales-Prediction.git
cd Medical-Inventory-Sales-Prediction
```

### 2️⃣ Create a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
streamlit run app.py
```

### 5️⃣ Open in Browser

```text
http://localhost:8501
```

---

## 🔄 Reproducing the Analysis

To reproduce the complete machine learning workflow:

Open:

```text
notebooks/
└── Medical_Inventory.ipynb
```

Execute the notebook sequentially.

> Note: The original dataset is not included due to confidentiality requirements.

---

## 🔒 Data Privacy

The dataset used in this project was obtained from real-world medical inventory operations.

To respect confidentiality agreements and business privacy requirements, the raw dataset is not included in this repository.

All visualizations, trained models, and analysis outputs have been shared without exposing sensitive business information.

---

## 👨‍💻 Author

**Charagundla Hemanth Sai (Ch. Hemanth Sai)**

Artificial Intelligence & Data Science Student

📧 Email: [hemanthsai.ch456@gmail.com](mailto:hemanthsai.ch456@gmail.com)

🔗 LinkedIn:

https://www.linkedin.com/in/hemanth-sai-charagundla-4a8659376/

💻 GitHub:

https://github.com/Hemanthsai456