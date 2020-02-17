import os

import asyncpg

from server.utilities.security import generate_password_hash


async def migrate(conn):
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
