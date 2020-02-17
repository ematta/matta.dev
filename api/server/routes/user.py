"""API Routes."""
from typing import Dict, List, TYPE_CHECKING, Tuple

from aiohttp.web import get, json_response, post

from server.middleware.users import user_payload
from server.utilities.token import token_required

if TYPE_CHECKING:
    from aiohttp.web import Response, Request, RouteDef


@token_required
async def handle_user_info(
    user: "Dict", token: "bytes", request: "Request",
) -> "Response":
    """Returns user info and token."""
    payload: "Dict" = {
        "success": True,
        "user": user,
        "message": "Retrieved user",
        "token": token,
    }
    return json_response(data=payload, status=200)


async def handle_user_login(request: "Request") -> "Response":
    """Logs in as user and responds with Response."""
    data: "Dict" = await request.json()
    payload: "Tuple[Dict, int]" = await user_payload(
        data, request.app["pg_pool"],
    )
    return json_response(data=payload[0], status=payload[1])


routes: "List[RouteDef]" = [
    post("/api/user/login", handle_user_login, name="user_login"),
    get("/api/user/info", handle_user_info, name="user_info"),
]
