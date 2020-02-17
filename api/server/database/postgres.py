"""Postgres engine creator."""
import asyncpg

from server.utilities.config import config
from server.utilities.logger import logger


def db_url() -> "str":
    """Creates PG DSN."""
    db_config = config["database"]
    logger.debug(f"POSTGRES_USER: {db_config['POSTGRES_USER']}")
    logger.debug(f"POSTGRES_URL: {db_config['POSTGRES_URL']}")
    logger.debug(f"POSTGRES_PORT: {db_config['POSTGRES_PORT']}")
    logger.debug(f"POSTGRES_DB: {db_config['POSTGRES_DB']}")
    return (
        "postgresql://"
        f"{db_config['POSTGRES_USER']}:{db_config['POSTGRES_PASSWORD']}"
        f"@{db_config['POSTGRES_URL']}:{db_config['POSTGRES_PORT']}/{db_config['POSTGRES_DB']}"
    )


async def init_pg_pool():
    """Sets pg pool for application."""
    return await asyncpg.create_pool(db_url())
