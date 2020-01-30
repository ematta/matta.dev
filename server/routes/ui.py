"""UI Routes."""
from typing import Dict, List, TYPE_CHECKING

from aiohttp.web import HTTPFound, get

from aiohttp_jinja2 import template

from server.middleware.post import get_all_posts, get_post

if TYPE_CHECKING:
    from aiohttp.web import Request, Response, RouteDef


@template("blog.jinja2")
async def handler_blog(request) -> "Dict":
    """Returns all posts."""
    posts = await get_all_posts(dbx=request.app["dropbox"])
    return {"posts": posts}


@template("blog.jinja2")
async def handler_specific_post(request: "Request") -> "Dict":
    """Returns a specific post."""
    post: "str" = await get_post(
        post=request.match_info["post"], dbx=request.app["dropbox"],
    )
    return {"post": post}


async def handle_personal_get(request: "Request") -> "Response":
    """Temp redirect to blogs."""
    location = request.app.router["blog"].url_for()
    return HTTPFound(location=location)


async def handle_resume_get(request: "Request") -> "Response":
    """Temp redirect to blogs."""
    location = request.app.router["blog"].url_for()
    return HTTPFound(location=location)
    return HTTPFound(location=location)


async def handle_projects_get(request: "Request") -> "Response":
    """Temp redirect to blogs."""
    location = request.app.router["blog"].url_for()
    return HTTPFound(location=location)


async def handle_index_get(request: "Request") -> "Response":
    """Temp redirect to blogs."""
    location = request.app.router["blog"].url_for()
    return HTTPFound(location=location)


routes: "List[RouteDef]" = [
    get("/about/me", handle_personal_get, name="personal"),
    get("/about/project", handle_projects_get, name="projects"),
    get("/about/resume", handle_resume_get, name="resume"),
    get("/", handle_index_get, name="index"),
    get("/blog", handler=handler_blog, name="blog"),
    get("/blog/{post}", handler=handler_specific_post, name="post"),
]
