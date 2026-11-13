# Business Impact Report

## Medical Inventory Sales Prediction & Inventory Segmentation

---

# 1. Executive Summary

The Medical Inventory Sales Prediction system was developed to support inventory planning and procurement decision-making through machine learning-based demand forecasting.

Rather than replacing human decision-making, the system acts as a decision-support tool that helps inventory managers identify demand patterns, inventory risks, and procurement priorities.

The objective is to improve inventory visibility, support forecasting activities, and reduce operational inefficiencies associated with overstocking and stock shortages.

---

# 2. Business Problem

Medical inventory management presents several operational challenges:

* Demand uncertainty
* Overstocking risk
* Stockout risk
* Manual forecasting limitations
* Excess inventory carrying costs
* Inefficient procurement decisions

Traditional inventory planning often relies on historical experience and manual estimation, making it difficult to consistently align inventory levels with future demand.

The project addresses these challenges through machine learning-driven demand forecasting and inventory intelligence.

---

# 3. Solution Overview

The solution combines:

### Demand Forecasting

Predicts expected sales demand using historical inventory and procurement data powered by the production **Gradient Boosting Regressor** model (achieving R² = 0.7978, RMSE = 9.692, MAE = 4.415).

### Demand Classification

Forecasts are categorized into:

* Low Demand
* Medium Demand
* High Demand

### Inventory Risk Assessment

Identifies:

* Stockout Risk
* Balanced Inventory
* Overstock Risk

### Recommendation Engine

Generates inventory planning recommendations based on forecasted demand and inventory conditions.

---

# 4. Business Workflow

## Traditional Process

Inventory Review

↓

Manual Forecasting

↓

Procurement Decision

↓

Inventory Adjustment

↓

Potential Overstock or Stockout

---

## Model-Assisted Process

Inventory Data

↓

Machine Learning Prediction

↓

Demand Classification

↓

Inventory Risk Assessment

↓

Procurement Recommendation

↓

Inventory Review

↓

Final Business Decision

---

# 5. Decision Support Framework

## High Demand Prediction

### Scenario

Forecast indicates strong future demand.

### Recommended Actions

* Increase procurement priority
* Monitor inventory levels closely
* Maintain safety stock
* Review replenishment frequency

### Expected Benefits

* Reduced stockout risk
* Improved product availability
* Better customer service levels

---

## Medium Demand Prediction

### Scenario

Forecast indicates stable demand.

### Recommended Actions

* Maintain existing procurement cycle
* Continue periodic inventory review
* Monitor demand changes

### Expected Benefits

* Balanced inventory levels
* Stable inventory turnover
* Efficient purchasing operations

---

## Low Demand Prediction

### Scenario

Forecast indicates reduced demand.

### Recommended Actions

* Reduce future purchasing volume
* Review inventory exposure
* Monitor slow-moving products

### Expected Benefits

* Lower inventory carrying costs
* Reduced excess stock
* Improved inventory efficiency

---

# 6. Inventory Risk Matrix

| Demand Level | Inventory Level | Risk Assessment |
| ------------ | --------------- | --------------- |
| High         | Low             | Stockout Risk   |
| High         | High            | Balanced        |
| Medium       | Medium          | Balanced        |
| Low          | High            | Overstock Risk  |
| Low          | Low             | Low Risk        |

This framework helps inventory managers quickly identify situations requiring operational attention.

---

# 7. Business Value Generated

### Demand Visibility

Provides forward-looking demand estimates instead of relying solely on historical observations.

### Inventory Optimization Support

Helps identify inventory situations that may require procurement adjustments.

### Procurement Planning

Supports purchasing decisions using data-driven forecasts.

### Risk Identification

Highlights potential inventory risks before they become operational problems.

### Decision Consistency

Provides a repeatable forecasting framework across products and inventory categories.

### Prediction Auditability & History Tracking

Provides an automated historical record of all predictions synchronized directly to Google Sheets:

* **Audit Trail:** Preserves an immutable log of forecasts, inputs, and procurement recommendations with unique Prediction IDs.
* **Forecast Accountability:** Allows hospital and inventory management to review past purchasing recommendations against actual consumption.
* **Model Governance:** Supports longitudinal tracking of input values and demand categories to detect demand shifts and distribution changes.

---

# 8. Integration with Inventory Segmentation

The project also incorporates K-Means inventory segmentation.

### Fast-Moving Products

* High replenishment priority
* Frequent monitoring

### High-Value Products

* Inventory exposure monitoring
* Financial risk management

### Low-Demand Products

* Overstock prevention
* Inventory rationalization

### Bulk & Moderate Demand Products

* Routine procurement planning
* Inventory balancing

Combining forecasting and segmentation provides additional operational context for inventory decisions.

---

# 9. Project Limitations

The project is intended as a decision-support system and should not be considered a fully automated procurement solution.

Business users should consider:

* Market conditions
* Supplier constraints
* Seasonal factors
* Exceptional demand events
* Operational policies

when making final inventory decisions.

---

# 10. Conclusion

The Medical Inventory Sales Prediction system, powered by the **Gradient Boosting Regressor**, demonstrates how machine learning can support inventory management by combining demand forecasting, inventory risk assessment, recommendation generation, and inventory segmentation.

The solution transforms historical inventory records into actionable operational insights that can assist inventory managers in planning, monitoring, and decision-making activities.

While not intended to replace business judgment, the system provides a structured and data-driven framework for improving inventory planning processes.
