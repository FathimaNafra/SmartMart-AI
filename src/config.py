from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Data directories
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw" / "rossmann"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"

# Dataset paths
TRAIN_DATA = RAW_DATA_DIR / "train.csv"
STORE_DATA = RAW_DATA_DIR / "store.csv"
TEST_DATA = RAW_DATA_DIR / "test.csv"