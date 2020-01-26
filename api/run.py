import base64

from aiohttp import web

from aiohttp_security import (
    SessionIdentityPolicy,
    authorized_userid,
    setup as setup_security,
)

from aiohttp_session import setup as setup_session
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from cryptography.fernet import Fernet

import aiohttp_cors

from api.routes.user import routes as user_routes
from api.routes.index import routes as index_routes
from api.utilities.config import config
from api.database.auth import DBAuthorizationPolicy
from api.database.engine import init_db_pool
from api.utilities.logger import logger


async def current_user_ctx_processor(request):
    username = await authorized_userid(request)
    is_anonymous = not bool(username)
    return {"current_user": {"is_anonymous": is_anonymous}}


async def init_app():
    app = web.Application()
    app["config"] = config
    db_pool = await init_db_pool(app)
    setup_session(
        app,
        EncryptedCookieStorage(
            base64.urlsafe_b64decode(app["config"]["secret_key"])
        )
    )
    setup_security(app, SessionIdentityPolicy(), DBAuthorizationPolicy(db_pool))
    app.add_routes(user_routes + index_routes)
    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
                allow_credentials=True,
                expose_headers="*",
                allow_headers="*",
            )
    })
    for route in list(app.router.routes()):
        cors.add(route)
    return app
