import os

import sys
from logging import getLogger

from .default import *
from pathlib import Path
DEBUG = True



CONTAINER_TASK_ENV = {
    'PYTHONPATH': '/home/drtools/{{ cookiecutter.repo_name }}/'
                  ':/home/drtools/drtools/'
                  ':/home/drtools/sparsity/',
    'DRTOOLS_SETTINGS_MODULE': '{{ cookiecutter.repo_name }}.settings.dev'
}

try:
    _modules_path = Path(os.environ['MODULES_PATH'])

    _sparsity = _modules_path.joinpath('sparsity')
    _drtools = _modules_path.joinpath('drtools_base')

    CONTAINER_TASK_VOLUMES.update({
        str(_modules_path.joinpath('{{ cookiecutter.repo_name }}')):
            {'bind': '/home/drtools/{{ cookiecutter.repo_name }}',
             'mode': 'ro'},
    })

    CONTAINER_TASK_VOLUMES[str(_sparsity)] = \
        {'bind': '/home/drtools/sparsity', 'mode': 'ro'}

    CONTAINER_TASK_VOLUMES[str(_drtools)] = \
        {'bind': '/home/drtools/drtools', 'mode': 'ro'}

except KeyError:
    if os.environ.get('CONTROLLER', False):
        log = getLogger(__name__)
        log.critical("Can't use controller with dev settings "
                     "without specifying MODULES_PATH")
        sys.exit(1)
