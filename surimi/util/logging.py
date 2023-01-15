import logging
from logging import Logger, Formatter, StreamHandler, FileHandler
from tempfile import gettempdir
from pathlib import Path


def setup_logger(logger: Logger):
    if logger.hasHandlers():
        logger.handlers.clear()

    logger.setLevel(logging.DEBUG)

    formatter = Formatter('%(name)s:{%(levelname)s}: %(message)s')

    stream_handler = StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    filepath = Path(gettempdir()) / ('name' + '.log')

    logger.info('Logging into: ' + str(filepath))

    file_handler = FileHandler(filepath, mode='w')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
