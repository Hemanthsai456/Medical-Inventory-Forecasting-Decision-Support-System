"""
Feature Engineering Module for Medical Inventory Forecasting.

Extracts feature preparation, data leakage prevention, encoding, and train/test splitting logic.
"""

from typing import Tuple
import pandas as pd
from sklearn.model_selection import train_test_split


def prepare_ml_dataset(stock_df: pd.DataFrame) -> pd.DataFrame:
    """Prepare ML-ready dataset from product stock data.

    - Removes data leakage columns (TotQty, Qoh)
    - Removes high-cardinality identifier column (Name)
    - Applies one-hot encoding on categorical features
    - Converts boolean dummies to integer
    """
    ml_df = stock_df.copy()

    # Drop data leakage columns
    ml_df = ml_df.drop(columns=["TotQty", "Qoh"], errors="ignore")

    # Drop high-cardinality identifier column
    ml_final = ml_df.drop(columns=["Name"], errors="ignore")

    # One-hot encode categorical columns
    categorical_cols = [
        col for col in ["Company", "type"] if col in ml_final.columns
    ]
    ml_final = pd.get_dummies(ml_final, columns=categorical_cols, drop_first=True)

    # Remove company dummy columns to avoid excessive sparse features / overfitting
    ml_model = ml_final.loc[
        :, ~ml_final.columns.str.startswith("Company_")
    ].copy()

    # Convert boolean dummy columns to integers
    bool_cols = ml_model.select_dtypes(include="bool").columns
    ml_model[bool_cols] = ml_model[bool_cols].astype(int)

    return ml_model


def split_features_and_target(
    ml_model: pd.DataFrame, target_column: str = "SaleTot"
) -> Tuple[pd.DataFrame, pd.Series]:
    """Separate feature matrix X and target vector y."""
    X = ml_model.drop(columns=[target_column])
    y = ml_model[target_column]
    return X, y


def create_train_test_split(
    X: pd.DataFrame,
    y: pd.Series,
    test_size: float = 0.2,
    random_state: int = 5,
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Perform train-test split using specified test size and random state."""
    return train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
