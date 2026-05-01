from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.routes import upload_file, view_uploaded_file, view_all_notes
from app.core.cache import init_redis, close_redis
from app.core.database import engine
import app.core.models as database_models

database_models.Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    
    await init_redis()
    print("Started Redis Connection.")
    yield

    await close_redis()
    print("Closed Redis Connection")

app = FastAPI(lifespan=lifespan)

app.include_router(upload_file.router)
app.include_router(view_uploaded_file.router)
app.include_router(view_all_notes.router)

if __name__ == "__main__":
    app()
