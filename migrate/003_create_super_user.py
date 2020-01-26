import os

import asyncpg

from api.utilities.config import config
from api.database.engine import db_url
from api.utilities.security import generate_password_hash


async def migrate():
    url = db_url(config["database"])
    conn = await asyncpg.connect(url)
    await conn.execute("""INSERT INTO roles(name) VALUES($1)""", 'superuser')
    await conn.execute("""
            INSERT INTO users(name, email, password, role_id, approved)
            VALUES($1, $2, $3, $4, $5)
        """,
        'root',
        'admin@matta.dev',
        generate_password_hash(os.environ['ADMIN_PASSWORD']),
        1,
        True
    )
    await conn.close()
