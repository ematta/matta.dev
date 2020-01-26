"""Users table."""
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from asyncpg import Connection, Record


async def find_user_by_email(conn: "Connection", email: "str") -> "Record":
    """Returns one record from email."""
    return await conn.fetchrow(
        """
        SELECT * FROM users
        WHERE email = $1
        """,
        email,
    )


async def get_users(conn: "Connection") -> "Any":
    """Returns all users."""
    return await conn.fetch(
        """
        SELECT * FROM users
        ORDER BY $1
        """,
    )
