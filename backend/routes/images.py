from fastapi import APIRouter, File, HTTPException, UploadFile

from backend.schemas import UploadResponse
from backend.services.storage import InvalidImageError, save_upload

router = APIRouter(tags=["images"])


@router.post("/upload-image", response_model=UploadResponse)
def upload_image(image: UploadFile = File(...)):
    try:
        path = save_upload(image)
    except InvalidImageError as error:
        raise HTTPException(status_code=415, detail=str(error)) from error

    return UploadResponse(
        image_id=path.stem,
        filename=image.filename,
        size=path.stat().st_size,
    )
