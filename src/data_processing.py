"""
Data Processing Module for Medical Inventory Forecasting & Decision Support System.

Combines data cleaning, aggregation, and merging responsibilities.
"""

import numpy as np
import pandas as pd


def clean_product_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean product-level dataset including column standardization, type mapping,
    numeric conversions, and dropping missing values.
    """
    product_df = df.copy()

    # Clean column names
    product_df.columns = product_df.columns.str.strip()

    # Clean text columns
    for col in product_df.select_dtypes(include="object").columns:
        product_df[col] = product_df[col].astype(str).str.strip()

    # Rename typos in column names
    product_df = product_df.rename(columns={"Comapny": "Company"})

    # Convert numeric columns
    num_cols = ["Packing", "OStk", "PurTot", "TotQty", "SaleTot", "Qoh", "QohValue"]
    for col in num_cols:
        if col in product_df.columns:
            product_df[col] = pd.to_numeric(product_df[col], errors="coerce")

    # Standardize product type column
    if "type" in product_df.columns:
        product_df["type"] = (
            product_df["type"].astype(str).str.lower().str.strip()
        )

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

        # Filter out invalid type 'iu'
        product_df = product_df[product_df["type"] != "iu"]

    # Drop missing values (matches original notebook stock = stock.dropna())
    product_df = product_df.dropna()

    return product_df


def clean_company_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean company-level dataset handling column whitespace, typos, missing values,
    and zero-to-NaN conversions.
    """
    company_df = df.copy()

    # Clean column names
    company_df.columns = company_df.columns.str.strip()

    # Clean text columns
    for col in company_df.select_dtypes(include="object").columns:
        company_df[col] = company_df[col].astype(str).str.strip()

    # Rename typos in column names
    company_df = company_df.rename(columns={"Comapny": "Company"})

    # Replace 0 with NaN for activity validation
    company_df = company_df.replace(0, np.nan)

    # Remove rows with all NaN in key financial columns
    target_cols = [
        "Opening Value",
        "Sale Value",
        "Purchase Value",
        "Closing Value",
    ]
    company_df = company_df.dropna(subset=target_cols, how="all")

    # Fill remaining NaNs back with 0
    company_df = company_df.fillna(0)

    return company_df


def aggregate_product_by_company(stock_df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate product-level metrics by company."""
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

    # Rename aggregated columns
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
    """Merge company-level dataset with aggregated product-level data."""
    company_grouped = company_df.merge(df_grouped, on="Company", how="left")
    company_grouped = company_grouped.dropna()
    return company_grouped
