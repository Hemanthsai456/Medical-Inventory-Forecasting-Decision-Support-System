import streamlit as st
from utils.prediction import predict_sales

st.title("🔮 Sales Prediction")

st.info(
    """
    Predict expected medical inventory sales using the trained
    Gradient Boosting Regressor model.
    Enter inventory parameters below and click **Predict Sales**.
    """
)

# ======================
# Example Values Button
# ======================

if "packing" not in st.session_state:
    st.session_state.packing = None
    st.session_state.ostk = None
    st.session_state.purtot = None
    st.session_state.qohvalue = None
    st.session_state.product_type = "tab"

if st.button("📋 Load Example Values"):
    st.session_state.packing = 10.0
    st.session_state.ostk = 500.0
    st.session_state.purtot = 2000.0
    st.session_state.qohvalue = 1500.0
    st.session_state.product_type = "tab"

# ======================
# Prediction Form
# ======================

with st.container(border=True):

    col1, col2 = st.columns(2)

    with col1:
        packing = st.number_input(
            "Packing",
            min_value=0.0,
            value=st.session_state.packing,
            placeholder="Enter Packing",
            help="Packaging quantity of the product"
        )

        ostk = st.number_input(
            "Opening Stock (OStk)",
            min_value=0.0,
            value=st.session_state.ostk,
            placeholder="Enter Opening Stock",
            help="Inventory available at the beginning of the period"
        )

    with col2:
        purtot = st.number_input(
            "Purchase Total (PurTot)",
            min_value=0.0,
            value=st.session_state.purtot,
            placeholder="Enter Purchase Total",
            help="Total purchase value of inventory"
        )

        qohvalue = st.number_input(
            "Quantity on Hand Value (QohValue)",
            min_value=0.0,
            value=st.session_state.qohvalue,
            placeholder="Enter Quantity on Hand Value",
            help="Current inventory value available in stock"
        )

    product_type = st.selectbox(
        "Product Type",
        [
            "dose",
            "gram",
            "kit",
            "lot",
            "ml",
            "sach",
            "tab",
            "unit",
            "vial",
            "x"
        ],
        index=[
            "dose",
            "gram",
            "kit",
            "lot",
            "ml",
            "sach",
            "tab",
            "unit",
            "vial",
            "x"
        ].index(st.session_state.product_type),
        help="Select the product category"
    )

    predict_btn = st.button(
        "🔮 Predict Sales",
        use_container_width=True
    )

# ======================
# Prediction
# ======================

if predict_btn:

    if None in [packing, ostk, purtot, qohvalue]:
        st.warning("⚠️ Please fill all numeric fields.")
    else:

        # Input Summary
        st.markdown("### 📋 Input Summary")

        col1, col2, col3, col4, col5 = st.columns(5)

        col1.metric("Packing", f"{packing:,.0f}")
        col2.metric("Opening Stock", f"{ostk:,.0f}")
        col3.metric("Purchase Total", f"{purtot:,.0f}")
        col4.metric("QOH Value", f"{qohvalue:,.0f}")
        col5.metric("Product Type", product_type)

        prediction = predict_sales(
            packing,
            ostk,
            purtot,
            qohvalue,
            product_type
        )

        st.markdown("---")

        st.markdown("## 💰 Prediction Result")

        st.metric(
            label="Predicted Sales Value",
            value=f"{prediction:,.2f}"
        )

        # Business Interpretation

        if prediction > 5000:
            st.success(
                "📈 High expected sales volume. "
                "Ensure adequate inventory availability."
            )

        elif prediction > 1000:
            st.info(
                "📊 Moderate expected sales volume. "
                "Maintain balanced inventory levels."
            )

        else:
            st.warning(
                "📉 Low expected sales volume. "
                "Monitor stock levels to avoid overstocking."
            )

        st.caption(
            "Prediction generated using the trained Gradient Boosting Regressor model."
        )