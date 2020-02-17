"""Redis engine (with pooling)."""
from typing import TYPE_CHECKING

from aioredis import create_redis_pool

from server.utilities.config import config

if TYPE_CHECKING:
    from aioredis import Pool
    from aiohttp.web import Application


async def init_redis_pool():
    """Creates redis pool and attaches to app."""
    pool: "Pool" = await create_redis_pool(
        (config["redis"]["REDIS_HOST"], config["redis"]["REDIS_PORT"]),
    )
    return pool


async def close_redis(app: "Application"):
    """Closes redis."""
    pool = app["redis_pool"]
    pool.close()
    await pool.wait_closed()
