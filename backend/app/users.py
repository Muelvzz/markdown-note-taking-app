from fastapi import APIRouter
from schemas import Upload

router = APIRouter()

@router.post("/file")
async def read_file():
    return {
        "message": "This is a router path"
    }