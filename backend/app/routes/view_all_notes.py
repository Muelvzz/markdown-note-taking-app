from fastapi import status, HTTPException, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
import json

from ..core.cache import set_cache, get_cache
from ..core.database import get_db
from ..core import schemas, models
from .router_init import router
from ..utils.data_to_dict import data_to_dict
from ..utils.read_notes import read_notes_from_folder

@router.get("/notes", status_code=status.HTTP_200_OK, response_model=schemas.AllNotesOut)
async def view_all_notes(db: Session = Depends(get_db)):

    try:
        all_notes = []

        all_notes_from_redis = await get_cache("all_notes")
        if all_notes_from_redis:
            all_notes = json.loads(all_notes_from_redis)
        
        else:
            all_notes_from_db = db.query(models.Notes).limit(10).all()
            all_notes_from_db_to_list = [data_to_dict(data) for data in all_notes_from_db]

            all_notes = await read_notes_from_folder(all_notes_from_db_to_list)

            encoded_all_notes = jsonable_encoder(all_notes)
            await set_cache("all_notes", json.dumps(encoded_all_notes))
        
        return schemas.AllNotesOut.success(all_notes)
    
    except Exception as e:

        print(f"Error occured: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occured while retrieving notes..."
        )