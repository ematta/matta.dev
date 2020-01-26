async def find_user_by_email(conn, email):
    result = await conn.execute(
        """
        SELECT * FROM users
        WHERE email = $1
        """,
        email,
    )
    return result


async def get_users(conn):
    result = await conn.execute(
        """
        SELECT * FROM users
        ORDER BY $1
        """
    )
    return result
