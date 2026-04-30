from fastapi import Depends, FastAPI
from contextlib import asynccontextmanager
from typing import Any
from app import users
from redis.asyncio.client import Redis
import redis.asyncio as redis
import json, asyncio

from app.cache import init_redis, close_redis
from app.config import redis_host, redis_port

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
