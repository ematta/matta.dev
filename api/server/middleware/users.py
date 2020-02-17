"""API /users middleware."""
from typing import Dict, TYPE_CHECKING, Tuple

from server.database.models.users import find_user_by_email
from server.utilities.logger import logger
from server.utilities.security import check_password_hash
from server.utilities.token import generate_token

if TYPE_CHECKING:
    from asyncpg import Pool, Record


async def user_payload(data: "Dict", pool: "Pool") -> "Tuple[Dict, int]":
    """Builds our user payload and responds with it and a status code."""
    payload: "Dict" = {
        "success": None,
        "message": "",
        "token": "",
        "user": {},
    }
    status: "int" = 0
    if not data["email"] or not data["password"]:
        payload["success"] = False
        payload["message"] = "Missing email or password"
        status = 404
    async with pool.acquire() as conn:
        user: "Record" = await find_user_by_email(conn, data["email"])
        if user:
            user_data = dict(user)
            if not check_password_hash(data["password"], user_data["password"]):
                payload["success"] = False
                payload["message"] = "Password incorrect"
                status = 401
            else:
                del user_data[
                    "password"
                ]  # Clean out the hashed password before sending
                payload["success"] = True
                payload["message"] = "User authenticated"
                token = await generate_token(user_data["email"])
                payload["token"] = str(token)
                payload["user"] = user_data
                status = 201
        else:
            payload["success"] = False
            payload["message"] = "No user found"
    logger.debug(f"Status sent: {status}")
    logger.debug(f"Payload sent: {payload}")
    return (payload, status)
