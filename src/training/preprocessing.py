import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def load_data():
    data_path = PROJECT_ROOT / "data" / "processed" / "sales_data.csv"

    df = pd.read_csv(
        data_path,
        low_memory=False
    )

    categorical_features = [
        "StateHoliday",
        "StoreType",
        "Assortment",
        "PromoInterval"
    ]

    for col in categorical_features:
        df[col] = df[col].fillna("Unknown").astype(str)

    return df


def prepare_data(df):

    columns_to_drop = [
        "Sales",
        "Date",
        "Customers",
        "SalesPerCustomer"
    ]

    X = df.drop(columns=columns_to_drop)
    y = df["Sales"]

    categorical_features = [
        "StateHoliday",
        "StoreType",
        "Assortment",
        "PromoInterval"
    ]

    numerical_features = [
        col for col in X.columns
        if col not in categorical_features
    ]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )

    numeric_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median"))
        ]
    )

    categorical_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", OneHotEncoder(handle_unknown="ignore"))
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numerical_features),
            ("cat", categorical_transformer, categorical_features)
        ]
    )

    return (
        X_train,
        X_test,
        y_train,
        y_test,
        preprocessor
    )