import os
import pathlib

import pytoml


AIOHTTP_ENV = os.environ["AIOHTTP_ENV"]
APP_ROOT = pathlib.Path(__file__).parent.parent.parent


def load_config():
    with open(f"{APP_ROOT}/{AIOHTTP_ENV}.toml") as f:
        return pytoml.load(f)
