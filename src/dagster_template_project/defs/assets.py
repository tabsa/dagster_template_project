import pandas as pd
from dagster import asset
from src.dagster_template_project.config.config import (
    SAMPLE_DATA_PATH,
    PROCESSED_DATA_PATH,
)


@asset
def sample_asset() -> str:
    """Simple process returning a string."""
    return "Hello from Dagster!"


@asset
def processed_data() -> str:
    """Somple ETL process that reads CSV file and adds an extra column."""
    ## Read data from the CSV
    df = pd.read_csv(SAMPLE_DATA_PATH)

    ## Add an age_group column based on the value of age
    df["age_group"] = pd.cut(
        df["age"], bins=[0, 30, 40, 100], labels=["Young", "Middle", "Senior"]
    )

    ## Save processed data
    df.to_csv(PROCESSED_DATA_PATH, index=False)
    return "Data loaded successfully"
