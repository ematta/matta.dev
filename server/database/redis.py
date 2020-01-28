"""Redis engine (with pooling)."""
from typing import TYPE_CHECKING

from aioredis import create_redis_pool

if TYPE_CHECKING:
    from aioredis import Pool
    from aiohttp.web import Application


async def init_redis_pool(app: "Application"):
    """Creates redis pool and attaches to app."""
    pool: "Pool" = await create_redis_pool(
        (app["config"]["redis"]["REDIS_HOST"], app["config"]["redis"]["REDIS_PORT"]),
    )

    async def close_redis(app: "Application"):
        pool.close()
        await pool.wait_closed()

    app.on_cleanup.append(close_redis)
    app["redis_pool"] = pool
