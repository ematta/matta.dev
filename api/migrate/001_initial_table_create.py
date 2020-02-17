import asyncpg


async def migrate(conn):
    await conn.execute("DROP TABLE IF EXISTS roles CASCADE")
    await conn.execute("DROP TABLE IF EXISTS users CASCADE")
    await conn.execute(
        """
        CREATE TABLE IF NOT EXISTS roles(
            id       SERIAL,
            name     text,
            PRIMARY KEY (id)
        )
    """
    )
    await conn.execute(
        """
        CREATE TABLE IF NOT EXISTS users(
            id          SERIAL,
            name        text,
            email       text,
            password    text,
            role_id     integer,
            PRIMARY KEY (id),
            FOREIGN KEY (role_id) REFERENCES roles (id)
        )
    """
    )
