from fastapi import FastAPI
from contextlib import asynccontextmanager

from app import users
from app.cache import init_redis, close_redis
from app.database import engine
import app.models as database_models

database_models.Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    
    await init_redis()
    print("Started Redis Connection.")
    yield

    await close_redis()
    print("Closed Redis Connection")

app = FastAPI(lifespan=lifespan)

app.include_router(users.router)

if __name__ == "__main__":
    app()
