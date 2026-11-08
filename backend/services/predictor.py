import sys
from pathlib import Path

from backend.config import PROJECT_DIR

if str(PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_DIR))

from src.predict import predict_ripeness


class PredictionError(RuntimeError):
    pass


def predict(image_path: Path) -> dict:
    try:
        return predict_ripeness(image_path)
    except Exception as error:
        raise PredictionError(str(error)) from error
