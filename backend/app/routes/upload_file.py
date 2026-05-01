from fastapi import status, UploadFile, File, HTTPException
from typing import Annotated
from pathlib import Path
import json

from ..core.cache import set_cache
from ..core.config import allowed_extensions
from .router_init import router

@router.post("/file", status_code=status.HTTP_202_ACCEPTED)
async def upload_file(
    file: Annotated[UploadFile, File()],
    ):

    try:
        file_extension = Path(file.filename).suffix.lower()
        if file_extension not in allowed_extensions:
            return {
                "status_code": status.HTTP_406_NOT_ACCEPTABLE,
                "message": f"The file must be the following {allowed_extensions}"
            }

        filename = file.filename
        file_content = await file.read()

        uploaded_file = {
            "filename": filename,
            "file_content": file_content.decode("utf-8"),
        }
        file_into_json = json.dumps(uploaded_file)

        await set_cache("uploaded_file", file_into_json, 600)

        return { 
            "message": "Upload successfully",
            "file": {
                "filename": filename,
                "content": file_content
            }
        }
    except Exception as e:
        
        print(f"Error occured: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occured while uploading notes..."
        )