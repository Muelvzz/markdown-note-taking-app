from fastapi import APIRouter, File, UploadFile, status, Depends
from typing import Annotated
import json

from . cache import get_cache, set_cache

router = APIRouter()

@router.post("/file", status_code=status.HTTP_202_ACCEPTED)
async def upload_file(
    file: Annotated[UploadFile, File()],
    ):

    content = await file.read()

    file_content = {
        "filename": file.filename,
        "file_content": content.decode("utf-8"),
    }
    file_into_json = json.dumps(file_content)

    await set_cache("uploaded_file", file_into_json, 600)

    return { 
        "message": "Upload successfully",
        "file": {
            "filename": file.filename,
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