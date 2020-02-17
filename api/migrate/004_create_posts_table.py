import asyncpg

async def migrate(conn):
    await conn.execute("DROP TABLE IF EXISTS posts CASCADE")
    await conn.execute(
        """
        CREATE TABLE IF NOT EXISTS posts(
            id       SERIAL,
            title    text,
            post     text,
            user_id  integer,
            PRIMARY KEY (id),
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """
    )
