import logging

from api.utilities.config import config

logger = logging.getLogger(__name__)
logger.setLevel(config['app']['LOGGER_LEVEL'])

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh = logging.FileHandler('api.log')
fh.setLevel(config['app']['LOGGER_LEVEL'])
fh.setFormatter(formatter)

ch = logging.StreamHandler()
ch.setLevel(config['app']['LOGGER_LEVEL'])
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)
