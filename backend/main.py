from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

from app.routes import upload_file, view_uploaded_file, view_all_notes, clear_cache, update_note
from app.core.cache import init_redis, close_redis
from app.core.database import engine
from app.core.config import origins, notes_folder
import app.core.models as database_models

database_models.Base.metadata.create_all(bind=engine)

print(f"Exist: {notes_folder.exists()}")
if not notes_folder.exists():
    notes_folder.mkdir(exist_ok=True)

@asynccontextmanager
async def lifespan(app: FastAPI):
    
    await init_redis()
    print("Started Redis Connection.")
    yield

    await close_redis()
    print("Closed Redis Connection")

app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_file.router)
app.include_router(view_uploaded_file.router)
app.include_router(view_all_notes.router)
app.include_router(clear_cache.router)
app.include_router(update_note.router)

if __name__ == "__main__":
    app()