import pandas as pd

from src.config import TRAIN_DATA, STORE_DATA, TEST_DATA


def load_csv(file_path) -> pd.DataFrame:
    """
    Load a CSV file.

    Args:
        file_path: Path to the CSV file.

    Returns:
        pd.DataFrame
    """
    return pd.read_csv(file_path, low_memory=False)


def load_train_data() -> pd.DataFrame:
    """Load the Rossmann training dataset."""
    return load_csv(TRAIN_DATA)


def load_store_data() -> pd.DataFrame:
    """Load the Rossmann store dataset."""
    return load_csv(STORE_DATA)


def load_test_data() -> pd.DataFrame:
    """Load the Rossmann test dataset."""
    return load_csv(TEST_DATA)