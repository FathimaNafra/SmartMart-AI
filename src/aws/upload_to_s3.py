import boto3
from src.config import PROCESSED_DATA_DIR

# Your S3 bucket name
BUCKET_NAME = "smartmart-ai-fathima-nafra"


def upload_processed_data() -> None:
    """
    Upload the processed dataset to AWS S3.
    """

    s3 = boto3.client("s3")

    file_path = PROCESSED_DATA_DIR / "sales_data.csv"

    s3.upload_file(
        str(file_path),
        BUCKET_NAME,
        "processed/sales_data.csv"
    )

    print("☁️ Dataset uploaded successfully to AWS S3!")
    print(f"Bucket : {BUCKET_NAME}")
    print("Folder : processed/")
    print("File   : sales_data.csv")