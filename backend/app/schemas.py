from fastapi import FastAPI
from pydantic import BaseModel

class Upload(BaseModel):
    file: str