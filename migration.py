import asyncio
import os
import pathlib
import sys


def load_module(module):
    module_path = module
    if module_path in sys.modules:
        return sys.modules[module_path]
    return __import__(module_path, fromlist=[module])


if __name__ == "__main__":
    for filename in os.listdir(f"{pathlib.Path(__file__).parent}/migrate"):
        if filename.endswith(".py") and not filename.startswith("__init__"):
            migrate_module = f"migrate.{filename.replace('.py', '')}"
            _migrate = load_module(migrate_module)
            asyncio.get_event_loop().run_until_complete(_migrate.migrate())
