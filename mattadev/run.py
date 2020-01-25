from aiohttp import web

import aiohttp_jinja2

from aiohttp_security import (
    SessionIdentityPolicy,
    authorized_userid,
    setup as setup_security,
)

from aiohttp_session import setup as setup_session
from aiohttp_session.redis_storage import RedisStorage

import jinja2

from mattadev.routes.user import routes as user_routes
from mattadev.routes.index import routes as index_routes
from mattadev.utilities.config import load_config
from mattadev.utilities.database import DBAuthorizationPolicy, init_db
from mattadev.utilities.logger import logger
from mattadev.utilities.redis import init_redis


async def current_user_ctx_processor(request):
    username = await authorized_userid(request)
    is_anonymous = not bool(username)
    return {"current_user": {"is_anonymous": is_anonymous}}


async def init_app():
    app = web.Application()
    app["config"] = load_config()
    logger.debug(f"Config: {app['config']}")
    db_pool = await init_db(app)
    redis_pool = await init_redis(app)
    setup_session(app, RedisStorage(redis_pool))
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.PackageLoader("mattadev"),
        context_processors=[current_user_ctx_processor],
    )
    setup_security(app, SessionIdentityPolicy(), DBAuthorizationPolicy(db_pool))
    app.add_routes(user_routes + index_routes)
    return app
