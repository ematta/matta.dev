"""Configuration processor."""
import os
from pathlib import Path
from typing import Dict

from cryptography.fernet import Fernet


import pytoml


APP_ENV: "str" = os.environ["APP_ENV"]
APP_ROOT: "str" = str(Path(__file__).parent.parent.parent)
SERVER_ROOT: "str" = str(Path(__file__).parent.parent)


def load_config() -> "Dict":
    """Returns configuration.

    Loads from [env].toml file and adds `secret_key` and `posts` location.
    """
    config: "Dict" = {}
    with open(f"{APP_ROOT}/{APP_ENV}.toml") as f:
        config = pytoml.load(f)
    config["secret_key"] = Fernet.generate_key()
    return config


config: "Dict" = load_config()
