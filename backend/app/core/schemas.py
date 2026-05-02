from pydantic import BaseModel
from datetime import date
from typing import List

class UploadResponse(BaseModel):
    status_code: int
    message: str
    file: dict[str, str] | None = None

    @classmethod
    def response(cls, status, msg, file=None):
        return cls(status_code=status, message=msg, file=file)

    class Config:
        from_attributes = True


class CreateNotes(BaseModel):
    file_name: str
    file_content: str
    
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