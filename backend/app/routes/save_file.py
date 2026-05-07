from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
import json

from .. core.cache import get_cache, delete_cache
from .. core import schemas
from .. core import models
from .. core.database import get_db
from . router_init import router


@router.get("/save", status_code=status.HTTP_202_ACCEPTED ,response_model=schemas.UploadResponse)
async def save_file_into_database(db: Session = Depends(get_db)):

    status_code = 0
    message = ""

    try:
        file = await get_cache("uploaded_file")

        if file is None:
            status_code = status.HTTP_400_BAD_REQUEST
            message = "No existing notes to be saved"

        else:
            decoded_file = json.loads(file)

            file_name = decoded_file["file_name"]
            file_content = decoded_file["content"]

            new_note = models.Notes(file_name=file_name, content=file_content)
            db.add(new_note)
            db.commit()
            db.refresh(new_note)

            await delete_cache("all_notes")

            status_code = status.HTTP_202_ACCEPTED
            message = "Note saved successfully"

        return schemas.UploadResponse.response(status=status_code, msg=message)
    
    except Exception as e:

        print(f"Error occured: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occured while retrieving the notes..."
        )