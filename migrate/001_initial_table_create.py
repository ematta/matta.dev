import asyncpg

from mattadev.utilities.config import load_config
from mattadev.utilities.database import db_url


async def migrate():
    config = load_config()
    url = db_url(config["database"])
    conn = await asyncpg.connect(url)
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
            username    text,
            password    text,
            role_id     integer,
            PRIMARY KEY (id),
            FOREIGN KEY (role_id) REFERENCES roles (id)
        )
    """
    )
    await conn.close()
