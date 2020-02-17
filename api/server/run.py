"""Main app entry."""
from typing import TYPE_CHECKING

from aiohttp.web import Application

import aiohttp_cors

import aiohttp_jinja2

from aiohttp_session import setup as setup_session
from aiohttp_session.redis_storage import RedisStorage

from dropbox import Dropbox

import jinja2

from server.database.postgres import init_pg_pool
from server.database.redis import close_redis, init_redis_pool
from server.routes.user import routes as user_routes
from server.routes.post import routes as post_routes
from server.utilities.config import SERVER_ROOT, config

if TYPE_CHECKING:
    from aiohttp_cors import CorsConfig


async def init_app() -> "Application":
    """Generates our Application."""
    app: "Application" = Application()
    app["config"] = config
    app["pg_pool"] = await init_pg_pool()
    app.add_routes(user_routes + post_routes)
    cors: "CorsConfig" = aiohttp_cors.setup(
        app,
        defaults={
            "*": aiohttp_cors.ResourceOptions(
                allow_credentials=True, expose_headers="*", allow_headers="*",
            ),
        },
    )
    for route in list(app.router.routes()):
        cors.add(route)
    return app
