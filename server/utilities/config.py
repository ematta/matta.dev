"""Configuration processor."""
import os
from pathlib import Path
from typing import Dict

from cryptography.fernet import Fernet


APP_ENV: "str" = os.environ["APP_ENV"]
APP_ROOT: "str" = str(Path(__file__).parent.parent.parent)
SERVER_ROOT: "str" = str(Path(__file__).parent.parent)


def load_config() -> "Dict":
    """Returns configuration.

    Loads from env vars
    """
    datbase: "Dict" = {
        "POSTGRES_URL": os.environ["POSTGRES_URL"],
        "POSTGRES_PORT": os.environ["POSTGRES_PORT"],
        "POSTGRES_USER": os.environ["POSTGRES_USER"],
        "POSTGRES_PASSWORD": os.environ["POSTGRES_PASSWORD"],
        "POSTGRES_DB": os.environ["POSTGRES_DB"],
    }
    redis: "Dict" = {
        "REDIS_HOST": os.environ["REDIS_HOST"],
        "REDIS_PORT": os.environ["REDIS_PORT"],
    }
    dropbox: "Dict" = {
        "ACCESS_TOKEN": os.environ["ACCESS_TOKEN"],
    }
    return {
        "LOGGER_LEVEL": os.getenv("LOGGER_LEVEL", 20),
        "SECRET_KEY": Fernet.generate_key(),
        "datbase": datbase,
        "redis": redis,
        "dropbox": dropbox,
    }


config: "Dict" = load_config()
