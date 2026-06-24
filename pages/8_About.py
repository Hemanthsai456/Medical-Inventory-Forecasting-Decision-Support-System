import streamlit as st

st.title("👨‍💻 About This Project")

# ==================================
# Project Overview
# ==================================

st.header("💊 Project Overview")

st.markdown("""
**Medical Inventory Forecasting & Decision Support System** is an end-to-end Machine Learning project developed to forecast medical inventory sales using historical inventory and purchase data.

The project combines predictive modeling, interactive analytics dashboards, explainable AI, inventory segmentation, and deployment into a complete business-focused decision support solution.

The final production model is a **Gradient Boosting Regressor**, selected after extensive experimentation and comparison across multiple machine learning and ensemble models.
""")

# ==================================
# Project Statistics
# ==================================

st.header("📈 Project Statistics")

col1, col2 = st.columns(2)

with col1:
    st.metric("Models Evaluated", "14")
    st.metric("Final R² Score", "0.7978")

with col2:
    st.metric("Target Variable", "SaleTot")
    st.metric("Final Model", "Gradient Boosting")

# ==================================
# Skills Demonstrated
# ==================================

st.header("🛠️ Skills Demonstrated")

st.markdown("""
### Data Analysis

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Data Validation
- Feature Engineering
- Data Storytelling

### Machine Learning

- Regression Modeling
- Ensemble Learning
- Hyperparameter Tuning
- Model Evaluation
- Model Selection
- Error Analysis & Diagnostics
            
#### Business Analytics & Decision Support

- Demand Classification
- Inventory Risk Assessment
- Procurement Recommendation Systems
- Inventory Turnover Analysis
- Business Impact Simulation
- Decision Support Analytics

### Explainable AI

- SHAP Explainability
- Feature Importance Analysis
- Prediction Interpretation

### Interactive Analytics

- Plotly Dashboards
- Executive KPI Design
- Business Insights Generation
- Interactive Data Exploration

### Business Intelligence

- Inventory Risk Assessment
- Demand Classification
- Recommendation Engine Development
- Decision Support Analytics

### Unsupervised Learning

- K-Means Clustering
- Cluster Profiling
- Inventory Segmentation
            
#### Documentation
- Technical Architecture Documentation
- Error Analysis Reporting
- Business Impact Documentation

### Deployment

- Model Serialization
- Streamlit Application Development
- Interactive Dashboard Development
- Git & GitHub Version Control
""")

# ==================================
# Tools & Technologies
# ==================================

st.header("⚙️ Tools & Technologies")

st.markdown("""
- Python
- Pandas
- NumPy
- Scikit-Learn
- XGBoost
- SHAP
- Plotly
- Matplotlib
- Streamlit
- Excel
- Git
- GitHub
""")

# ==================================
# Project Workflow
# ==================================

st.header("🔄 Project Workflow")

# Project Workflow

st.code("""
Raw Inventory Data
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis
        ↓
Feature Engineering
        ↓
Model Development
        ↓
Hyperparameter Tuning
        ↓
Model Evaluation
        ↓
Error Analysis
        ↓
SHAP Explainability
        ↓
Inventory Segmentation
        ↓
Demand Classification
        ↓
Inventory Risk Assessment
        ↓
Procurement Recommendation Engine
        ↓
Business Impact Simulation
        ↓
Interactive Dashboard Development
        ↓
Streamlit Deployment
""")


# ==================================
# Developer
# ==================================

st.header("👤 Developer")

st.markdown("""
**Charagundla Hemanth Sai**

Artificial Intelligence & Data Science

This project was developed as part of a professional machine learning portfolio focused on solving real-world inventory management and forecasting challenges using data-driven approaches.
""")

# ==================================
# Contact
# ==================================

st.header("📬 Contact")

st.markdown("""
📧 Email: hemanthsai.ch456@gmail.com

🔗 LinkedIn:
https://www.linkedin.com/in/hemanth-sai-charagundla-4a8659376/

💻 GitHub Project:
https://github.com/Hemanthsai456/Medical-Inventory-Forecasting-Decision-Support-System
""")

# ==================================
# Closing Note
# ==================================

st.success("""
This project demonstrates the complete machine learning lifecycle—from data preparation and analytics to model deployment, explainability, inventory segmentation, and business decision support.
""")