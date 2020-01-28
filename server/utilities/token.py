"""Checks token (decorator)."""
from datetime import datetime, timedelta
from functools import wraps
from typing import Callable, Dict, List, TYPE_CHECKING

from aiohttp import web

import jwt

from server.database.models.users import find_user_by_email
from server.utilities.config import config


if TYPE_CHECKING:
    from aiohtto.web import Response
    from asyncpg import Record


async def generate_token(email: "str") -> "bytes":
    """Creates a token based off of email address."""
    return jwt.encode(
        {
            "sub": email,
            "iat": datetime.utcnow(),
            "exp": datetime.utcnow() + timedelta(hours=2),
        },
        config["secret_key"],
    )


def token_required(f: "Callable") -> "Response":
    """Token checker decorator."""

    @wraps(f)
    async def _verify(*args, **kwargs):
        """Verifies the token."""
        request: "str" = args[0]
        auth_headers: "List" = request.headers.get("Authorization", "").split()
        if len(auth_headers) != 2:
            resp: Dict = {
                "message": "Authentication header not set correctly (or token missing).",
                "authenticated": False,
            }
            return web.json_response(resp)
        try:
            token: "str" = auth_headers[1]
            data: "str" = jwt.decode(token, config["secret_key"])
            async with request.app["pg_pool"].acquire() as conn:
                user: "Record" = await find_user_by_email(conn=conn, email=data["sub"])
                if not user:
                    resp: "Dict" = {
                        "message": "Users not found.",
                        "authenticated": False,
                    }
                    return web.json_response(resp)
            user_dict: "Dict" = dict(user)
            del user_dict["password"]
            return await f(user_dict, token.encode("utf-8"), *args, **kwargs)
        except jwt.ExpiredSignatureError:
            resp: "Dict" = {
                "message": "Expired token. Reauthentication required.",
                "authenticated": False,
            }
            return web.json_response(resp)
        except jwt.InvalidTokenError:
            resp: "Dict" = {
                "message": "Invalid token. Registeration and / or authentication required",
                "authenticated": False,
            }
            return web.json_response(resp)

    return _verify
