import streamlit as st

st.set_page_config(
    page_title="Medical Inventory Sales Prediction & Segmentation",
    page_icon="💊",
    layout="wide"
)

st.title("💊 Medical Inventory Sales Prediction & Segmentation")

st.markdown("""
### End-to-End Machine Learning Project

Predicting medical inventory sales using advanced machine learning, explainable AI, and inventory segmentation techniques.
""")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Final Model", "Gradient Boosting")

with col2:
    st.metric("R² Score", "0.7978")

with col3:
    st.metric("Models Evaluated", "14")

with col4:
    st.metric("Target", "SaleTot")

st.divider()

st.header("📌 Project Overview")

st.markdown("""
Medical inventory management is critical for maintaining stock availability while minimizing inventory costs.

This project uses historical inventory and purchase information to predict future sales, identify key sales drivers using SHAP Explainability, and segment products using K-Means Clustering for better inventory planning.

### Key Components

- 📊 Exploratory Data Analysis
- 🤖 Machine Learning Models
- ⚙️ Hyperparameter Tuning
- 📌 Feature Importance Analysis
- 🧠 SHAP Explainability
- 📦 K-Means Inventory Segmentation
- 🚀 Streamlit Deployment
""")

st.divider()

st.header("🗺️ Project Workflow")

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
Deployment
""")

st.success(
    "Use the sidebar to explore EDA, predictions, model performance, explainability, inventory segmentation, and project details."
)
