from typing import Final
from pathlib import Path

DATA_DIR: Final = Path(__file__).parents[3] / "data"
SAMPLE_DATA_PATH: Final = DATA_DIR / "sample_data.csv"
PROCESSED_DATA_PATH: Final = DATA_DIR / "processed_data.csv"
