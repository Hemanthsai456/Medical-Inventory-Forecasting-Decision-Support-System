import streamlit as st
import pandas as pd
from utils.prediction import predict_sales
from utils.history import save_prediction
from datetime import datetime

@st.cache_data
def load_reference_data():
    return pd.read_pickle(
        "models/dashboard_data.pkl"
    )

reference_df = load_reference_data()

LOW_THRESHOLD = reference_df["SaleTot"].quantile(0.25)
HIGH_THRESHOLD = reference_df["SaleTot"].quantile(0.75)

st.title("🔮 Sales Prediction")

st.info(
    """
    Predict expected medical inventory sales using the trained
    Gradient Boosting Regressor model.
    Enter inventory parameters below and click **Predict Sales**.
    """
)

with st.expander("ℹ️ What do these inputs mean?"):
    st.markdown("""
    **Packing** → Number of units contained in one package (e.g., 10 tablets per strip or 200 ml per bottle).

    **Opening Stock** → Inventory available before any new purchases are made.

    **Purchased Quantity** → Additional inventory purchased during the period.

    **Current Inventory Value** → Monetary value of inventory currently available in stock.

    **Product Type** → Unit/category used to measure the medical inventory item (ml, tablet, sachet, vial, etc.).
    """)

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

with st.container(border=True):

    col1, col2 = st.columns(2)

    with col1:

        packing = st.number_input(
            "Packing (Units per Package)",
            min_value=0.0,
            value=st.session_state.packing,
            placeholder="Enter Packing",
            help="Number of units contained in one package."
        )

        ostk = st.number_input(
            "Opening Stock (Starting Inventory)",
            min_value=0.0,
            value=st.session_state.ostk,
            placeholder="Enter Opening Stock",
            help="Inventory available before new purchases are made."
        )

    with col2:

        purtot = st.number_input(
            "Purchased Quantity",
            min_value=0.0,
            value=st.session_state.purtot,
            placeholder="Enter Purchased Quantity",
            help="Additional inventory purchased during the period."
        )

        qohvalue = st.number_input(
            "Current Inventory Value",
            min_value=0.0,
            value=st.session_state.qohvalue,
            placeholder="Enter Current Inventory Value",
            help="Monetary value of inventory currently available in stock."
        )

    product_type = st.selectbox(
        "Product Type",
        [
            "dose", "gram", "kit", "lot", "ml",
            "sach", "tab", "unit", "vial", "x"
        ],
        index=[
            "dose", "gram", "kit", "lot", "ml",
            "sach", "tab", "unit", "vial", "x"
        ].index(st.session_state.product_type),
        help="Select the product category."
    )

    predict_btn = st.button(
        "🔮 Predict Sales",
        use_container_width=True
    )

if predict_btn:

    if None in [packing, ostk, purtot, qohvalue]:
        st.warning("⚠️ Please fill all numeric fields.")

    else:

        st.markdown("### 📋 Input Summary")

        col1, col2, col3, col4, col5 = st.columns(5)

        col1.metric("Packing", f"{packing:,.0f}")
        col2.metric("Opening Stock", f"{ostk:,.0f}")
        col3.metric("Purchased Quantity", f"{purtot:,.0f}")
        col4.metric("Inventory Value", f"{qohvalue:,.0f}")
        col5.metric("Product Type", product_type)

        prediction = predict_sales(
            packing,
            ostk,
            purtot,
            qohvalue,
            product_type
        )

        if prediction >= HIGH_THRESHOLD:
            demand_level = "High"
        elif prediction >= LOW_THRESHOLD:
            demand_level = "Medium"
        else:
            demand_level = "Low"

        if prediction > 0:

            stock_ratio = ostk / prediction

            if stock_ratio < 0.5:
                inventory_risk = "Stockout Risk"
            elif stock_ratio > 2:
                inventory_risk = "Overstock Risk"
            else:
                inventory_risk = "Balanced"

        else:
            inventory_risk = "Unknown"

        if demand_level == "High":

            if inventory_risk == "Stockout Risk":
                recommendation = "Increase procurement immediately."
                strategy = "Maintain additional safety stock."
            else:
                recommendation = "Maintain current replenishment cycle."
                strategy = "Monitor sales closely."

        elif demand_level == "Medium":
            recommendation = "Maintain current inventory levels."
            strategy = "Review demand periodically."

        else:

            if inventory_risk == "Overstock Risk":
                recommendation = "Reduce future purchases."
                strategy = "Clear slow-moving inventory."
            else:
                recommendation = "Monitor inventory carefully."
                strategy = "Avoid excess procurement."

        st.markdown("---")

        st.markdown("## 📈 Prediction Result")

        st.markdown(
            f"""
            <div style="
                background-color:#1E4620;
                padding:20px;
                border-radius:10px;
                text-align:center;
                font-size:32px;
                font-weight:bold;
                color:white;
            ">
                 Predicted Units Sold: {round(prediction):,}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.caption(
            "Model: Gradient Boosting Regressor | R² = 0.798 | MAE = 4.415"
        )

        st.markdown("### 🎯 Business Recommendation")

        r1, r2, r3 = st.columns(3)

        with r1:
            st.metric("Demand Level", demand_level)

        with r2:
            if inventory_risk == "Stockout Risk":
                st.error("🔴 Stockout Risk")

            elif inventory_risk == "Overstock Risk":
                st.warning("🟠 Overstock Risk")

            else:
                st.success("🟢 Stock Balanced")
        with r3:
            st.metric("Product Type", product_type.upper())

        st.success(f"✅ Recommended Action:\n\n{recommendation}")
        st.info(f"📌 Suggested Strategy:\n\n{strategy}")

        st.markdown("### 💼 Expected Business Impact")

        if demand_level == "High":

            st.success(
                """
        Expected Outcome

        • Strong sales potential

        • Faster inventory movement

        • Higher replenishment frequency may be required
        """
            )

        elif demand_level == "Medium":

            st.info(
                """
        Expected Outcome

        • Stable inventory movement

        • Balanced purchasing requirements

        • Lower stockout probability
        """
            )

        else:

            st.warning(
                """
        Expected Outcome

        • Slow inventory movement

        • Potential carrying cost increase

        • Inventory review recommended
        """
            )

        total_inventory = ostk + purtot

        if total_inventory > 0:

            turnover_ratio = prediction / total_inventory

            st.markdown("### 📊 Inventory Turnover Insight")

            st.progress(min(turnover_ratio, 1.0))

            st.info(
                f"Predicted Inventory Turnover: {turnover_ratio:.1%}"
            )

            if turnover_ratio >= 0.60:
                st.success(
                    "📈 High expected inventory turnover. A large portion of available inventory is expected to be sold."
                )
            elif turnover_ratio >= 0.40:
                st.warning(
                    "📊 Moderate expected inventory turnover. Inventory movement appears balanced."
                )
            else:
                st.error(
                    "📉 Low expected inventory turnover. Monitor inventory levels to avoid overstocking."
                )

        st.caption(
            "Prediction generated using the trained Gradient Boosting Regressor model."
        )
    # Save prediction record to history
    save_prediction(
        {
            "Timestamp": datetime.now(),
            "Packing": packing,
            "OStk": ostk,
            "PurTot": purtot,
            "QohValue": qohvalue,
            "ProductType": product_type,
            "Prediction": round(prediction, 2),
            "DemandLevel": demand_level,
            "InventoryRisk": inventory_risk,
            "Recommendation": recommendation
        }
    )

