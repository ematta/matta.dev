import base64

from aiohttp import web

from aiohttp_session import setup as setup_session
from aiohttp_session.cookie_storage import EncryptedCookieStorage

import aiohttp_cors

from api.routes.user import routes as user_routes
from api.routes.index import routes as index_routes
from api.utilities.config import config
from api.database.engine import init_db_pool


async def init_app():
    app = web.Application()
    app["config"] = config
    await init_db_pool(app)
    setup_session(
        app,
        EncryptedCookieStorage(base64.urlsafe_b64decode(app["config"]["secret_key"])),
    )
    app.add_routes(user_routes + index_routes)
    cors = aiohttp_cors.setup(
        app,
        defaults={
            "*": aiohttp_cors.ResourceOptions(
                allow_credentials=True, expose_headers="*", allow_headers="*",
            )
        },
    )
    for route in list(app.router.routes()):
        cors.add(route)
    return app
