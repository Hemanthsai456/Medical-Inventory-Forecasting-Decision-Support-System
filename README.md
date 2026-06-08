# 💊 Medical Inventory Sales Prediction & Segmentation

## 🚀 Live Demo

🔗 Streamlit Application:

https://hemanthsai-medical-sales-inventory-prediction.streamlit.app/

🔗 GitHub Repository:

https://github.com/Hemanthsai456/Medical-Inventory-Sales-Prediction

---

## 📌 Project Overview

Medical inventory management is a critical business function that directly impacts product availability, operational efficiency, and profitability. Poor inventory planning can lead to overstocking, increased holding costs, product expiration, and lost sales opportunities.

This project leverages Machine Learning and Data Analytics techniques to predict medical inventory sales and identify inventory patterns that support data-driven business decision-making.

The project combines:

* Exploratory Data Analysis (EDA)
* Sales Forecasting using Machine Learning
* Feature Importance Analysis
* Explainable AI (SHAP)
* K-Means Inventory Segmentation
* Interactive Streamlit Dashboard

---

### Home Page 

<p align="center">
  <img src="images\home_page.png" width="900">
</p>


---

## 🎯 Problem Statement

Medical stores often face challenges in balancing inventory levels with customer demand.

### Business Challenges

* Overstocking increases inventory carrying costs.
* Understocking results in missed sales opportunities.
* Demand patterns are difficult to estimate manually.
* Inventory behavior varies across products and suppliers.

### Project Objectives

* Predict total sales (`SaleTot`)
* Identify key drivers of sales performance
* Segment products based on inventory characteristics
* Support inventory optimization and forecasting

---

## 📊 Dataset Information

The dataset consists of real-world medical inventory records collected from operational inventory management systems.

### Note

Due to confidentiality requirements, the original dataset cannot be publicly shared.

The repository contains the complete analysis workflow, machine learning models, visualizations, and deployment code without exposing sensitive business information.

---

## ⚙️ Technology Stack

### Programming & Analysis

* Python
* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn

### Machine Learning

* Scikit-Learn
* XGBoost

### Explainable AI

* SHAP

### Deployment

* Streamlit Community Cloud

### Version Control

* Git
* GitHub

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
Feature Importance Analysis
        ↓
SHAP Explainability
        ↓
K-Means Clustering
        ↓
Streamlit Deployment
```

---

## 📈 Exploratory Data Analysis

EDA was performed to understand inventory behavior and uncover business insights.

### Key Analyses

* Fast Moving Products
* High Turnover Companies
* Inventory Hoarding Analysis
* Purchase vs Sales Analysis
* Stock vs Sales Analysis
* Overstocked Product Identification

### Business Insights

* Fast-moving products were identified for replenishment planning.
* Overstocked inventory was detected for cost reduction opportunities.
* Supplier performance patterns were analyzed.
* Inventory utilization trends were discovered.

---

## 🤖 Machine Learning Models Evaluated

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

A total of **14 models** were evaluated and compared.

---

## 🏆 Final Model Performance

### Selected Model

**Gradient Boosting Regressor**

| Metric   | Value  |
| -------- | ------ |
| R² Score | 0.7978 |
| RMSE     | 9.692  |
| MAE      | 4.415  |

### Why Gradient Boosting?

* Highest R² Score
* Lowest RMSE
* Lowest MAE
* Strong Generalization Performance
* Consistent Prediction Accuracy

---

## Model Comparison Dashboard

<p align="center">
  <img src="images\model_comparison1.png" width="100%">
</p>

<p align="center">
  <img src="images\model_comparison2.png" width="100%">
</p>

<p align="center">
  <img src="images\model_comparison3.png" width="100%">
</p>

<p align="center">
  <img src="images\model_comparison4.png" width="100%">
</p>

---

## 📌 Feature Importance Analysis

Feature importance analysis was performed using the final tuned Gradient Boosting model.

### Top Predictive Features

1. OStk (Opening Stock)
2. PurTot (Purchase Total)
3. QohValue (Inventory Value)
4. Packing
5. Product Type Features

These variables contributed the majority of the predictive power used for sales forecasting.

---

## 🧠 Explainable AI (SHAP)

SHAP (SHapley Additive exPlanations) was used to interpret model behavior and increase prediction transparency.

### Implemented Visualizations

* SHAP Summary Plot
* SHAP Waterfall Plot

### Benefits

* Global feature importance understanding
* Individual prediction explanations
* Improved model interpretability
* Increased stakeholder trust

---

## Explainable AI (SHAP) Page


<p align="center">
  <img src="images\shap_page1.png" width="100%">
</p>


<p align="center">
  <img src="images\shap_page2.png" width="100%">
</p>


---

## 📦 Inventory Segmentation

K-Means Clustering was applied to segment products based on inventory characteristics.

### Cluster Profiles

#### Cluster 0 – Low-Demand Products

* Low sales volume
* Slow inventory turnover

#### Cluster 1 – Fast-Moving Products

* High sales volume
* Frequent stock movement

#### Cluster 2 – High-Value Products

* High inventory value
* Requires careful monitoring

#### Cluster 3 – Bulk & Moderate-Demand Products

* Moderate demand
* Larger inventory quantities

### Business Value

* Inventory Optimization
* Demand Forecasting
* Stock Planning
* Resource Allocation

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

The project was converted into an interactive multi-page Streamlit application.

### Dashboard Pages

* Home
* EDA Dashboard
* Sales Prediction
* Model Comparison
* Explainable AI
* Inventory Segmentation
* About

---

## 📂 Repository Structure

```text
Medical-Inventory-Sales-Prediction/

├── app.py
├── pages/
├── utils/
├── models/
├── images/
├── notebooks/
├── requirements.txt
└── README.md
```

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

## 📦 Pretrained Models

The repository includes pretrained model files:

```text
models/
├── medical_inventory_gb_model.pkl
└── model_columns.pkl
```

This allows users to run predictions immediately without retraining the model.

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

---

## ⭐ Project Highlights

* End-to-End Machine Learning Pipeline
* 14 Model Comparisons
* Hyperparameter Tuning
* Feature Importance Analysis
* SHAP Explainability
* K-Means Segmentation
* Business Insight Generation
* Interactive Streamlit Dashboard
* Streamlit Application Deployed
* Real-World Business Use Case
* Confidential Dataset Handling
* Portfolio-Ready Deployment

---

## 🔮 Future Enhancements

- Interactive Plotly Dashboards for advanced data visualization.
- Prediction History Tracking using SQLite or PostgreSQL.
- FastAPI backend for serving model predictions as REST APIs.
- Docker containerization for simplified deployment.
- Automated PDF report generation for inventory insights.
- Cloud deployment using AWS, GCP, or Azure.
- User authentication and role-based access control.
- Model monitoring for tracking prediction performance over time.