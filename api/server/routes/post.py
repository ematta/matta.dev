"""UI Routes."""
from typing import Dict, List, TYPE_CHECKING

from aiohttp.web import json_response, get

from server.middleware.post import get_all_posts, get_post

if TYPE_CHECKING:
    from aiohttp.web import Request, Response, RouteDef


async def handler_blog(request) -> "Response":
    """Returns all posts."""
    posts = await get_all_posts()
    payload: "Dict" = {"posts": posts}
    return json_response(data=payload, status=200)


async def handler_specific_post(request: "Request") -> "Response":
    """Returns a specific post."""
    post: "str" = await get_post(
        post=request.match_info["post"],
    )
    payload: "Dict" =  {"post": post}
    return json_response(data=payload, status=200)


routes: "List[RouteDef]" = [
    get("/api/post", handler=handler_blog, name="blog"),
    get("/api/post/{post}", handler=handler_specific_post, name="post"),
]
