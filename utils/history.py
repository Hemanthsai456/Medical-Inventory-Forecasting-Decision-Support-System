import pandas as pd
from pathlib import Path

HISTORY_FILE = "models/prediction_history.csv"

def save_prediction(record):

    df = pd.DataFrame([record])

    if Path(HISTORY_FILE).exists():

        df.to_csv(
            HISTORY_FILE,
            mode="a",
            header=False,
            index=False
        )

    else:

        df.to_csv(
            HISTORY_FILE,
            index=False
        )
