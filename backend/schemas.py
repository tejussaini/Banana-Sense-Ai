from pydantic import BaseModel


class UploadResponse(BaseModel):
    image_id: str
    filename: str | None
    size: int


class AnalysisResponse(BaseModel):
    image_id: str
    predicted_class: str
    confidence: float
    shelf_life_days: int
    advice: str
