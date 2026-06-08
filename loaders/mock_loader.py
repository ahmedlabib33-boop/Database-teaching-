from pathlib import Path

import pandas as pd


DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def _load_mock_file(filename):
    return pd.read_excel(DATA_DIR / filename).fillna("")


def load_mock_math():
    return _load_mock_file("mock_math.xlsx")


def load_mock_english():
    return _load_mock_file("mock_english.xlsx")
