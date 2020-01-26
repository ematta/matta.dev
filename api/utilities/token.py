from functools import wraps
import jwt
from datetime import datetime, timedelta
from aiohttp import web
from api.database.users import find_user_by_email
from api.utilities.config import config


async def generate_token(email):
    return jwt.encode(
        {
            "sub": email,
            "iat": datetime.utcnow(),
            "exp": datetime.utcnow() + timedelta(minutes=30),
        },
        config["secret_key"],
    )


def token_required(f):
    """ Token checker decorator """

    @wraps(f)
    async def _verify(*args, **kwargs):
        """ Verifies the token """
        request = args[0]
        auth_headers = request.headers.get("Authorization", "").split()
        if len(auth_headers) != 2:
            resp = {
                "message": "Authentication header not set correctly (or token missing).",
                "authenticated": False,
            }
            return web.json_response(resp)
        try:
            token = auth_headers[1]
            data = jwt.decode(token, config["secret_key"])
            user = None
            async with request.app["db_pool"].acquire() as conn:
                user = await find_user_by_email(conn=conn, email=data["sub"])
                if not user:
                    resp = {"message": "Users not found.", "authenticated": False}
                    return web.json_response(resp)
            user_dict = dict(user)
            del user_dict["password"]
            return await f(user_dict, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            resp = {
                "message": "Expired token. Reauthentication required.",
                "authenticated": False,
            }
            return web.json_response(resp)
        except jwt.InvalidTokenError:
            resp = {
                "message": "Invalid token. Registeration and / or authentication required",
                "authenticated": False,
            }
            return web.json_response(resp)

    return _verify
