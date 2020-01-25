from aiohttp import web

from aiohttp_security import (
    SessionIdentityPolicy,
    setup as setup_security,
)

from aiohttp_session import setup as setup_session
from aiohttp_session.redis_storage import RedisStorage

from server.routes.user import routes as user_routes
from server.utilities.config import load_config
from server.utilities.database import DBAuthorizationPolicy, init_db
from server.utilities.logger import logger
from server.utilities.redis import init_redis


async def init_app():
    app = web.Application()
    app["config"] = load_config()
    logger.debug(f"Config: {app['config']}")
    db_pool = await init_db(app)
    redis_pool = await init_redis(app)
    setup_session(app, RedisStorage(redis_pool))

    setup_security(app, SessionIdentityPolicy(), DBAuthorizationPolicy(db_pool))

    app.add_routes(user_routes)

    return app
