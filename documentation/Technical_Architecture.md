# Technical Architecture

## Medical Inventory Sales Prediction & Inventory Segmentation

---

# 1. Project Overview

The Medical Inventory Sales Prediction & Segmentation System is an end-to-end machine learning application designed to forecast medical inventory sales and generate inventory intelligence through predictive analytics, explainable AI, and inventory segmentation.

The system combines data preprocessing, machine learning, explainability techniques, clustering algorithms, and interactive dashboards into a unified decision-support platform.

---

# 2. System Architecture

```text
Raw Medical Inventory Data
            │
            ▼
      Data Cleaning
            │
            ▼
   Feature Engineering
            │
            ▼
    Model Development
            │
            ▼
 Model Evaluation & Tuning
            │
            ▼
 Explainable AI (SHAP)
            │
            ▼
Inventory Segmentation
            │
            ▼
 Business Logic Layer
            │
            ▼
  Streamlit Application
            │
            ▼
 End User Interaction
```

---

# 3. Dataset Layer

The project uses proprietary medical inventory records containing inventory, procurement, and sales information.

### Target Variable

```text
SaleTot
```

Represents total sales quantity.

### Key Features

```text
Packing
OStk
PurTot
QohValue
```

### Product Type Features

```text
type_dose
type_gram
type_kit
type_lot
type_ml
type_sach
type_tab
type_unit
type_vial
type_x
```

Total Features Used:

```text
14 Features
```

---

# 4. Data Processing Pipeline

### Step 1

Data Loading

↓

### Step 2

Data Cleaning

↓

### Step 3

Missing Value Handling

↓

### Step 4

Feature Preparation

↓

### Step 5

Product Type Encoding

↓

### Step 6

Train-Test Split

↓

### Step 7

Model Training

---

# 5. Machine Learning Architecture

## Models Evaluated

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

* Stacking Linear Regression
* Stacking Ridge
* Stacking Lasso
* Stacking Random Forest
* Stacking Gradient Boosting
* Stacking XGBoost

Total Models Evaluated:

```text
14 Models
```

### Complete Benchmark Comparison

| Model | Model Family | R² Score | RMSE | MAE |
| :--- | :--- | :--- | :--- | :--- |
| **Gradient Boosting Regressor (Tuned)** | **Tree-Based (Final Model)** | **0.7978** | **9.692** | **4.415** |
| Voting [1, 4, 2] | Voting Ensemble | 0.7900 | 9.876 | 4.422 |
| Voting [1, 5, 3] | Voting Ensemble | 0.7895 | 9.889 | 4.435 |
| Voting [2, 5, 3] | Voting Ensemble | 0.7882 | 9.920 | 4.420 |
| Voting [1, 3, 2] | Voting Ensemble | 0.7882 | 9.921 | 4.429 |
| Voting [1, 1, 1] | Voting Ensemble | 0.7826 | 10.050 | 4.430 |
| Stacking Lasso | Stacking Ensemble | 0.7810 | 10.087 | 4.530 |
| Stacking Ridge | Stacking Ensemble | 0.7804 | 10.101 | 4.562 |
| Stacking LR | Stacking Ensemble | 0.7804 | 10.101 | 4.562 |
| XGBoost Regressor (Tuned) | Tree-Based | 0.7684 | 10.373 | 4.595 |
| Random Forest Regressor (Tuned) | Tree-Based | 0.7513 | 10.750 | 4.559 |
| Stacking RF | Stacking Ensemble | 0.7508 | 10.760 | 4.699 |
| Stacking GBR | Stacking Ensemble | 0.7184 | 11.438 | 4.717 |
| Stacking XGB | Stacking Ensemble | 0.6448 | 12.846 | 5.101 |

---

# 6. Final Production Model

## Selected Model

```text
Gradient Boosting Regressor
```

### Performance

| Metric   | Value  |
| -------- | ------ |
| R² Score | 0.7978 |
| RMSE     | 9.692  |
| MAE      | 4.415  |

### Selection Criteria

The model achieved:

* Highest R² Score
* Lowest RMSE
* Lowest MAE
* Best overall generalization performance

among all evaluated models.

---

# 7. Explainable AI Layer

The project incorporates SHAP (SHapley Additive Explanations) to improve model interpretability.

## Implemented Components

### Global Explainability

* SHAP Summary Plot

### Local Explainability

* SHAP Waterfall Plot

### Feature Ranking

Top Features:

1. OStk
2. PurTot
3. QohValue
4. Packing
5. Product Type Features

### Business Benefit

Allows users to understand:

* Why predictions were generated
* Which variables influence forecasts
* How inventory variables affect demand predictions

---

# 8. Inventory Segmentation Architecture

