"""
Modeling Module for Medical Inventory Forecasting.

Combines individual model training, ensemble models, hyperparameter tuning,
and model evaluation / comparison metrics.
"""

from typing import Dict, List, Tuple, Any, Optional
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor,
    VotingRegressor,
    StackingRegressor,
)
from xgboost import XGBRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def scale_features(
    X_train: pd.DataFrame, X_test: pd.DataFrame
) -> Tuple[np.ndarray, np.ndarray, StandardScaler]:
    """Fit StandardScaler on X_train and transform X_train and X_test."""
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, scaler


def train_linear_models(
    X_train_scaled: np.ndarray, y_train: pd.Series
) -> Dict[str, Any]:
    """Train Linear Regression, Ridge, and Lasso models on scaled features."""
    lr = LinearRegression()
    lr.fit(X_train_scaled, y_train)

    ridge = Ridge(alpha=1.0)
    ridge.fit(X_train_scaled, y_train)

    lasso = Lasso(alpha=0.1)
    lasso.fit(X_train_scaled, y_train)

    return {"Linear Regression": lr, "Ridge": ridge, "Lasso": lasso}


def train_base_tree_models(
    X_train: pd.DataFrame, y_train: pd.Series
) -> Dict[str, Any]:
    """Train baseline decision tree and ensemble models."""
    dt = DecisionTreeRegressor(random_state=5)
    dt.fit(X_train, y_train)

    rf = RandomForestRegressor(n_estimators=500, random_state=5)
    rf.fit(X_train, y_train)

    gbr = GradientBoostingRegressor(
        n_estimators=100, learning_rate=0.1, random_state=10
    )
    gbr.fit(X_train, y_train)

    xgb = XGBRegressor(
        n_estimators=100, learning_rate=0.05, max_depth=5, random_state=5
    )
    xgb.fit(X_train, y_train)

    return {
        "Decision Tree": dt,
        "Random Forest": rf,
        "Gradient Boosting": gbr,
        "XGBoost": xgb,
    }


def tune_random_forest(
    X_train: pd.DataFrame, y_train: pd.Series, cv: int = 5, n_jobs: int = -1
) -> GridSearchCV:
    """Perform hyperparameter tuning for Random Forest Regressor using GridSearchCV."""
    param_grid_rf = {
        "n_estimators": [100, 300],
        "max_depth": [3, 5, 10],
        "min_samples_split": [2, 5],
    }

    rf_grid = GridSearchCV(
        estimator=RandomForestRegressor(random_state=5),
        param_grid=param_grid_rf,
        cv=cv,
        scoring="r2",
        n_jobs=n_jobs,
    )
    rf_grid.fit(X_train, y_train)
    return rf_grid


def tune_gradient_boosting(
    X_train: pd.DataFrame, y_train: pd.Series, cv: int = 3, n_jobs: int = -1
) -> GridSearchCV:
    """Perform hyperparameter tuning for Gradient Boosting Regressor using GridSearchCV."""
    param_grid_gb = {
        "n_estimators": [100, 300],
        "learning_rate": [0.05, 0.1],
        "max_depth": [2, 3, 5],
        "subsample": [0.8, 1.0],
    }

    gb_grid = GridSearchCV(
        estimator=GradientBoostingRegressor(random_state=42),
        param_grid=param_grid_gb,
        cv=cv,
        scoring="r2",
        n_jobs=n_jobs,
    )
    gb_grid.fit(X_train, y_train)
    return gb_grid


def tune_xgboost(
    X_train: pd.DataFrame, y_train: pd.Series, cv: int = 5, n_jobs: int = -1
) -> GridSearchCV:
    """Perform hyperparameter tuning for XGBoost Regressor using GridSearchCV."""
    param_grid_xg = {
        "n_estimators": [100, 300],
        "max_depth": [3, 4],
        "learning_rate": [0.05, 0.1],
        "subsample": [0.8, 1.0],
        "colsample_bytree": [0.8, 1.0],
        "gamma": [0, 0.1],
        "reg_alpha": [0.5, 1],
        "reg_lambda": [1, 1.5],
    }

    xg_grid = GridSearchCV(
        estimator=XGBRegressor(random_state=42),
        param_grid=param_grid_xg,
        cv=cv,
        scoring="r2",
        n_jobs=n_jobs,
    )
    xg_grid.fit(X_train, y_train)
    return xg_grid


def train_voting_regressor(
    estimators: List[Tuple[str, Any]],
    weights: Optional[List[float]] = None,
    X_train: Optional[pd.DataFrame] = None,
    y_train: Optional[pd.Series] = None,
) -> VotingRegressor:
    """Train VotingRegressor ensemble with specified base estimators and weights."""
    voting = VotingRegressor(estimators=estimators, weights=weights)
    if X_train is not None and y_train is not None:
        voting.fit(X_train, y_train)
    return voting


def train_stacking_regressor(
    estimators: List[Tuple[str, Any]],
    final_estimator: Any,
    X_train: pd.DataFrame,
    y_train: pd.Series,
) -> StackingRegressor:
    """Train StackingRegressor ensemble with specified base estimators and meta-estimator."""
    stacking = StackingRegressor(
        estimators=estimators, final_estimator=final_estimator
    )
    stacking.fit(X_train, y_train)
    return stacking


def evaluate_model(
    y_true: pd.Series, y_pred: np.ndarray, model_name: str = "Model"
) -> Dict[str, Any]:
    """Calculate evaluation metrics (MAE, RMSE, R2) for predictions."""
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    return {"Model": model_name, "MAE": mae, "RMSE": rmse, "R2 Score": r2}


def compare_models(results_list: List[Dict[str, Any]]) -> pd.DataFrame:
    """Convert list of model evaluation dictionaries to DataFrame."""
    return pd.DataFrame(results_list)


def plot_subplots(
    y_test: pd.Series, y_pred: np.ndarray, model_name: str
) -> plt.Figure:
    """Plot Actual vs Predicted scatter and Residual scatter subplots."""
    residuals = y_test - y_pred

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    # 1. Actual vs Predicted
    axes[0].scatter(y_test, y_pred, alpha=0.6)
    min_val = min(y_test.min(), y_pred.min())
    max_val = max(y_test.max(), y_pred.max())
    axes[0].plot([min_val, max_val], [min_val, max_val], "r--", alpha=0.6)
    axes[0].set_xlabel("Actual SaleTot")
    axes[0].set_ylabel("Predicted SaleTot")
    axes[0].set_title(f"{model_name}\nActual vs Predicted")

    # 2. Residual Plot
    axes[1].scatter(y_pred, residuals, alpha=0.6)
    axes[1].axhline(0, color="red", linestyle="--")
    axes[1].set_xlabel("Predicted SaleTot")
    axes[1].set_ylabel("Residuals")
    axes[1].set_title(f"{model_name}\nResidual Plot")

    plt.tight_layout()
    return fig


def plot_model_comparison(
    results_df: pd.DataFrame, title: str = "Model Performance Comparison"
) -> plt.Figure:
    """Plot bar chart comparing model evaluation metrics."""
    fig, ax = plt.subplots(figsize=(8, 5))
    df_plot = results_df.set_index("Model")
    df_plot.plot(kind="bar", ax=ax)
    ax.set_title(title)
    ax.set_ylabel("Score")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    return fig
