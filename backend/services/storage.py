import re
import shutil
from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile

from backend.config import ALLOWED_SUFFIXES, UPLOAD_DIR

_IMAGE_ID_PATTERN = re.compile(r"[0-9a-f]{32}")


class InvalidImageError(ValueError):
    pass


class ImageNotFoundError(FileNotFoundError):
    pass


def save_upload(image: UploadFile) -> Path:
    suffix = Path(image.filename or "").suffix.lower()

    if suffix not in ALLOWED_SUFFIXES:
        raise InvalidImageError(f"Unsupported image type: {suffix or 'unknown'}")

    path = UPLOAD_DIR / f"{uuid4().hex}{suffix}"

    with path.open("wb") as target:
        shutil.copyfileobj(image.file, target)

    return path


def resolve_image(image_id: str) -> Path:
    if not _IMAGE_ID_PATTERN.fullmatch(image_id):
        raise InvalidImageError(f"Invalid image id: {image_id}")

    for candidate in UPLOAD_DIR.glob(f"{image_id}.*"):
        if candidate.is_file():
            return candidate

    raise ImageNotFoundError(f"No uploaded image with id {image_id}")
