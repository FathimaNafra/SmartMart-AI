from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------
# Project Paths
# ---------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

RESULTS_DIR = PROJECT_ROOT / "results"

comparison_file = RESULTS_DIR / "model_comparison.csv"

# ---------------------------------------------------
# Load Comparison Results
# ---------------------------------------------------

df = pd.read_csv(comparison_file)

print(df)

# ---------------------------------------------------
# MAE Chart
# ---------------------------------------------------

plt.figure(figsize=(8,5))

plt.bar(df["Model"], df["MAE"])

plt.title("Model Comparison - MAE")
plt.ylabel("MAE")
plt.xlabel("Model")

plt.tight_layout()

plt.savefig(RESULTS_DIR / "mae_comparison.png")

plt.close()

# ---------------------------------------------------
# RMSE Chart
# ---------------------------------------------------

plt.figure(figsize=(8,5))

plt.bar(df["Model"], df["RMSE"])

plt.title("Model Comparison - RMSE")
plt.ylabel("RMSE")
plt.xlabel("Model")

plt.tight_layout()

plt.savefig(RESULTS_DIR / "rmse_comparison.png")

plt.close()

# ---------------------------------------------------
# R² Chart
# ---------------------------------------------------

plt.figure(figsize=(8,5))

plt.bar(df["Model"], df["R2"])

plt.title("Model Comparison - R² Score")
plt.ylabel("R²")
plt.xlabel("Model")

plt.tight_layout()

plt.savefig(RESULTS_DIR / "r2_comparison.png")

plt.close()

print("\n✅ Charts saved successfully!")