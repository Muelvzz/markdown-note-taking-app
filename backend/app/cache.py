from . import config
from redis.asyncio import Redis

def error_redis_init():
    raise RuntimeError("Redis not initialized. Call init_redis() first.")

async def init_redis():
    global redis

    redis = Redis(
        host=config.redis_host,
        port=config.redis_port,
        db=config.redis_db,
        password=config.redis_password,
        decode_responses=True,
    )

async def close_redis():
    global redis

    if redis:
        await redis.close()

async def get_cache(key: str):
    if not redis:
        error_redis_init()
    return await redis.get(key)

async def set_cache(key: str, value: str, ttl: int = 600):
    if not redis:
        error_redis_init()
    await redis.set(key, value, ex=ttl)

async def delete_cache(key: str):
    if not redis:
        error_redis_init()
    await redis.delete(key)