import asyncpg

from server.database.postgres import db_url


async def migrate():
    url = db_url()
    conn = await asyncpg.connect(url)
    await conn.execute("""
        ALTER TABLE users
        ADD COLUMN approved BOOLEAN DEFAULT false;
    """)
    await conn.close()
