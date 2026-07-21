import pandas as pd


def check_empty(df: pd.DataFrame, dataset_name: str) -> None:
    """
    Check if the dataset is empty.
    """
    if df.empty:
        raise ValueError(f"{dataset_name} dataset is empty.")

    print(f"✅ {dataset_name}: Dataset is not empty.")


def check_required_columns(
    df: pd.DataFrame,
    required_columns: list[str],
    dataset_name: str
) -> None:
    """
    Check whether all required columns exist.
    """
    missing = [col for col in required_columns if col not in df.columns]

    if missing:
        raise ValueError(
            f"{dataset_name} is missing required columns: {missing}"
        )

    print(f"✅ {dataset_name}: Required columns exist.")


def check_duplicates(df: pd.DataFrame, dataset_name: str) -> None:
    """
    Check duplicate rows.
    """
    duplicates = df.duplicated().sum()

    print(f"📌 {dataset_name}: {duplicates} duplicate rows found.")


def check_missing_values(df: pd.DataFrame, dataset_name: str) -> None:
    """
    Display missing values.
    """
    print(f"\n📊 Missing Values ({dataset_name})")

    missing = df.isnull().sum()

    print(missing[missing > 0])

    print("-" * 40)


def validate_dataset(
    df: pd.DataFrame,
    dataset_name: str,
    required_columns: list[str]
) -> None:
    """
    Run all validation checks.
    """

    print(f"\n========== Validating {dataset_name} ==========")

    check_empty(df, dataset_name)

    check_required_columns(df, required_columns, dataset_name)

    check_duplicates(df, dataset_name)

    check_missing_values(df, dataset_name)

    print(f"✅ {dataset_name} validation completed.\n")