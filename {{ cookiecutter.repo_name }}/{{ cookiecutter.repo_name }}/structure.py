"""Define global project (file-)structure here.

This module is used to define all filepaths and/or keys
used in the project. the __factory function is used to build
these paths or path templates on settings or environment variables.
"""

from os import path
from drtools.conf import settings

PATH = {}
PATH_TEMPLATE = {}


def __factory():
    global PATH_TEMPLATE
    global PATH
    PATH.update({
        'ROOT': settings.ROOT,
        'RAW_DATA_DIR': path.join(settings.ROOT, 'data', 'raw/'),
        'PROCESSED_DIR': path.join(settings.ROOT, 'data', 'processed/'),
        'EVAL_DIR': path.join(settings.ROOT, 'models/')
    })
    PATH_TEMPLATE.update({
    })


__factory()


def refresh():
    __factory()