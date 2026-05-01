from pydantic import BaseModel
from datetime import date
from typing import List

class CreateNotes(BaseModel):
    file_name: str
    content: str
    
    class Config:
        from_attributes = True

class NoteOut(CreateNotes):
    created_at: date

    class Config:
        from_attributes = True

class AllNotesOut(BaseModel):
    status_code: int = 200
    message: str
    all_notes: List[NoteOut]

    @classmethod
    def success(self, notes: list, message="Query successful"):
        return self(message=message, all_notes=notes)

    class Config:
        from_attributes = True