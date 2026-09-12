from typing import Tuple
import pandas as pd
from sklearn.model_selection import train_test_split

def prepare_ml_dataset(stock_df: pd.DataFrame) -> pd.DataFrame:
    # Remove data leakage columns and high-cardinality identifiers
    ml_df = stock_df.copy()
    ml_df = ml_df.drop(columns=["TotQty", "Qoh"], errors="ignore")
    ml_final = ml_df.drop(columns=["Name"], errors="ignore")

    # Apply one-hot encoding to categorical features
    categorical_cols = [
        col for col in ["Company", "type"] if col in ml_final.columns
    ]
    ml_final = pd.get_dummies(
        ml_final, columns=categorical_cols, drop_first=True
    )

    # Remove company dummy columns to avoid high dimensionality and overfitting
    ml_model = ml_final.loc[
        :, ~ml_final.columns.str.startswith("Company_")
    ].copy()

    # Convert boolean dummy variables to integers
    bool_cols = ml_model.select_dtypes(include="bool").columns
    ml_model[bool_cols] = ml_model[bool_cols].astype(int)

    return ml_model


def split_features_and_target(
    ml_model: pd.DataFrame, target_column: str = "SaleTot"
) -> Tuple[pd.DataFrame, pd.Series]:
    # Separate feature matrix X and target vector y
    X = ml_model.drop(columns=[target_column])
    y = ml_model[target_column]
    return X, y


def create_train_test_split(
    X: pd.DataFrame,
    y: pd.Series,
    test_size: float = 0.2,
    random_state: int = 5,
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    # Split data into training and testing sets
    return train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )