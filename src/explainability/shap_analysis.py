from pathlib import Path

import joblib
import pandas as pd
import shap
import matplotlib.pyplot as plt

from src.training.preprocessing import (
    load_data,
    prepare_data
)

print("=" * 60)
print("SHAP EXPLAINABILITY")
print("=" * 60)

# --------------------------------------------------
# Paths
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

MODEL_PATH = PROJECT_ROOT / "models" / "best_model.pkl"
RESULTS_DIR = PROJECT_ROOT / "results"

# --------------------------------------------------
# Load Model
# --------------------------------------------------

pipeline = joblib.load(MODEL_PATH)

print("✅ Best Model Loaded")

# --------------------------------------------------
# Extract Pipeline Components
# --------------------------------------------------

preprocessor = pipeline.named_steps["preprocessor"]
rf_model = pipeline.named_steps["regressor"]

print("✅ Pipeline Extracted")

# --------------------------------------------------
# Load Data
# --------------------------------------------------

df = load_data()

X_train, X_test, y_train, y_test, _ = prepare_data(df)

print("✅ Data Loaded")

# --------------------------------------------------
# Transform Data
# --------------------------------------------------

X_test_processed = preprocessor.transform(X_test)

feature_names = preprocessor.get_feature_names_out()

print("✅ Data Preprocessed")

# --------------------------------------------------
# SHAP Explainer
# --------------------------------------------------

explainer = shap.TreeExplainer(rf_model)

print("✅ SHAP Explainer Created")

# Use only first 200 samples for speed
X_sample = X_test_processed[:200]

shap_values = explainer.shap_values(X_sample)

print("✅ SHAP Values Calculated")

# --------------------------------------------------
# Summary Plot
# --------------------------------------------------

plt.figure(figsize=(10,6))

shap.summary_plot(
    shap_values,
    X_sample,
    feature_names=feature_names,
    show=False
)

plt.tight_layout()

plt.savefig(
    RESULTS_DIR / "shap_summary.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("✅ shap_summary.png saved")

# --------------------------------------------------
# Bar Plot
# --------------------------------------------------

plt.figure(figsize=(10,6))

shap.summary_plot(
    shap_values,
    X_sample,
    feature_names=feature_names,
    plot_type="bar",
    show=False
)

plt.tight_layout()

plt.savefig(
    RESULTS_DIR / "shap_bar.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("✅ shap_bar.png saved")

print("\n" + "=" * 60)
print("SHAP ANALYSIS COMPLETED")
print("=" * 60)