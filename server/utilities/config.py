import os
import pathlib

import pytoml


AIOHTTP_ENV = os.environ["AIOHTTP_ENV"]


def load_config():
    with open(f"{pathlib.Path(__file__).parent.parent}/{AIOHTTP_ENV}.toml") as f:
        return pytoml.load(f)
