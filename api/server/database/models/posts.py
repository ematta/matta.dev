"""Users table."""
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from asyncpg import Connection, Record


async def find_post_by_id(conn: "Connection", id: "int") -> "Record":
    """Returns one record from email."""
    return await conn.fetchrow(
        """
        SELECT * FROM posts
        WHERE id = $1
        """,
        id,
    )


async def find_all_posts(conn: "Connection") -> "Any":
    """Returns all users."""
    return await conn.fetch(
        """
        SELECT * FROM posts
        ORDER BY date
        """,
    )
