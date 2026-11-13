import json
import logging
import os
import re
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional, Tuple
import pandas as pd
import requests

logger = logging.getLogger(__name__)

HISTORY_FILE = "models/prediction_history.csv"
CONFIG_FILE = "utils/prediction_history.txt"

COLUMNS = [
    "Prediction_ID",
    "Timestamp",
    "Product_ID",
    "Input_Features",
    "Predicted_Demand",
    "Demand_Category",
    "Model_Version",
]


def get_sheet_target() -> Dict[str, Optional[str]]:
    """
    Parses configuration file and Streamlit secrets to locate target Google Sheet,
    Spreadsheet ID, and Google Apps Script Web App URL.
    """
    target = {
        "sheet_url": None,
        "spreadsheet_id": None,
        "apps_script_url": None,
    }

    # 1. Check utils/prediction_history.txt
    cfg_path = Path(CONFIG_FILE)
    if cfg_path.exists():
        try:
            content = cfg_path.read_text(encoding="utf-8").strip()
            for line in content.splitlines():
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "script.google.com/macros/s/" in line:
                    target["apps_script_url"] = line
                elif "docs.google.com/spreadsheets/d/" in line:
                    target["sheet_url"] = line
                    match = re.search(r"/spreadsheets/d/([a-zA-Z0-9-_]+)", line)
                    if match:
                        target["spreadsheet_id"] = match.group(1)
                elif not target["apps_script_url"] and (line.startswith("http://") or line.startswith("https://")):
                    target["apps_script_url"] = line
        except Exception as e:
            logger.warning("Could not read %s: %s", CONFIG_FILE, e)

    # 2. Check Streamlit secrets if available
    try:
        import streamlit as st

        if hasattr(st, "secrets") and st.secrets:
            secrets = st.secrets

            # Check common variable names
            for key in ["apps_script_url", "prediction_history_url", "google_sheet_url", "sheet_url", "PREDICTION_HISTORY_URL"]:
                if key in secrets and secrets[key]:
                    val = str(secrets[key]).strip()
                    if "script.google.com" in val:
                        target["apps_script_url"] = val
                    elif "docs.google.com/spreadsheets/d/" in val:
                        target["sheet_url"] = val
                        match = re.search(r"/spreadsheets/d/([a-zA-Z0-9-_]+)", val)
                        if match:
                            target["spreadsheet_id"] = match.group(1)
                    elif not target["apps_script_url"] and (val.startswith("http://") or val.startswith("https://")):
                        target["apps_script_url"] = val

            if "connections" in secrets and "gsheets" in secrets["connections"]:
                gsheets_conf = secrets["connections"]["gsheets"]
                if "spreadsheet" in gsheets_conf:
                    target["sheet_url"] = gsheets_conf["spreadsheet"]
                    match = re.search(r"/spreadsheets/d/([a-zA-Z0-9-_]+)", target["sheet_url"])
                    if match:
                        target["spreadsheet_id"] = match.group(1)
    except Exception:
        pass

    return target


def append_to_local_csv(record: Dict[str, Any]) -> bool:
    """Appends the prediction record to local CSV fallback history."""
    try:
        path = Path(HISTORY_FILE)
        path.parent.mkdir(parents=True, exist_ok=True)

        df_row = pd.DataFrame([record], columns=COLUMNS)

        if path.exists():
            df_row.to_csv(path, mode="a", header=False, index=False)
        else:
            df_row.to_csv(path, mode="w", header=True, index=False)
        return True
    except Exception as e:
        logger.error("Failed to append to local CSV %s: %s", HISTORY_FILE, e)
        return False


def append_to_google_sheet(record: Dict[str, Any]) -> Tuple[bool, str]:
    """
    Appends prediction record to Google Sheet using Apps Script Webhook
    or Google Sheets API (v4) via Service Account credentials.
    """
    target = get_sheet_target()
    apps_script_url = target.get("apps_script_url")
    spreadsheet_id = target.get("spreadsheet_id")

    # Method A: Google Apps Script Web App URL
    if apps_script_url:
        try:
            response = requests.post(
                apps_script_url,
                json=record,
                headers={"Content-Type": "application/json"},
                timeout=8,
            )
            if response.status_code in [200, 201, 302]:
                return True, "Synced to Google Sheet via Apps Script Web App."
            return False, f"Apps Script endpoint returned status {response.status_code}."
        except Exception as e:
            return False, f"Apps Script request failed: {e}"

    # Method B: Direct Google Sheets API with Service Account
    if spreadsheet_id:
        try:
            from google.oauth2 import service_account
            import google.auth.transport.requests

            service_account_info = None

            # Check Streamlit secrets
            try:
                import streamlit as st

                if hasattr(st, "secrets"):
                    if "gcp_service_account" in st.secrets:
                        service_account_info = dict(st.secrets["gcp_service_account"])
                    elif "google_service_account" in st.secrets:
                        service_account_info = dict(st.secrets["google_service_account"])
                    elif "connections" in st.secrets and "gsheets" in st.secrets["connections"]:
                        service_account_info = dict(st.secrets["connections"]["gsheets"])
            except Exception:
                pass

            # Check environment variable
            if not service_account_info and os.getenv("GOOGLE_APPLICATION_CREDENTIALS"):
                cred_file = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
                if Path(cred_file).exists():
                    with open(cred_file, "r", encoding="utf-8") as f:
                        service_account_info = json.load(f)

            if service_account_info:
                scopes = ["https://www.googleapis.com/auth/spreadsheets"]
                creds = service_account.Credentials.from_service_account_info(
                    service_account_info, scopes=scopes
                )
                request = google.auth.transport.requests.Request()
                creds.refresh(request)

                url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/A1:append?valueInputOption=USER_ENTERED&insertDataOption=INSERT_ROWS"
                headers = {
                    "Authorization": f"Bearer {creds.token}",
                    "Content-Type": "application/json",
                }
                body = {
                    "values": [[
                        record["Prediction_ID"],
                        record["Timestamp"],
                        record["Product_ID"],
                        record["Input_Features"],
                        record["Predicted_Demand"],
                        record["Demand_Category"],
                        record["Model_Version"],
                    ]]
                }
                resp = requests.post(url, headers=headers, json=body, timeout=8)
                if resp.status_code == 200:
                    return True, "Synced to Google Sheet via Sheets API."
                return False, f"Sheets API returned status {resp.status_code}."
            else:
                return False, "Google Sheet link recognized. Web App URL or Service Account required for remote write access."
        except Exception as e:
            return False, f"Google Sheets API error: {e}"

    return False, "No valid Google Sheet destination configured."


