from redis import asyncio as aioredis
from fastapi import FastAPI, Depends

def register_redis(app: FastAPI, config: dict):
    """
    注册Redis连接对象到App应用对象中
    :param app: App应用对象
    :param config: redis配置信息
    :return:
    """
    async def redis_pool():
        redis = await aioredis.from_url(
            f"redis://{config.get('username')}:{config.get('password')}@{config.get('host')}:{config.get('port')}/{config.get('db')}",
            decode_responses=True
        )
        return redis

    @app.on_event("startup")
    async def startup_event():
        app.state.redis = await redis_pool()

    @app.on_event("shutdown")
    async def shutdown_event():
        if hasattr(app.state, "redis"):
            await app.state.redis.close()

# 依赖函数，用于获取 Redis 连接
async def get_redis():
    """获取 Redis 连接."""
    from main import app
    if not hasattr(app.state, "redis"):
        raise RuntimeError("Redis not initialized")
    return app.state.redis