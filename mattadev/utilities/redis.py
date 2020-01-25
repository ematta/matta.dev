import aioredis


async def init_redis(app):

    pool = await aioredis.create_redis_pool(
        (app["config"]["redis"]["REDIS_HOST"], app["config"]["redis"]["REDIS_PORT"])
    )

    async def close_redis(app):
        pool.close()
        await pool.wait_closed()

    app.on_cleanup.append(close_redis)
    app["redis_pool"] = pool
    return pool
