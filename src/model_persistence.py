from pathlib import Path
from typing import Any, List, Optional, Union
import joblib
import pandas as pd

# Repository base directory
BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_MODEL_DIR = BASE_DIR / "models"


def _resolve_path(
    filepath: Optional[Union[str, Path]], default_filename: str
) -> Path:
    # Resolve a given filepath or relative string into a portable Path object
    if filepath is None:
        return DEFAULT_MODEL_DIR / default_filename
    path = Path(filepath)
    if not path.is_absolute():
        if path.exists():
            return path
        alt_path = BASE_DIR / path
        return alt_path
    return path


def save_model(
    model: Any, filepath: str = "models/medical_inventory_gb_model.pkl"
) -> None:
    # Save trained ML model artifact using joblib
    path = _resolve_path(filepath, "medical_inventory_gb_model.pkl")
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, path)


def load_model(
    filepath: str = "models/medical_inventory_gb_model.pkl",
) -> Any:
    # Load trained ML model artifact using joblib
    path = _resolve_path(filepath, "medical_inventory_gb_model.pkl")
    return joblib.load(path)


def save_model_columns(
    columns: List[str], filepath: str = "models/model_columns.pkl"
) -> None:
    # Save list of model feature column names
    path = _resolve_path(filepath, "model_columns.pkl")
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(columns, path)


def load_model_columns(
    filepath: str = "models/model_columns.pkl",
) -> List[str]:
    # Load list of model feature column names
    path = _resolve_path(filepath, "model_columns.pkl")
    return joblib.load(path)


def save_dashboard_data(
    df: pd.DataFrame, filepath: str = "models/dashboard_data.pkl"
) -> None:
    # Save reference dataset artifact for dashboard/app consumption
    path = _resolve_path(filepath, "dashboard_data.pkl")
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_pickle(path)


def load_dashboard_data(
    filepath: str = "models/dashboard_data.pkl",
) -> pd.DataFrame:
    # Load reference dataset artifact for dashboard/app consumption
    path = _resolve_path(filepath, "dashboard_data.pkl")
    return pd.read_pickle(path)
