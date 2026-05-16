from fastapi import status, UploadFile, File, HTTPException, Depends
from typing import Annotated
from pathlib import Path
from sqlalchemy.orm import Session
from datetime import datetime

from ..core.cache import delete_cache
from ..core.config import allowed_extensions
from ..core import schemas, models
from .router_init import router
from ..core.database import get_db
from ..utils.notes_folder_utils import save_into_notes_folder

@router.post("/file", status_code=status.HTTP_202_ACCEPTED, response_model=schemas.UploadResponse)
async def upload_file(
    file: Annotated[UploadFile, File()],
    db: Session = Depends(get_db)
    ):

    status_code = 0
    message = ""
    file_dict = None

    try:
        file_extension = Path(file.filename).suffix.lower()
        if file_extension not in allowed_extensions:
            status_code = status.HTTP_406_NOT_ACCEPTABLE
            message = f"The file must be the following {allowed_extensions}"

        else:
            await delete_cache("all_notes")

            filename = file.filename
            file_content = await file.read()
            file_path = await save_into_notes_folder(file_content.decode("utf-8"))

            new_note = models.Notes(file_name=filename, file_path=file_path, last_edited=datetime.utcnow())
            db.add(new_note)
            db.commit()
            db.refresh(new_note)

            status_code = status.HTTP_200_OK
            message = "Upload successfully"

        return schemas.UploadResponse.response(status=status_code, msg=message, file=file_dict)
    
    except Exception as e:
        
        print(f"Error occured: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occured while uploading notes..."
        )