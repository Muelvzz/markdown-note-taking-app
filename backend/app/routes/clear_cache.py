from fastapi import status, HTTPException

from . router_init import router
from .. core.cache import delete_cache, check_cache
from .. core import schemas

@router.delete("/clear/{field}", status_code=status.HTTP_200_OK, response_model=schemas.UploadResponse)
async def clear_cache(field: str):
    try:
        status_code = 0
        message = ""

        is_cache_exist = await check_cache(field)
        print(f"is_cache_exist: {is_cache_exist}")
        if is_cache_exist:
            await delete_cache(field)

            status_code = status.HTTP_200_OK
            message = f"{field} key is cleared from cache."

        else:
            status_code = status.HTTP_404_NOT_FOUND
            message = f"{field} key is not found from the cache"

        return schemas.UploadResponse.response(status=status_code, msg=message)
    
    except Exception as e:
        print(f"Error occured: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Theres an error in caching"
        )