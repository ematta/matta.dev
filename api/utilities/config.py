import os
import pathlib

from cryptography.fernet import Fernet
import pytoml


APP_ENV = os.environ["APP_ENV"]
APP_ROOT = pathlib.Path(__file__).parent.parent.parent


def load_config():
    config = {}
    with open(f"{APP_ROOT}/{APP_ENV}.toml") as f:
        config = pytoml.load(f)
    config["secret_key"] = Fernet.generate_key()
    return config


config = load_config()