def save_prediction(
    record: Optional[Dict[str, Any]] = None,
    *,
    prediction_id: Optional[str] = None,
    timestamp: Optional[Any] = None,
    product_id: Optional[str] = None,
    input_features: Optional[Any] = None,
    predicted_demand: Optional[Any] = None,
    demand_category: Optional[str] = None,
    model_version: Optional[str] = None,
) -> Tuple[bool, str, Dict[str, Any]]:
    """
    Saves a prediction record to local CSV history and attempts synchronization
    to the configured Google Sheet.

    Columns stored:
    - Prediction_ID: Unique prediction identifier
    - Timestamp: Date and time formatted string
    - Product_ID: Product identifier, if available
    - Input_Features: JSON string of all input values
    - Predicted_Demand: Model prediction output
    - Demand_Category: Predicted demand classification
    - Model_Version: Machine learning model identifier
    """
    record = record or {}

    # 1. Prediction_ID
    p_id = (
        prediction_id
        or record.get("Prediction_ID")
        or f"PRED-{datetime.now().strftime('%Y%m%d')}-{uuid.uuid4().hex[:6].upper()}"
    )

    # 2. Timestamp
    raw_ts = timestamp or record.get("Timestamp")
    if isinstance(raw_ts, datetime):
        ts_str = raw_ts.strftime("%Y-%m-%d %H:%M:%S")
    elif isinstance(raw_ts, str) and raw_ts.strip():
        ts_str = raw_ts.strip()
    else:
        ts_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 3. Product_ID
    prod_id = product_id or record.get("Product_ID") or record.get("product_id")
    if not prod_id or not str(prod_id).strip():
        prod_id = "N/A"
    else:
        prod_id = str(prod_id).strip()

    # 4. Input_Features
    raw_inputs = input_features or record.get("Input_Features")
    if raw_inputs is None:
        raw_inputs = {
            k: record[k]
            for k in ["Packing", "OStk", "PurTot", "QohValue", "ProductType"]
            if k in record
        }
    if isinstance(raw_inputs, dict):
        inp_str = json.dumps(raw_inputs, ensure_ascii=False)
    else:
        inp_str = str(raw_inputs)

    # 5. Predicted_Demand
    p_demand = (
        predicted_demand
        if predicted_demand is not None
        else (record.get("Predicted_Demand") if "Predicted_Demand" in record else record.get("Prediction", 0.0))
    )
    try:
        p_demand = round(float(p_demand), 2)
    except Exception:
        pass

    # 6. Demand_Category
    d_category = (
        demand_category
        or record.get("Demand_Category")
        or record.get("DemandLevel")
        or "N/A"
    )

    # 7. Model_Version
    m_version = (
        model_version
        or record.get("Model_Version")
        or "Gradient Boosting Regressor v1.0"
    )

    standardized_record = {
        "Prediction_ID": p_id,
        "Timestamp": ts_str,
        "Product_ID": prod_id,
        "Input_Features": inp_str,
        "Predicted_Demand": p_demand,
        "Demand_Category": d_category,
        "Model_Version": m_version,
    }

    # Always save to local CSV
    append_to_local_csv(standardized_record)

    # Attempt sync to Google Sheet
    sheet_ok, sheet_msg = append_to_google_sheet(standardized_record)

    return sheet_ok, sheet_msg, standardized_record


def get_prediction_history(limit: Optional[int] = None) -> pd.DataFrame:
    """Loads prediction history from local CSV storage (newest first)."""
    path = Path(HISTORY_FILE)
    if path.exists():
        try:
            df = pd.read_csv(path)
            if limit and limit > 0:
                return df.tail(limit).iloc[::-1].reset_index(drop=True)
            return df.iloc[::-1].reset_index(drop=True)
        except Exception as e:
            logger.warning("Could not read prediction history CSV: %s", e)
            return pd.DataFrame(columns=COLUMNS)
    return pd.DataFrame(columns=COLUMNS)
