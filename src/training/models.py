from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor


def train_linear_regression(preprocessor):

    model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("regressor", LinearRegression())
        ]
    )

    return model

def train_random_forest(preprocessor):

    model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            (
                "regressor",
                RandomForestRegressor(
                    n_estimators=100,
                    random_state=42,
                    n_jobs=-1
                )
            )
        ]
    )

    return model


def train_xgboost(preprocessor):

    model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            (
                "regressor",
                XGBRegressor(
                    n_estimators=300,
                    learning_rate=0.05,
                    max_depth=8,
                    subsample=0.8,
                    colsample_bytree=0.8,
                    random_state=42,
                    n_jobs=-1,
                    objective="reg:squarederror"
                )
            )
        ]
    )

    return model