import asyncio
import os
import pathlib
import sys

from server.utilities.logger import logger


def load_module(module):
    module_path = module
    if module_path in sys.modules:
        return sys.modules[module_path]
    return __import__(module_path, fromlist=[module])


if __name__ == "__main__":
    logger.info("Starting migration")
    for filename in sorted(os.listdir(f"{pathlib.Path(__file__).parent}/migrate")):
        if filename.endswith(".py") and not filename.startswith("__init__"):
            migrate_module = f"migrate.{filename.replace('.py', '')}"
            logger.info(f"processing {migrate_module}")
            _migrate = load_module(migrate_module)
            asyncio.get_event_loop().run_until_complete(_migrate.migrate())
            logger.info(f"{migrate_module} finished")
    logger.info("Finished migration")
