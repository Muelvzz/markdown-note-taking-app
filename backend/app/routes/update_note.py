from fastapi import Depends, status, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from .. core.database import get_db
from .. core import schemas, models
from .. core.cache import delete_cache
from .. utils.data_to_dict import data_to_dict
from .. utils.notes_folder_utils import update_existing_files
from . router_init import router

@router.patch("/file/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=schemas.UploadResponse)
async def update_file(update_note: schemas.UploadNote, id: int, db: Session = Depends(get_db)):
    try:
        note_to_be_updated = db.query(models.Notes).filter(models.Notes.id == id).first()
        user_note = update_note.model_dump(exclude_unset=True)

        if note_to_be_updated is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Note could not be found."
            )
        note_to_be_updated_dict = data_to_dict(note_to_be_updated)

        note_to_be_updated.file_name = user_note["file_name"]
        note_to_be_updated.last_edited = datetime.utcnow()

        db.add(note_to_be_updated)
        db.commit()
        db.refresh(note_to_be_updated)

        update_existing_files(note_to_be_updated_dict["file_path"], user_note["file_content"])
        await delete_cache("all_notes")

        return schemas.UploadResponse.response(status=status.HTTP_202_ACCEPTED, msg="Update note successfully.")

    except Exception as e:
        print(f"Error occured: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occured."
        )
    
""""
User sends a request
    Frontend gives the necessary data to the user
    User edits the response and sends a request once again

    Backend finds the id to the data
        if it doesn't find any, then the backend raises an error
    
    Backend updates the row of the id from the user's input
    Backend saves the updated data

    Backend updates the fil content of the id from the user's input
    Backend deletes the cache

    Backend sends a positive response
"""