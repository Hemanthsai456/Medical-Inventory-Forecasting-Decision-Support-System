import streamlit as st

st.title("👨‍💻 About This Project")

# ==================================
# Project Overview
# ==================================

st.header("💊 Project Overview")

st.markdown("""
**Medical Inventory Sales Prediction & Segmentation** is an end-to-end Machine Learning project developed to forecast medical inventory sales using historical inventory and purchase data.

The project combines data analysis, predictive modeling, explainable AI, clustering techniques, and deployment into a complete business-focused solution.

The final production model is a **Gradient Boosting Regressor**, selected after extensive experimentation and comparison with multiple machine learning and ensemble models.
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

### Machine Learning
- Regression Modeling
- Ensemble Learning
- Hyperparameter Tuning
- Model Evaluation

### Explainable AI
- SHAP Explainability
- Feature Importance Analysis
- Prediction Interpretation

### Unsupervised Learning
- K-Means Clustering
- Cluster Profiling
- Inventory Segmentation

### Deployment
- Model Serialization
- Streamlit Application Development
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
- Matplotlib
- Seaborn
- Streamlit
- Excel
- Git
- GitHub
""")

# ==================================
# Project Workflow
# ==================================

st.header("🔄 Project Workflow")

st.code("""
Raw Inventory Data
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
Model Comparison
        ↓
SHAP Explainability
        ↓
K-Means Clustering
        ↓
Model Deployment
""")

# ==================================
# Developer
# ==================================

st.header("👤 Developer")

st.markdown("""
**Charagundla Hemanth Sai (Ch. Hemanth Sai)**

Artificial Intelligence & Data Science Student

This project was developed as part of a practical machine learning portfolio focused on solving real-world business problems using data-driven approaches.
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
https://github.com/Hemanthsai456/Medical-Inventory-Sales-Prediction
""")

# ==================================
# Closing Note
# ==================================

st.success("""
This project demonstrates the complete machine learning lifecycle:
from data preparation and analysis to model deployment and business interpretation.
""")
