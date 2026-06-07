# Medical Inventory Sales Prediction and Segmentation

## Project Overview

This project predicts medical inventory sales (SaleTot) using machine learning and identifies inventory patterns through clustering.

## Problem Statement

Accurate sales forecasting is critical for inventory management in medical stores. Overstocking increases holding costs, while understocking leads to lost sales.

The goal of this project is to:

- Predict SaleTot
- Identify important factors affecting sales
- Segment inventory using K-Means clustering

## Dataset

The dataset was obtained from real-world medical inventory records.

Due to confidentiality agreements, the raw dataset cannot be publicly shared.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- XGBoost
- SHAP
- Matplotlib
- Seaborn

## Machine Learning Models

- Linear Regression
- Ridge Regression
- Lasso Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBoost
- Voting Regressor
- Stacking Regressor

## Model Performance

| Model | R² Score |
|---------|---------|
| Gradient Boosting | 0.7978 |
| Voting [1,3,1] | 0.7908 |
| XGBoost | 0.7684 |
| Random Forest | 0.7513 |

Best Model: Gradient Boosting Regressor

## Explainable AI

SHAP was used to understand feature importance and prediction behavior.

## Inventory Segmentation

K-Means clustering was applied to identify inventory patterns and business insights.

## Repository Structure

(Explain folders)

## Future Improvements

- Streamlit Dashboard
- Real-time Inventory Monitoring
- Automated Restocking Recommendations
