from src.training.preprocessing import (
    load_data,
    prepare_data
)

from src.training.models import (
    train_linear_regression,
    train_random_forest,
    train_xgboost
)

from src.evaluation.metrics import (
    evaluate_model
)

from src.training.save_model import save_model

import pandas as pd


print("=" * 60)
print("SMARTMART AI - MODEL TRAINING")
print("=" * 60)

# =====================================================
# Load and Prepare Data
# =====================================================

df = load_data()

X_train, X_test, y_train, y_test, preprocessor = prepare_data(df)

results = []

# =====================================================
# Linear Regression
# =====================================================

print("\n" + "=" * 60)
print("TRAINING LINEAR REGRESSION")
print("=" * 60)

lr_model = train_linear_regression(preprocessor)

lr_model.fit(X_train, y_train)

mae, rmse, r2 = evaluate_model(
    lr_model,
    X_test,
    y_test
)

results.append({
    "Model": "Linear Regression",
    "MAE": mae,
    "RMSE": rmse,
    "R2": r2
})

print("\n========== LINEAR REGRESSION RESULTS ==========")
print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.4f}")

# =====================================================
# Random Forest
# =====================================================

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

results.append({
    "Model": "Random Forest",
    "MAE": mae,
    "RMSE": rmse,
    "R2": r2
})

print("\n========== RANDOM FOREST RESULTS ==========")
print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.4f}")

# =====================================================
# XGBoost
# =====================================================

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

results.append({
    "Model": "XGBoost",
    "MAE": mae,
    "RMSE": rmse,
    "R2": r2
})

print("\n========== XGBOOST RESULTS ==========")
print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.4f}")

# =====================================================
# Model Comparison
# =====================================================

comparison_df = pd.DataFrame(results)

comparison_df = comparison_df.sort_values(
    by="R2",
    ascending=False
).reset_index(drop=True)

print("\n" + "=" * 60)
print("MODEL COMPARISON")
print("=" * 60)

print(comparison_df)

# =====================================================
# Save Results
# =====================================================

comparison_df.to_csv(
    "results/model_comparison.csv",
    index=False
)

print("\n✅ Model comparison saved to results/model_comparison.csv")

# =====================================================
# Save Best Model
# =====================================================

best_model_name = comparison_df.iloc[0]["Model"]

print(f"\n🏆 Best Model: {best_model_name}")

if best_model_name == "Linear Regression":
    save_model(lr_model, "best_model.pkl")

elif best_model_name == "Random Forest":
    save_model(rf_model, "best_model.pkl")

else:
    save_model(xgb_model, "best_model.pkl")

print("✅ Best model saved as models/best_model.pkl")