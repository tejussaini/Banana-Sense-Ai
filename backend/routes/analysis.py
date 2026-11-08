from fastapi import APIRouter, HTTPException

from backend.schemas import AnalysisResponse
from backend.services.predictor import PredictionError, predict
from backend.services.shelf_life import estimate
from backend.services.storage import (
    ImageNotFoundError,
    InvalidImageError,
    resolve_image,
)

router = APIRouter(tags=["analysis"])


@router.post("/analyze/{image_id}", response_model=AnalysisResponse)
def analyze_image(image_id: str):
    try:
        path = resolve_image(image_id)
    except InvalidImageError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error
    except ImageNotFoundError as error:
        raise HTTPException(status_code=404, detail=str(error)) from error

    try:
        prediction = predict(path)
    except PredictionError as error:
        raise HTTPException(status_code=422, detail="Could not process image") from error

    shelf_life = estimate(prediction["predicted_class"])

    return AnalysisResponse(
        image_id=image_id,
        predicted_class=prediction["predicted_class"],
        confidence=prediction["confidence"],
        shelf_life_days=shelf_life["shelf_life_days"],
        advice=shelf_life["advice"],
    )
