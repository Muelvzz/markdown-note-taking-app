from pydantic import BaseModel
from datetime import datetime
from typing import List


class BaseNote(BaseModel):
    id: int | None = None
    file_name: str
    file_path: str
    last_edited: datetime


class CreateNote(BaseNote):
    pass


class UploadNote(BaseModel):
    file_name: str
    file_content: str


class NoteOut(CreateNote):
    created_at: datetime
    file_content: str

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


class UploadResponse(BaseModel):
    status_code: int
    message: str
    file: NoteOut | None = None

    @classmethod
    def response(cls, status, msg, file=None):
        return cls(status_code=status, message=msg, file=file)

    class Config:
        from_attributes = True