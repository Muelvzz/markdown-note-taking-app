from fastapi import APIRouter, File, UploadFile, status
from typing import Annotated

router = APIRouter()

@router.post("/file", status_code=status.HTTP_202_ACCEPTED)
async def upload_file(
    file: Annotated[bytes, File()],
    fileb: Annotated[UploadFile, File()],
    ):

    return {
        "message": "Upload successfully",
        "file": {
            "file_size": len(file),
            "fileb": fileb,
            "fileb_content_type": fileb.content_type
        }
    }