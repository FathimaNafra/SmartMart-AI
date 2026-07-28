from pathlib import Path
import joblib


PROJECT_ROOT = Path(__file__).resolve().parents[2]

MODELS_DIR = PROJECT_ROOT / "models"
MODELS_DIR.mkdir(exist_ok=True)


def save_model(model, filename):

    model_path = MODELS_DIR / filename

    joblib.dump(model, model_path)

    print(f"✅ Model saved to {model_path}")