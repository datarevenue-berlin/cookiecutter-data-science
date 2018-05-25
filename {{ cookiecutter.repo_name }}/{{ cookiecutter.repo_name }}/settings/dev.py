from .default import *
DEBUG = True
ROOT = {{ cookiecutter.remote_storage }}

CONTAINER_TASK_ENV = {
    'PYTHONPATH': '/home/drtools/{{ cookiecutter.repo_name }}/'
                  ':/home/drtools/drtools/'
                  ':/home/drtools/sparsity/',
    'DRTOOLS_SETTINGS_MODULE': '{{ cookiecutter.repo_name }}.settings.dev'
}

_modules_path = os.environ.get(
    'MODULES_PATH',
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
)
CONTAINER_TASK_VOLUMES = {
    os.path.join(_modules_path, 'sparsity'):
        {'bind': '/home/drtools/sparsity', 'mode': 'ro'},
    os.path.join(_modules_path, 'drtools'):
        {'bind': '/home/drtools/drtools', 'mode': 'ro'},
    os.path.join(_modules_path, '{{ cookiecutter.repo_name }}'):
        {'bind': '/home/drtools/{{ cookiecutter.repo_name }}', 'mode': 'ro'},
}

CONTAINER_TASK_NET = '{{ cookiecutter.repo_name }}_dev'

CONTAINER_TASK_IMAGE = 'drtools/{{ cookiecutter.repo_name }}:dev'
