import pandas as pd
import streamlit as st
from src.model_persistence import (
    load_model as load_persisted_model,
    load_model_columns,
)


@st.cache_resource
def load_model():
    model = load_persisted_model("models/medical_inventory_gb_model.pkl")
    columns = load_model_columns("models/model_columns.pkl")
    return model, columns


model, model_columns = load_model()


def predict_sales(packing, ostk, purtot, qohvalue, product_type):
    # Base input
    input_data = {
        "Packing": packing,
        "OStk": ostk,
        "PurTot": purtot,
        "QohValue": qohvalue,
    }

    # Create all type dummy columns
    type_columns = [
        "type_dose",
        "type_gram",
        "type_kit",
        "type_lot",
        "type_ml",
        "type_sach",
        "type_tab",
        "type_unit",
        "type_vial",
        "type_x",
    ]

    for col in type_columns:
        input_data[col] = 0

    selected_type = f"type_{product_type}"

    if selected_type in input_data:
        input_data[selected_type] = 1

    # Convert to DataFrame
    df = pd.DataFrame([input_data])

    # Match training column order
    df = df.reindex(columns=model_columns, fill_value=0)

    prediction = model.predict(df)[0]

    return prediction