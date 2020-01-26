import asyncpg


def db_url(config):
    return (
        "postgresql://"
        f"{config['POSTGRES_USER']}:{config['POSTGRES_PASSWORD']}"
        f"@{config['POSTGRES_URL']}:{config['POSTGRES_PORT']}/{config['POSTGRES_DB']}"
    )


async def init_db_pool(app):
    pool = await asyncpg.create_pool(db_url(app["config"]["database"]))
    app["db_pool"] = pool
    return pool
