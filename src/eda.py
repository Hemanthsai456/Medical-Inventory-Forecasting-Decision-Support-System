from typing import Optional, Tuple
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def get_top_demand_products(
    stock_df: pd.DataFrame, top_n: int = 10
) -> pd.DataFrame:
    # Return top N products by total sales
    return stock_df.sort_values(by="SaleTot", ascending=False).head(top_n)


def plot_top_demand_products(
    top_sales: pd.DataFrame, title: str = "Top 10 High-Demand Products"
) -> plt.Figure:
    # Plot bar chart of top high-demand products
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=top_sales["SaleTot"], y=top_sales["Name"], ax=ax)
    ax.set_title(title)
    ax.set_xlabel("Total Sales")
    ax.set_ylabel("Product")
    plt.tight_layout()
    return fig


def get_low_demand_products(
    stock_df: pd.DataFrame, max_sales: float = 1.0, top_n: int = 10
) -> Tuple[pd.DataFrame, int, float, pd.DataFrame]:
    # Identify low-demand/dead stock products (SaleTot <= max_sales)
    low_sales = stock_df[stock_df["SaleTot"] <= max_sales]
    total_products = len(stock_df)
    low_count = len(low_sales)
    low_percent = (low_count / total_products * 100) if total_products > 0 else 0.0
    top_low = low_sales.sort_values(by="QohValue", ascending=False).head(top_n)
    return low_sales, low_count, low_percent, top_low


def plot_low_demand_products(
    top_low: pd.DataFrame,
    title: str = "Top 10 Low-Demand Products by Inventory Value",
) -> plt.Figure:
    # Plot low demand products with highest inventory value
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=top_low["QohValue"], y=top_low["Name"], ax=ax)
    ax.set_title(title)
    ax.set_xlabel("Inventory Value (QohValue)")
    ax.set_ylabel("Product")
    plt.tight_layout()
    return fig


def get_overstocked_products(
    stock_df: pd.DataFrame, top_n: int = 10
) -> pd.DataFrame:
    # Identify overstocked products (High Stock > mean, Low Sales < mean)
    overstock = stock_df[
        (stock_df["Qoh"] > stock_df["Qoh"].mean())
        & (stock_df["SaleTot"] < stock_df["SaleTot"].mean())
    ]
    return overstock.sort_values(by="Qoh", ascending=False).head(top_n)


def plot_overstocked_products(
    overstock: pd.DataFrame,
    title: str = "Overstocked Products (High Stock, Low Sales)",
) -> plt.Figure:
    # Plot bar chart of overstocked products
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=overstock["Qoh"], y=overstock["Name"], ax=ax)
    ax.set_title(title)
    ax.set_xlabel("Stock (Qoh)")
    ax.set_ylabel("Product")
    plt.tight_layout()
    return fig


def get_fast_moving_products(
    stock_df: pd.DataFrame, top_n: int = 10
) -> pd.DataFrame:
    # Identify fast-moving products (Sales > median, Stock < median)
    fast_moving = stock_df[
        (stock_df["SaleTot"] > stock_df["SaleTot"].median())
        & (stock_df["Qoh"] < stock_df["Qoh"].median())
    ]
    return fast_moving.sort_values(by="SaleTot", ascending=False).head(top_n)


def plot_fast_moving_products(
    fast_moving: pd.DataFrame, title: str = "Fast-Moving Products"
) -> plt.Figure:
    # Plot bar chart of fast-moving products
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=fast_moving["SaleTot"], y=fast_moving["Name"], ax=ax)
    ax.set_title(title)
    ax.set_xlabel("Sales")
    ax.set_ylabel("Product")
    plt.tight_layout()
    return fig


def plot_sales_vs_stock(
    stock_df: pd.DataFrame, title: str = "Stock vs Sales"
) -> plt.Figure:
    # Plot scatter plot of stock vs sales
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=stock_df, x="Qoh", y="SaleTot", ax=ax)
    ax.set_title(title)
    ax.set_xlabel("Stock (Qoh)")
    ax.set_ylabel("Sales (SaleTot)")
    plt.tight_layout()
    return fig


def get_top_companies_by_sales(
    company_grouped: pd.DataFrame, top_n: int = 10
) -> pd.DataFrame:
    # Return top N companies by sales value
    return company_grouped.sort_values(by="Sale Value", ascending=False).head(top_n)


def plot_top_companies(
    top_companies: pd.DataFrame, title: str = "Top Companies by Sales"
) -> plt.Figure:
    # Plot top companies by sales value
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=top_companies["Sale Value"], y=top_companies["Company"], ax=ax)
    ax.set_title(title)
    ax.set_xlabel("Sales Value")
    ax.set_ylabel("Company")
    plt.tight_layout()
    return fig


def plot_purchase_vs_sales(
    company_grouped: pd.DataFrame, title: str = "Purchase vs Sales"
) -> plt.Figure:
    # Plot scatter plot of purchase vs sales at company level
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(
        data=company_grouped, x="Purchase Value", y="Sale Value", ax=ax
    )
    ax.set_title(title)
    ax.set_xlabel("Purchase Value")
    ax.set_ylabel("Sales Value")
    plt.tight_layout()
    return fig


def get_high_turnover_companies(
    company_grouped: pd.DataFrame, top_n: int = 10
) -> pd.DataFrame:
    # Identify companies with high sales and low closing stock
    fast_companies = company_grouped[
        (company_grouped["Sale Value"] > company_grouped["Sale Value"].median())
        & (
            company_grouped["Closing Value"]
            < company_grouped["Closing Value"].median()
        )
    ]
    return fast_companies.sort_values(by="Sale Value", ascending=False).head(top_n)


def get_inventory_hoarding_companies(
    company_grouped: pd.DataFrame, top_n: int = 10
) -> pd.DataFrame:
    # Identify companies with high closing stock and low sales
    hoarding = company_grouped[
        (
            company_grouped["Closing Value"]
            > company_grouped["Closing Value"].median()
        )
        & (company_grouped["Sale Value"] < company_grouped["Sale Value"].median())
    ]
    return hoarding.sort_values(by="Closing Value", ascending=False).head(top_n)