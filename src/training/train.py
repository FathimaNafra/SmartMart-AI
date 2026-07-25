from src.training.preprocessing import (
    load_data,
    prepare_data
)

from src.training.models import (
    train_linear_regression
)

from src.evaluation.metrics import (
    evaluate_model
)

from src.training.models import (
    train_linear_regression,
    train_random_forest
)

from src.training.models import (
    train_linear_regression,
    train_random_forest,
    train_xgboost
)

print("=" * 60)
print("SMARTMART AI - MODEL TRAINING")
print("=" * 60)

# Load dataset
df = load_data()

# Prepare data
X_train, X_test, y_train, y_test, preprocessor = prepare_data(df)

# Create model
model = train_linear_regression(preprocessor)

print("\nTraining Linear Regression...")

model.fit(X_train, y_train)

print("Training Complete!")

# Evaluate
mae, rmse, r2 = evaluate_model(
    model,
    X_test,
    y_test
)

print("\n========== RESULTS ==========")

print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.4f}")

print("\n" + "=" * 60)
print("TRAINING RANDOM FOREST")
print("=" * 60)

rf_model = train_random_forest(preprocessor)

rf_model.fit(X_train, y_train)

mae, rmse, r2 = evaluate_model(
    rf_model,
    X_test,
    y_test
)

print("\n========== RANDOM FOREST RESULTS ==========")
print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.4f}")

print("\n" + "=" * 60)
print("TRAINING XGBOOST")
print("=" * 60)

xgb_model = train_xgboost(preprocessor)

xgb_model.fit(X_train, y_train)

mae, rmse, r2 = evaluate_model(
    xgb_model,
    X_test,
    y_test
)

print("\n========== XGBOOST RESULTS ==========")
print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.4f}")