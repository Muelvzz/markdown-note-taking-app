from fastapi import status, HTTPException

from . router_init import router
from .. core.cache import delete_cache

@router.delete("/clear/{field}", status_code=status.HTTP_200_OK)
async def clear_cache(field: str):
    try:
        await delete_cache(field)

        return {
            "status_code": status.HTTP_200_OK,
            "message": f"{field} key is cleared from cache."
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Could not find {field} key from the cache."
        )