from fastapi import status, HTTPException, Depends
from sqlalchemy.orm import Session

from ..core import schemas, models
from .router_init import router
from ..core.database import get_db
from ..utils.data_to_dict import data_to_dict
from ..utils.read_notes import read_specific_notes_from_folder

@router.get("/file/{id}", status_code=status.HTTP_200_OK, response_model=schemas.UploadResponse)
async def view_notes(id: int, db: Session = Depends(get_db)):

    status_code = 0
    message = ""
    file_dict = None

    try:
        note_from_db = db.query(models.Notes).filter(models.Notes.id == id).first()

        if not note_from_db:
            status_code = status.HTTP_404_NOT_FOUND
            message = "Note was not found"

        else:
            db_note_to_dict = data_to_dict(note_from_db)
            db_note_content = await read_specific_notes_from_folder(db_note_to_dict["file_path"])

            db_note_to_dict["file_content"] = db_note_content

            status_code = status.HTTP_200_OK
            message = "Fetch Successfully"
            file_dict = db_note_to_dict

        return schemas.UploadResponse(status_code=status_code, message=message, file=file_dict)
    
    except Exception as e:
        
        print(f"Error occured: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occured while retrieving note..."
        )