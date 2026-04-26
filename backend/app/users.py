from fastapi import APIRouter

router = APIRouter()

@router.get("/file", tags=["file upload"])
async def read_file():
    return {
        "message": "This is a router path"
    }