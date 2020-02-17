import asyncio
import os
import pathlib
import sys

from server.utilities.logger import logger
from server.database.postgres import init_pg_pool

def load_module(module):
    module_path = module
    if module_path in sys.modules:
        return sys.modules[module_path]
    return __import__(module_path, fromlist=[module])

async def exec_migrate(migrate_module):
    pool = await init_pg_pool()
    async with pool.acquire() as conn:
        logger.info(f"processing {migrate_module}")
        _migrate = load_module(migrate_module)
        await _migrate.migrate(conn)
        logger.info(f"{migrate_module} finished")

if __name__ == "__main__":
    logger.info("Starting migration")
    for filename in sorted(os.listdir(f"{pathlib.Path(__file__).parent}/migrate")):
        if filename.endswith(".py") and not filename.startswith("__init__"):
            migrate_module = f"migrate.{filename.replace('.py', '')}"
            asyncio.get_event_loop().run_until_complete(exec_migrate(migrate_module))
    logger.info("Finished migration")
