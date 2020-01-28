"""Creates logger."""
from logging import FileHandler, Formatter, StreamHandler, getLogger
from typing import TYPE_CHECKING

from server.utilities.config import config


if TYPE_CHECKING:
    from logging import Logger

logger: "Logger" = getLogger(__name__)
logger.setLevel(config["LOGGER_LEVEL"])

formatter: "Formatter" = Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

fh: "FileHandler" = FileHandler("server.log")
fh.setLevel(config["app"]["LOGGER_LEVEL"])
fh.setFormatter(formatter)

ch: "StreamHandler" = StreamHandler()
ch.setLevel(config["app"]["LOGGER_LEVEL"])
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)
