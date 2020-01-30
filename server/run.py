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
from server.routes.api import routes as api_routes
from server.routes.ui import routes as ui_routes
from server.utilities.config import SERVER_ROOT, config

if TYPE_CHECKING:
    from aiohttp_cors import CorsConfig


async def init_app() -> "Application":
    """Generates our Application."""
    app: "Application" = Application()
    app["config"] = config
    app["pg_pool"] = await init_pg_pool()
    app["redis_pool"] = await init_redis_pool()
    app.on_cleanup.append(close_redis)
    app["dropbox"] = Dropbox(config["dropbox"]["ACCESS_TOKEN"])
    aiohttp_jinja2.setup(
        app, loader=jinja2.FileSystemLoader(f"{SERVER_ROOT}/templates"),
    )
    app.router.add_static("/static/", path=f"{SERVER_ROOT}/static", name="static")
    app["static_root_url"] = "server/"
    setup_session(app, RedisStorage(app["redis_pool"]))
    app.add_routes(api_routes + ui_routes)
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
