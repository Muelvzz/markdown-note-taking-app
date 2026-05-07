from fastapi import Depends, status, HTTPException
from sqlalchemy.orm import Session

from .. core.database import get_db
from .. core import schemas, models
from .. core.cache import delete_cache
from . router_init import router

@router.put("/file/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=schemas.UploadResponse)
async def update_file(update_note: schemas.UploadNote, id: int, db: Session = Depends(get_db)):
    try:
        note_to_be_updated = db.query(models.Notes).filter(models.Notes.id == id).first()

        if note_to_be_updated is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Note could not be found."
            )
        
        user_note = update_note.model_dump(exclude_unset=True)
        
        for key, value in user_note.items():
            setattr(note_to_be_updated, key, value)

        await delete_cache("all_notes")

        db.add(note_to_be_updated)
        db.commit()
        db.refresh(note_to_be_updated)

        return schemas.UploadResponse.response(status=status.HTTP_202_ACCEPTED, msg="Update note successfully.")

    except Exception as e:
        print(f"Error occured: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occured."
        )