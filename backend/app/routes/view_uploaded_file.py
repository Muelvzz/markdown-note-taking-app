from fastapi import status, File, HTTPException
import json

from ..core.cache import get_cache
from .router_init import router

@router.get("/file", status_code=status.HTTP_200_OK)
async def view_uploaded_file():
    try:
        file = await get_cache("uploaded_file")

        if file is None:
            return {
                "status_code": status.HTTP_404_NOT_FOUND,
                "message": "File does not exist"
            }

        decoded_redis_file = json.loads(file)
        return decoded_redis_file
    
    except Exception as e:
        
        print(f"Error occured: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occured while retrieving note..."
        )