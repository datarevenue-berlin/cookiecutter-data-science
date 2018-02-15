"""Define global project (file-)structure here.

This module is used to define all filepaths and/or keys
used in the project. the __factory function is used to build
these paths or path templates on settings or environment variables.

Naming convention:
all caps for paths and lower case names for path templates.
"""

from os import path
from drtools.conf import settings

PATH_TEMPLATES = {}


def __factory():
    global PATH_TEMPLATES

    # DATA_DIR = os.path.join(settings.ROOT, 'data/')
    RAW_DATA_DIR = path.join(settings.ROOT, 'data', 'raw/')
    PROCESSED_DIR = path.join(settings.ROOT, 'data', 'processed/')
    EVAL_DIR = path.join(settings.ROOT, 'models/')
    PATH_TEMPLATES.update({
        'EVAL_DIR':EVAL_DIR,
    })


__factory()


def refresh():
__factory()