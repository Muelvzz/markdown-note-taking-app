from fastapi import APIRouter, File, UploadFile, status, Depends, HTTPException
from typing import Annotated, List
from pathlib import Path
from sqlalchemy.orm import Session
import json

from . cache import get_cache, set_cache
from . config import allowed_extensions
from . database import get_db
from . import schemas, models

router = APIRouter()

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


@router.get("/notes", status_code=status.HTTP_200_OK, response_model=schemas.AllNotesOut)
async def view_all_notes(db: Session = Depends(get_db)):

    try:
        all_notes = []

        all_notes_from_redis = await get_cache("all_notes")
        if all_notes_from_redis:
            all_notes = json.loads(all_notes_from_redis)
        
        else:
            all_notes_from_db = db.query(models.Notes).all()
            all_notes = all_notes_from_db

            await set_cache("all_notes", json.dumps(all_notes), 600)
        
        return schemas.AllNotesOut.success(all_notes)
    
    except Exception as e:

        print(f"Error occured: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occured while retrieving notes..."
        )