import streamlit as st

st.title("💊 Medical Inventory Sales Prediction")

st.markdown("""
### Project Overview

Medical Inventory Sales Prediction is an end-to-end Machine Learning application designed to forecast medical inventory sales and support inventory management decisions.

The project combines predictive analytics, interactive dashboards, explainable AI, and inventory segmentation to transform raw inventory data into actionable business insights.

### Problem Statement

Medical inventory management is challenging due to demand uncertainty, overstocking risks, and stockout situations.

- Overstocking increases inventory carrying costs.
- Understocking can lead to missed sales opportunities.
- Manual forecasting often lacks accuracy and consistency.

This project uses historical inventory and procurement data to predict future sales demand and support data-driven inventory planning.

### Target Variable

**SaleTot (Total Sales Quantity)**

### Final Model

**Gradient Boosting Regressor**

### Model Performance

**R² Score = 0.798**

### Application Features

#### 📊 Interactive Analytics Dashboard

- Dynamic filtering
- Executive KPI monitoring
- Interactive Plotly visualizations
- Inventory risk analysis
- Business insights & executive summaries

#### 🔮 Sales Prediction Engine

- Gradient Boosting Regressor
- Demand classification
- Inventory risk assessment
- Business recommendation engine
- Inventory turnover analysis

#### 🧠 Explainable AI

- SHAP Summary Analysis
- SHAP Waterfall Analysis
- Feature Importance Ranking
- Business-focused model interpretation

#### 📦 Inventory Segmentation

- K-Means Clustering
- Cluster Profiling
- Inventory Categorization
- Inventory Strategy Insights

### Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- XGBoost
- SHAP
- Plotly
- K-Means Clustering
- Streamlit

### Business Value

- Better inventory planning
- Reduced stock wastage
- Improved procurement decisions
- Demand forecasting support
- Inventory risk identification
- Data-driven decision making
""")