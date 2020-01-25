from aiohttp_security.abc import AbstractAuthorizationPolicy

import asyncpg


def db_url(config):
    return (
        "postgresql://"
        f"{config['POSTGRES_USER']}:{config['POSTGRES_PASSWORD']}"
        f"@{config['POSTGRES_URL']}:{config['POSTGRES_PORT']}/{config['POSTGRES_DB']}"
    )


async def init_db(app):
    pool = await asyncpg.create_pool(db_url(app["config"]["database"]))
    app["db_pool"] = pool
    return pool


async def get_user_by_email(conn, email):
    result = await conn.execute(
        """
        SELECT * FROM users
        WHERE email = $1
        """,
        email
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


class DBAuthorizationPolicy(AbstractAuthorizationPolicy):
    def __init__(self, db_pool):
        self.db_pool = db_pool

    async def authorized_userid(self, identity):
        async with self.db_pool.acquire() as conn:
            user = await get_user_by_email(conn, identity)
            if user:
                return identity

        return None

    async def permits(self, identity, permission, context=None):
        if identity is None:
            return False
        return True
