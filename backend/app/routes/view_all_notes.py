from fastapi import status, HTTPException, Depends
from sqlalchemy.orm import Session
import json

from ..core.cache import set_cache, get_cache
from ..core.config import allowed_extensions
from ..core.database import get_db
from ..core import schemas, models
from .router_init import router

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