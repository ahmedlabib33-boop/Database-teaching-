from pathlib import Path

import pandas as pd


DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def load_math_topics():
    return pd.read_excel(
        DATA_DIR / "learning_math_topics.xlsx"
    )


def load_math_content():
    return pd.read_excel(
        DATA_DIR / "learning_math_content.xlsx"
    )


def load_english_topics():
    return pd.read_excel(
        DATA_DIR / "learning_english_topics.xlsx"
    )


def load_english_content():
    return pd.read_excel(
        DATA_DIR / "learning_english_content.xlsx"
    )
