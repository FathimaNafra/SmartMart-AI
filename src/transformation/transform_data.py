import pandas as pd


def merge_datasets(
    train_df: pd.DataFrame,
    store_df: pd.DataFrame
) -> pd.DataFrame:
    """
    Merge training and store datasets.
    """

    merged_df = train_df.merge(
        store_df,
        on="Store",
        how="left"
    )

    return merged_df


def create_date_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create useful date-based features.
    """

    df = df.copy()

    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month
    df["Day"] = df["Date"].dt.day
    df["Week"] = df["Date"].dt.isocalendar().week.astype(int)
    df["Quarter"] = df["Date"].dt.quarter
    df["DayOfYear"] = df["Date"].dt.dayofyear
    df["IsWeekend"] = df["DayOfWeek"].isin([6, 7]).astype(int)

    return df


def create_business_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create business-related features.
    """

    df = df.copy()

    # Sales per customer
    df["SalesPerCustomer"] = (
        df["Sales"] / df["Customers"]
    ).fillna(0)

    return df


def transform_data(
    train_df: pd.DataFrame,
    store_df: pd.DataFrame
) -> pd.DataFrame:
    """
    Execute all transformation steps.
    """

    df = merge_datasets(train_df, store_df)

    df = create_date_features(df)

    df = create_business_features(df)

    return df