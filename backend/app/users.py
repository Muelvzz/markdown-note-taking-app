from fastapi import APIRouter, File, UploadFile, status, Depends
from typing import Annotated
from pathlib import Path
import json

from . cache import get_cache, set_cache
from . config import allowed_extensions

router = APIRouter()

@router.post("/file", status_code=status.HTTP_202_ACCEPTED)
async def upload_file(
    file: Annotated[UploadFile, File()],
    ):
    file_ext = Path(file.filename).suffix.lower()
    if file_ext not in allowed_extensions:
        return {
            "status_code": status.HTTP_406_NOT_ACCEPTABLE,
            "message": f"The file must be the following {allowed_extensions}"
        }

    filename = file.filename
    content = await file.read()

    file_content = {
        "filename": filename,
        "file_content": content.decode("utf-8"),
    }
    file_into_json = json.dumps(file_content)

    await set_cache("uploaded_file", file_into_json, 600)

    return { 
        "message": "Upload successfully",
        "file": {
            "filename": filename,
            "content": content
        }
    }

@router.get("/file", status_code=status.HTTP_200_OK)
async def view_file():
    value = await get_cache("uploaded_file")

    if value is None:
        return {
            "status_code": status.HTTP_404_NOT_FOUND,
            "message": "File does not exist"
        }

    decoded_redis_value = json.loads(value)
    return decoded_redis_value