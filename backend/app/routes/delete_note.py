from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..core import schemas, models
from ..core.database import get_db
from ..utils.data_to_dict import data_to_dict
from ..core.cache import delete_cache
from ..routes.router_init import router
from ..utils.notes_folder_utils import delete_file_from_notes_folder

@router.delete("/file/{id}", status_code=status.HTTP_200_OK, response_model=schemas.UploadResponse)
async def delete_note(id: int, db: Session = Depends(get_db)):
  status_code = 0
  message = ""

  try:
    db_note = db.query(models.Notes).filter(models.Notes.id == id).first()

    if not db_note:
      status_code = status.HTTP_404_NOT_FOUND
      message = f"Id {id} is not found"

    else:
      db_note_dict = data_to_dict(db_note)

      await delete_cache("all_notes")
      delete_file_from_notes_folder(db_note_dict["file_path"])

      db.delete(db_note)
      db.commit()

      status_code = status.HTTP_200_OK
      message = f"Id {id} successfully deleted"

    return schemas.UploadResponse(status_code=status_code, message=message)

  except Exception as e:
    
    print(f"Error occured: {e}")
    raise HTTPException(
      status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
      detail="An error occured while retrieving note..."
    )