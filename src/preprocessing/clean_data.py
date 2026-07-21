import pandas as pd


def clean_train_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the training dataset.
    """

    df = df.copy()

    # Convert Date column
    df["Date"] = pd.to_datetime(df["Date"])

    # Remove duplicates
    df = df.drop_duplicates()

    # Convert StateHoliday to string
    df["StateHoliday"] = df["StateHoliday"].astype(str)

    return df


def clean_store_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the store dataset.
    """

    df = df.copy()

    # Fill CompetitionDistance with median
    df["CompetitionDistance"] = df["CompetitionDistance"].fillna(
        df["CompetitionDistance"].median()
    )

    # Replace missing PromoInterval
    df["PromoInterval"] = df["PromoInterval"].fillna("None")

    return df


def clean_test_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the test dataset.
    """

    df = df.copy()

    # Convert Date
    df["Date"] = pd.to_datetime(df["Date"])

    # Fill missing Open values
    df["Open"] = df["Open"].fillna(1)

    return df