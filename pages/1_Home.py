import streamlit as st

st.title("💊 Medical Inventory Sales Prediction & Segmentation")

st.markdown("""
### Project Overview

This project predicts total sales (SaleTot) for medical inventory items using Machine Learning.

### Problem Statement

Medical stores often struggle with inventory planning and sales forecasting.
Overstocking increases holding costs while understocking leads to missed sales opportunities.

This project uses historical inventory and purchase information to predict future sales.

### Target Variable

**SaleTot**

### Final Model

**Gradient Boosting Regressor**

### Model Performance

**R² Score = 0.798**

### Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- XGBoost
- SHAP
- K-Means Clustering
- Streamlit

### Business Value

- Better inventory planning
- Reduced stock wastage
- Improved procurement decisions
- Data-driven forecasting
""")
