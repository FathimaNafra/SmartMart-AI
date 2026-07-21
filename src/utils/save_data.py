import pandas as pd
from src.config import PROCESSED_DATA_DIR


def save_processed_data(df: pd.DataFrame) -> None:
    """
    Save the processed dataset to the processed data folder.
    """

    # Create the processed directory if it doesn't exist
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

    # Output file path
    output_file = PROCESSED_DATA_DIR / "sales_data.csv"

    # Save the dataframe
    df.to_csv(output_file, index=False)

    print(f"\n💾 Processed dataset saved successfully!")
    print(f"📂 Location: {output_file}")