"""Postgres engine creator."""
from typing import Dict, TYPE_CHECKING

import asyncpg

if TYPE_CHECKING:
    from asyncpg.pool import Pool
    from aiohttp.web import Application


def db_url(config: "Dict") -> "str":
    """Creates PG DSN."""
    return (
        "postgresql://"
        f"{config['POSTGRES_USER']}:{config['POSTGRES_PASSWORD']}"
        f"@{config['POSTGRES_URL']}:{config['POSTGRES_PORT']}/{config['POSTGRES_DB']}"
    )


async def init_pg_pool(app: "Application"):
    """Sets pg pool for application."""
    pool: "Pool" = await asyncpg.create_pool(db_url(app["config"]["database"]))
    app["pg_pool"] = pool
