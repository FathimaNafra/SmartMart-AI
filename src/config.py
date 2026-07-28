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

# AWS Configuration
S3_BUCKET_NAME = "smartmart-ai-fathima-nafra"

# S3 folders
S3_RAW_FOLDER = "raw"
S3_PROCESSED_FOLDER = "processed"
S3_LOGS_FOLDER = "logs"