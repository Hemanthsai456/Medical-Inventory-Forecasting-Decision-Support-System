"""
Error Analysis Module for Medical Inventory Forecasting.

Provides functions for evaluating prediction errors, analyzing top error instances,
and computing performance metrics across demand quantiles.
"""

from typing import Tuple, Dict, Any
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def calculate_prediction_errors(
    X_test: pd.DataFrame, y_test: pd.Series, y_pred: np.ndarray
) -> pd.DataFrame:
    """Construct DataFrame with features, Actual, Predicted, Error, and Absolute_Error."""
    error_df = X_test.copy()
    error_df["Actual"] = y_test
    error_df["Predicted"] = y_pred
    error_df["Error"] = error_df["Actual"] - error_df["Predicted"]
    error_df["Absolute_Error"] = np.abs(error_df["Error"])
    return error_df.sort_values("Absolute_Error", ascending=False)


def get_top_errors(error_df: pd.DataFrame, top_n: int = 20) -> pd.DataFrame:
    """Return top N prediction errors."""
    return error_df.head(top_n)


def analyze_demand_group_performance(
    y_test: pd.Series, y_pred: np.ndarray
) -> pd.DataFrame:
    """Calculate MAE, RMSE, and R2 broken down by demand groups (Low, Medium, High)."""
    q1 = np.percentile(y_test, 25)
    q3 = np.percentile(y_test, 75)

    low_mask = y_test <= q1
    mid_mask = (y_test > q1) & (y_test < q3)
    high_mask = y_test >= q3

    mae_low = (
        mean_absolute_error(y_test[low_mask], y_pred[low_mask])
        if low_mask.sum() > 0
        else 0.0
    )
    mae_mid = (
        mean_absolute_error(y_test[mid_mask], y_pred[mid_mask])
        if mid_mask.sum() > 0
        else 0.0
    )
    mae_high = (
        mean_absolute_error(y_test[high_mask], y_pred[high_mask])
        if high_mask.sum() > 0
        else 0.0
    )

    results = pd.DataFrame(
        {
            "Demand_Group": ["Low", "Medium", "High"],
            "Count": [low_mask.sum(), mid_mask.sum(), high_mask.sum()],
            "MAE": [mae_low, mae_mid, mae_high],
        }
    )
    return results


def plot_actual_vs_predicted(
    y_test: pd.Series,
    y_pred: np.ndarray,
    title: str = "Actual vs Predicted Sales",
) -> plt.Figure:
    """Scatter plot of actual vs predicted sales with ideal reference line."""
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(y_test, y_pred, alpha=0.6)
    ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--")
    ax.set_xlabel("Actual")
    ax.set_ylabel("Predicted")
    ax.set_title(title)
    plt.tight_layout()
    return fig


def plot_residual_histogram(
    errors: pd.Series, title: str = "Residual Distribution"
) -> plt.Figure:
    """Plot histogram / KDE of prediction residual errors."""
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(errors, bins=30, kde=True, ax=ax)
    ax.set_xlabel("Residual")
    ax.set_ylabel("Count")
    ax.set_title(title)
    plt.tight_layout()
    return fig


def plot_demand_group_mae(
    demand_perf: pd.DataFrame, title: str = "MAE by Demand Group"
) -> plt.Figure:
    """Bar chart of MAE per demand group."""
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(demand_perf["Demand_Group"], demand_perf["MAE"])
    ax.set_title(title)
    ax.set_xlabel("Demand Group")
    ax.set_ylabel("MAE")
    plt.tight_layout()
    return fig


def plot_top_errors(
    top20: pd.DataFrame, title: str = "Top 20 Prediction Errors"
) -> plt.Figure:
    """Bar chart of absolute error values for top prediction errors."""
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(range(len(top20)), top20["Absolute_Error"])
    ax.set_title(title)
    ax.set_xlabel("Observation")
    ax.set_ylabel("Absolute Error")
    plt.tight_layout()
    return fig