K-Means Clustering was implemented to identify inventory behavior patterns.

### Cluster Selection

```text
Elbow Method
```

Optimal Clusters:

```text
K = 4
```

### Cluster Validation

```text
Silhouette Score = 0.7028
```

### Cluster Profiles

#### Cluster 0

Low-Demand Products

#### Cluster 1

Fast-Moving Products

#### Cluster 2

High-Value Products

#### Cluster 3

Bulk & Moderate-Demand Products

### Business Benefit

Provides inventory categorization for operational planning and monitoring.

---

# 9. Business Logic Layer

The application contains a rule-based decision support engine.

### Demand Classification

Forecasts are categorized into:

```text
Low Demand
Medium Demand
High Demand
```

### Inventory Risk Assessment

The system evaluates:

```text
Stockout Risk
Balanced Inventory
Overstock Risk
```

### Recommendation Engine

Generates inventory actions based on:

* Predicted demand
* Inventory position
* Inventory risk

---

# 10. Prediction-History & Audit Layer

The application includes an automated prediction-history and audit logging architecture to ensure traceability, compliance, and model monitoring across procurement operations.

### Stored Information Schema

Every prediction event is recorded with 7 standardized attributes:

| Column | Type | Stored Information |
| :--- | :--- | :--- |
| **Prediction_ID** | String | Unique prediction identifier (`PRED-YYYYMMDD-XXXXXX`) |
| **Timestamp** | String | Date and time formatted timestamp (`YYYY-MM-DD HH:MM:SS`) |
| **Product_ID** | String | Product identifier or tracking code (if available) |
| **Input_Features** | JSON | Serialized dictionary of all input parameters |
| **Predicted_Demand** | Float | Model sales forecast output |
| **Demand_Category** | String | Predicted demand classification (`Low`, `Medium`, `High`) |
| **Model_Version** | String | Versioned identifier of the production model |

### Dual-Sync Persistence Architecture

```text
User Prediction Form
         │
         ▼
Model Inference (Gradient Boosting Regressor)
         │
         ▼
7-Attribute Standardized Record
         │
         ├──► Local File Persistence (models/prediction_history.csv)
         │
         └──► Cloud Synchronization Engine
                    │
                    ├──► Google Apps Script Webhook (POST JSON)
                    │
                    └──► Google Sheets API v4 (Service Account Token Auth)
```

### Reliability & Fault Tolerance

* **Non-Blocking Execution:** Network delays or Google Sheets authentication issues never interrupt the user experience or fail predictions.
* **Local Persistence Fallback:** All records are reliably written to local CSV storage (`models/prediction_history.csv`).
* **Interactive UI Inspection:** Recent predictions can be directly reviewed via an interactive expander on the Streamlit Prediction page.

---

# 11. Application Architecture

## Frontend

```text
Streamlit
```

Provides:

* Interactive dashboards
* Model explanations
* Inventory segmentation views
* Prediction interface with prediction history

---

## Backend

```text
Python
Scikit-Learn
XGBoost
SHAP
Pandas
NumPy
Requests
Google-Auth
```

Handles:

* Data processing
* Prediction generation
* Model execution
* Business logic
* Prediction history logging and Google Sheets sync

---

# 12. Application Modules

### Home

Project overview and business context.

### EDA Dashboard

Interactive inventory analytics and KPI monitoring.

### Prediction Engine

Sales forecasting, recommendation generation, and prediction history logging.

### Model Comparison

Performance benchmarking and model evaluation.

### Explainable AI

Prediction interpretation and feature analysis.

### Inventory Segmentation

Cluster analysis and inventory profiling.

### About

Project summary and technical overview.

---

# 13. Deployment Architecture

```text
GitHub Repository
        │
        ▼
Streamlit Cloud
        │
        ▼
End Users
```

### Deployment Components

* Trained Model Serialization
* Streamlit Application
* Git Version Control
* Cloud Deployment
* Google Sheets Cloud Sync

---

# 14. Technology Stack

## Programming

* Python

## Data Analysis

* Pandas
* NumPy

## Machine Learning

* Scikit-Learn
* XGBoost

## Explainable AI

* SHAP

## Visualization

* Matplotlib
* Seaborn
* Plotly

## Integration & Cloud Storage

* Google Sheets API
* Google Apps Script
* Requests
* Google-Auth

## Deployment

* Streamlit

## Version Control

* Git
* GitHub

---

# 15. Conclusion

The Medical Inventory Sales Prediction & Segmentation System demonstrates a complete machine learning lifecycle, integrating predictive modeling, explainability, inventory segmentation, business logic, and deployment into a unified inventory decision-support platform.

The architecture was designed to transform raw inventory records into actionable business insights while maintaining model transparency and operational relevance.
