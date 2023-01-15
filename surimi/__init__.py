import logging

from . import global_data
from .registration import register_core, unregister_core
from .util.register import cleanse_modules
from .util.logging import setup_logger

bl_info = {
    'name': 'Surimi Toolkit',
    'author': 'piparkaq',
    'version': (0, 1, 0),
    'blender': (2, 80, 0),
    'warning': 'Experimental',
    'category': 'Splatoon',
}

logger = logging.getLogger(__name__)


def register():
    setup_logger(logger)

    try:
        register_core()
        global_data.registered = True
    except Exception as e:
        global_data.registered = False


def unregister():
    if global_data.registered:
        unregister_core()

    cleanse_modules(__package__)
