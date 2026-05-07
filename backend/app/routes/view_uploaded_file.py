from fastapi import status, HTTPException
import json

from ..core.cache import get_cache
from ..core import schemas
from .router_init import router

@router.get("/file", status_code=status.HTTP_200_OK, response_model=schemas.UploadResponse)
async def view_uploaded_file():

    status_code = 0
    message = ""
    file_dict = None

    try:
        file = await get_cache("uploaded_file")

        if file is None:
            status_code = status.HTTP_404_NOT_FOUND
            message = "File does not exist"

        else:
            decoded_redis_file = json.loads(file)

            status_code = status.HTTP_200_OK
            message = "Fetch Successfully"
            file_dict = decoded_redis_file

        return schemas.UploadResponse(status_code=status_code, message=message, file=file_dict)
    
    except Exception as e:
        
        print(f"Error occured: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occured while retrieving note..."
        )