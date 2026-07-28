from pathlib import Path

import joblib
import pandas as pd
import matplotlib.pyplot as plt

print("=" * 60)
print("FEATURE IMPORTANCE")
print("=" * 60)

# =====================================================
# Project Paths
# =====================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

MODEL_PATH = PROJECT_ROOT / "models" / "best_model.pkl"
RESULTS_DIR = PROJECT_ROOT / "results"

# =====================================================
# Load Saved Pipeline
# =====================================================

pipeline = joblib.load(MODEL_PATH)

print("✅ Best Model Loaded")

# =====================================================
# Extract Pipeline Components
# =====================================================

preprocessor = pipeline.named_steps["preprocessor"]
rf_model = pipeline.named_steps["regressor"]

print("✅ Preprocessor Extracted")
print("✅ Random Forest Extracted")

# =====================================================
# Get Feature Names
# =====================================================

feature_names = preprocessor.get_feature_names_out()

print(f"✅ Total Features: {len(feature_names)}")

# =====================================================
# Feature Importance
# =====================================================

importance_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": rf_model.feature_importances_
})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
).reset_index(drop=True)

# =====================================================
# Print Top 20 Features
# =====================================================

print("\nTop 20 Most Important Features\n")
print(importance_df.head(20))

# =====================================================
# Save CSV
# =====================================================

importance_df.to_csv(
    RESULTS_DIR / "feature_importance.csv",
    index=False
)

print("\n✅ feature_importance.csv saved")

# =====================================================
# Plot Top 20 Features
# =====================================================

top20 = importance_df.head(20)

plt.figure(figsize=(12,8))

plt.barh(
    top20["Feature"],
    top20["Importance"]
)

plt.gca().invert_yaxis()

plt.title("Top 20 Feature Importance - Random Forest")

plt.xlabel("Importance Score")

plt.tight_layout()

plt.savefig(
    RESULTS_DIR / "feature_importance.png",
    dpi=300
)

plt.close()

print("✅ feature_importance.png saved")

print("\n" + "=" * 60)
print("FEATURE IMPORTANCE COMPLETED")
print("=" * 60)