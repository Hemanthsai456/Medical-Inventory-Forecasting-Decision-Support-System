import streamlit as st
import pandas as pd
from utils.prediction import predict_sales
from utils.history import save_prediction, get_prediction_history
from src.model_persistence import load_dashboard_data
from datetime import datetime
import uuid

@st.cache_data
def load_reference_data():
    return load_dashboard_data("models/dashboard_data.pkl")

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
    st.session_state.product_id = ""

if st.button("📋 Load Example Values"):
    st.session_state.packing = 10.0
    st.session_state.ostk = 500.0
    st.session_state.purtot = 2000.0
    st.session_state.qohvalue = 1500.0
    st.session_state.product_type = "tab"
    st.session_state.product_id = "MED-TAB-001"

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

    col_pt1, col_pt2 = st.columns(2)

    with col_pt1:
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

    with col_pt2:
        product_id = st.text_input(
            "Product ID (Optional)",
            value=st.session_state.product_id,
            placeholder="e.g. MED-TAB-001 (Optional)",
            help="Product identifier for tracking, if available."
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

        summary_cols = st.columns(6 if (product_id and product_id.strip()) else 5)

        summary_cols[0].metric("Packing", f"{packing:,.0f}")
        summary_cols[1].metric("Opening Stock", f"{ostk:,.0f}")
        summary_cols[2].metric("Purchased Quantity", f"{purtot:,.0f}")
        summary_cols[3].metric("Inventory Value", f"{qohvalue:,.0f}")
        summary_cols[4].metric("Product Type", product_type)
        if product_id and product_id.strip():
            summary_cols[5].metric("Product ID", product_id.strip())

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
            "Model: Gradient Boosting Regressor | R² = 0.7978 | RMSE = 9.692 | MAE = 4.415"
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

        st.markdown("### 🔄 Model-Assisted Inventory Planning Workflow")
        st.code("""
        Inventory Data
            ↓
        Sales Prediction
            ↓
        Demand Classification
            ↓
        Inventory Risk Assessment
            ↓
        Procurement Recommendation
            ↓
        Inventory Planning Decision
        """)

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
        st.info(
                "The matrix below illustrates common inventory risk scenarios based on forecasted demand and available stock levels."
            )
        st.markdown("### ⚠️ Inventory Risk Matrix")
        risk_df = pd.DataFrame({
            "Demand": [
                "High",
                "High",
                "Low",
                "Low"
            ],
            "Inventory": [
                "Low",
                "High",
                "Low",
                "High"
            ],
            "Risk": [
                "Stockout Risk",
                "Balanced",
                "Low Risk",
                "Overstock Risk"
            ]
        })

        st.dataframe(
            risk_df,
            use_container_width=True,
            hide_index=True
        )

        st.caption(
            "Prediction generated using the trained Gradient Boosting Regressor model."
        )

        st.markdown("### 🏥 Procurement Decision Simulation")
        if demand_level == "High":

            st.success("""
        Example Operational Decision

        Forecast: High Demand

        Procurement Team Action:
        Increase purchase quantity and maintain safety stock.

        Expected Result:
        Improved product availability and lower stockout probability.
        """)

        elif demand_level == "Medium":

            st.info("""
        Example Operational Decision

        Forecast: Medium Demand

        Procurement Team Action:
        Maintain standard purchasing cycle.

        Expected Result:
        Balanced inventory and stable turnover.
        """)

        else:

            st.warning("""
        Example Operational Decision

        Forecast: Low Demand

        Procurement Team Action:
        Reduce future purchases and review inventory exposure.

        Expected Result:
        Reduced excess inventory and lower carrying costs.
        """)


        # =========================================================
        # Save prediction record to Prediction-History System
        # =========================================================
        pred_id = f"PRED-{datetime.now().strftime('%Y%m%d')}-{uuid.uuid4().hex[:6].upper()}"
        prod_id_val = product_id.strip() if (product_id and product_id.strip()) else "N/A"

        input_data = {
            "Packing": packing,
            "OStk": ostk,
            "PurTot": purtot,
            "QohValue": qohvalue,
            "ProductType": product_type,
        }

        sheet_synced, sync_msg, saved_record = save_prediction(
            prediction_id=pred_id,
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            product_id=prod_id_val,
            input_features=input_data,
            predicted_demand=round(float(prediction), 2),
            demand_category=demand_level,
            model_version="Gradient Boosting Regressor v1.0",
        )
