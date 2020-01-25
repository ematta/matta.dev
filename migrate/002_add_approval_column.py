import asyncpg

from mattadev.utilities.config import config
from mattadev.utilities.database import db_url


async def migrate():
    url = db_url(config["database"])
    conn = await asyncpg.connect(url)
    await conn.execute("""
        ALTER TABLE users
        ADD COLUMN approved BOOLEAN DEFAULT false;
    """)
    await conn.close()
