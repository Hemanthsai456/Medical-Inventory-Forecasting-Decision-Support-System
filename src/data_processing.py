import numpy as np
import pandas as pd

def clean_product_data(df: pd.DataFrame) -> pd.DataFrame:
    product_df = df.copy()

    # Standardize column and text values
    product_df.columns = product_df.columns.str.strip()

    for col in product_df.select_dtypes(include="object").columns:
        product_df[col] = product_df[col].astype(str).str.strip()

    product_df = product_df.rename(columns={"Comapny": "Company"})

    # Convert numeric fields
    num_cols = ["Packing", "OStk", "PurTot", "TotQty", "SaleTot", "Qoh", "QohValue"]
    for col in num_cols:
        if col in product_df.columns:
            product_df[col] = pd.to_numeric(product_df[col], errors="coerce")

    if "type" in product_df.columns:
        product_df["type"] = (
            product_df["type"].astype(str).str.lower().str.strip()
        )

        # Normalize common type variations
        type_replacements = {
            "g": "gram",
            "gm": "gram",
            "gms": "gram",
            "gr": "gram",
            "grm": "gram",
            "vail": "vial",
            "t": "tab",
            "tub": "tab",
            "s": "sach",
            "m": "ml",
            "md": "ml",
        }
        product_df["type"] = product_df["type"].replace(type_replacements)

        # Remove invalid product types
        product_df = product_df[product_df["type"] != "iu"]

    product_df = product_df.dropna()

    return product_df


def clean_company_data(df: pd.DataFrame) -> pd.DataFrame:
    company_df = df.copy()

    # Standardize column and text values
    company_df.columns = company_df.columns.str.strip()

    for col in company_df.select_dtypes(include="object").columns:
        company_df[col] = company_df[col].astype(str).str.strip()

    company_df = company_df.rename(columns={"Comapny": "Company"})

    # Treat zero values as missing during activity validation
    company_df = company_df.replace(0, np.nan)

    target_cols = [
        "Opening Value",
        "Sale Value",
        "Purchase Value",
        "Closing Value",
    ]

    # Remove companies with no financial activity
    company_df = company_df.dropna(subset=target_cols, how="all")

    company_df = company_df.fillna(0)

    return company_df


def aggregate_product_by_company(stock_df: pd.DataFrame) -> pd.DataFrame:
    # Aggregate product metrics at company level
    agg_dict = {
        "OStk": "sum",
        "PurTot": "sum",
        "TotQty": "sum",
        "SaleTot": "sum",
        "Qoh": "sum",
        "QohValue": "sum",
    }

    present_aggs = {
        col: agg for col, agg in agg_dict.items() if col in stock_df.columns
    }

    df_grouped = stock_df.groupby("Company").agg(present_aggs).reset_index()

    rename_dict = {
        "OStk": "Grouped_OStk",
        "PurTot": "Grouped_PurTot",
        "TotQty": "Grouped_TotQty",
        "SaleTot": "Grouped_SaleTot",
        "Qoh": "Grouped_Qoh",
        "QohValue": "Grouped_QohValue",
    }

    df_grouped.rename(columns=rename_dict, inplace=True)

    return df_grouped


def merge_company_product_data(
    company_df: pd.DataFrame, df_grouped: pd.DataFrame
) -> pd.DataFrame:
    return company_df.merge(df_grouped, on="Company", how="left").dropna()