# Error Analysis Report

## Medical Inventory Sales Prediction & Inventory Segmentation

---

# 1. Executive Summary

This report evaluates the prediction errors of the final Gradient Boosting Regressor used for medical inventory sales forecasting.

The objective of this analysis is to understand model behavior beyond overall performance metrics and identify areas where prediction accuracy varies across different demand levels.

### Final Model Performance

| Metric   | Value  |
| -------- | ------ |
| R² Score | 0.7978 |
| RMSE     | 9.692  |
| MAE      | 4.415  |

### Key Findings

* The model performs consistently on low and medium demand products.
* Prediction errors increase significantly for high-demand products.
* Most large prediction errors occur during extreme sales situations.
* Inventory-related variables remain the strongest drivers of model behavior.
* The model is reliable for operational forecasting but less accurate during demand spikes.

--- 

# 2. Overall Model Performance

The final production model selected for deployment was a Gradient Boosting Regressor.

The model was evaluated using a held-out test dataset and achieved strong predictive performance, explaining approximately 80% of the variance in sales demand.

### Actual vs Predicted Analysis

![Actual vs Predicted](..\documentation\error_analysis\actual_vs_predicted.png)

The Actual vs Predicted plot shows that most observations follow the ideal prediction line, indicating strong overall model performance.

However, a small number of observations deviate substantially from the ideal line, suggesting reduced accuracy for extreme demand situations.

---

# 3. Demand Group Error Analysis

To better understand model behavior, products were segmented into demand groups using demand quantiles.

### Demand Group Performance

| Demand Group  | Count            | MAE              | RMSE |
| ------------- | ---------------- | ---------------- | ---- |
| Low Demand    | Replace from CSV | Replace from CSV |      |
| Medium Demand | Replace from CSV | Replace from CSV |      |
| High Demand   | Replace from CSV | Replace from CSV |      |

### Demand Group Visualization

![Demand Group MAE](..\documentation\error_analysis\demand_group_mae.png)

### Findings

* Low-demand products achieved the lowest prediction error.
* Medium-demand products maintained stable model performance.
* High-demand products experienced substantially larger prediction errors.
* Extreme sales behavior remains the most challenging forecasting scenario.

This indicates that the model captures normal inventory behavior effectively but struggles when demand deviates significantly from historical patterns.

---

# 4. Top 20 Prediction Error Analysis

To identify failure patterns, the 20 observations with the largest absolute prediction errors were examined.

### Top Error Visualization

![Top 20 Errors](..\documentation\error_analysis\top20_errors_plot.png)

### Key Observations

#### Observation 1

Large errors are concentrated in extreme-demand products rather than normal inventory items.

#### Observation 2

Several error cases contain unusually high opening stock values, indicating greater variability in sales behavior.

#### Observation 3

The model tends to underpredict sudden demand spikes and occasionally overpredict low-demand products.

#### Observation 4

Most prediction failures are isolated edge cases rather than systematic forecasting issues.

### Conclusion

The model performs well across the majority of inventory records, while the largest errors occur primarily in rare and difficult-to-predict demand scenarios.

---

# 5. Residual Analysis

Residual analysis was performed to evaluate model bias and error distribution.

## Residual Distribution

![Residual Histogram](..\documentation\error_analysis\residual_histogram.png)

### Findings

* Most residuals are concentrated near zero.
* The distribution indicates generally stable prediction behavior.
* A small number of large residuals contribute to overall error.

---

## Residual Scatter Analysis

![Residual Scatter](..\documentation\error_analysis\residual_scatter.png)

### Findings

* Residuals are randomly distributed around zero for most observations.
* Error variance increases as predicted demand increases.
* High-demand products exhibit greater forecasting uncertainty.

This pattern is expected in inventory forecasting problems where extreme sales behavior is inherently difficult to predict.

---

# 6. Key Findings

### Strengths

* Strong overall predictive performance.
* Reliable forecasting for low and medium demand products.
* Good generalization across inventory categories.
* Inventory-related variables provide strong predictive power.

### Limitations

* Reduced accuracy during demand spikes.
* Higher error variance for high-demand products.
* Extreme inventory situations remain difficult to model.

### Business Implications

The model can be used as a decision-support tool for inventory planning, procurement prioritization, and stock monitoring.

Forecasts should be supplemented with business review processes when dealing with unusually high-demand products or exceptional inventory events.

---

# 7. Future Improvements

Potential future enhancements include:

* Incorporating additional historical demand signals.
* Time-series based forecasting approaches.
* External demand drivers and seasonal indicators.
* Model monitoring and periodic retraining.
* Advanced anomaly detection for extreme inventory events.

---

# Conclusion

The Gradient Boosting Regressor demonstrates strong predictive performance for medical inventory sales forecasting and successfully captures the majority of demand behavior within the dataset.

Error analysis shows that prediction accuracy remains stable for normal inventory operations while performance decreases for rare high-demand scenarios. These findings indicate that the model is suitable for operational decision support and inventory planning while highlighting opportunities for future enhancement.
