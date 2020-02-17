"""Logic for posts."""
from os import path
from typing import Dict, List, TYPE_CHECKING

from server.database.models.posts import find_all_posts, find_post_by_id

if TYPE_CHECKING:
    from asyncpg import Pool, Record


async def get_all_posts(pool: "Pool") -> "List[Dict]":
    """Gets all posts from dropbox."""
    async with pool.acquire() as conn:
        posts = find_all_posts(conn)
    return sorted(posts, key=lambda post: post["title"], reverse=True)


async def get_post(pool: "Pool", post_id: "int") -> "str":
    """Returns markdown post"""
    async with pool.acquire() as conn:
        individual_post: "str" = find_post_by_id(conn, post_id)
    return individual_post
