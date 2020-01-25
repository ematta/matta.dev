import os
import pathlib

from aiohttp import web


from aiohttp_security import (
    SessionIdentityPolicy,
    setup as setup_security,
)

from aiohttp_session import setup as setup_session
from aiohttp_session.redis_storage import RedisStorage

import aioredis

import pytoml

from server.routes.user import routes as user_routes
from server.utilities.database import DBAuthorizationPolicy, init_db
from server.utilities.logger import logger

AIOHTTP_ENV = os.environ["AIOHTTP_ENV"]


async def setup_redis(app):

    pool = await aioredis.create_redis_pool(
        (app["config"]["redis"]["REDIS_HOST"], app["config"]["redis"]["REDIS_PORT"])
    )

    async def close_redis(app):
        pool.close()
        await pool.wait_closed()

    app.on_cleanup.append(close_redis)
    app["redis_pool"] = pool
    return pool


def load_config():
    with open(f"{pathlib.Path(__file__).parent.parent}/{AIOHTTP_ENV}.toml") as f:
        return pytoml.load(f)


async def init_app():
    app = web.Application()
    app["config"] = load_config()
    logger.debug(f"Config: {app['config']}")
    db_pool = await init_db(app)
    redis_pool = await setup_redis(app)
    setup_session(app, RedisStorage(redis_pool))

    setup_security(app, SessionIdentityPolicy(), DBAuthorizationPolicy(db_pool))

    app.add_routes(user_routes)

    return app
