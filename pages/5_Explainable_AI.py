import streamlit as st
import pandas as pd

st.title("🧠 Explainable AI (SHAP)")

st.subheader("📌 Model Explanation Summary")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Top Driver",
        "OStk"
    )

with c2:
    st.metric(
        "Key Driver",
        "PurTot"
    )

with c3:
    st.metric(
        "Model",
        "GB Regressor"
    )

with c4:
    st.metric(
        "R² Score",
        "0.798"
    )


# ======================
# SHAP Summary Plot
# ======================

st.header("📊 Global Model Explanation")

st.image(
    "images/shap_summary.png",
    use_container_width=True
)

c1, c2, c3 = st.columns(3)

with c1:
    st.success(
        """
🔑 Top Driver

Opening Stock (OStk)
has the largest influence on
sales predictions.
"""
    )

with c2:
    st.info(
        """
📦 Inventory Impact

Inventory-related variables
contribute more than
product category features.
"""
    )

with c3:
    st.warning(
        """
📈 Business Insight

Sales forecasts are driven
primarily by inventory
behavior patterns.
"""
    )

st.subheader(
    "🏆 Most Influential Features"
)

ranking_df = pd.DataFrame(
    {
        "Rank":[1,2,3,4,5],
        "Feature":[
            "OStk",
            "PurTot",
            "QohValue",
            "Packing",
            "Product Type"
        ]
    }
)

st.table(ranking_df)

# ======================
# SHAP Waterfall Plot
# ======================

st.header("🌊 Individual Prediction Explanation")

st.image(
    "images/shap_waterfall.png",
    use_container_width=True
)

st.info(
"""
This waterfall plot explains how individual feature contributions combine to produce a single sales prediction.

Positive values increase the forecast while negative values reduce it.
"""
)

# ======================
# Business Interpretation
# ======================

st.subheader(
    "💼 Business Interpretation"
)

col1, col2 = st.columns(2)

with col1:

    st.success(
        """
Inventory Availability

Opening Stock is the strongest
signal used by the model,
indicating that inventory
levels are closely related
to future sales activity.
"""
    )

with col2:

    st.info(
        """
Procurement Behavior

Purchase Quantity contributes
significantly to forecasts,
suggesting procurement
decisions are aligned with
expected demand.
"""
    )

st.warning(
"""
Inventory managers can use these explanations to understand why a forecast was generated and identify the operational factors driving predicted demand.
"""
)