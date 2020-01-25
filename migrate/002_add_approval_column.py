import asyncpg

from mattadev.utilities.config import load_config
from mattadev.utilities.database import db_url


async def migrate():
    config = load_config()
    url = db_url(config["database"])
    conn = await asyncpg.connect(url)
    await conn.execute("""
        ALTER TABLE users
        ADD COLUMN approved BOOLEAN DEFAULT false;
    """)
    await conn.close()
