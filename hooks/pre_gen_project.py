import re
import sys

from subprocess import check_output, CalledProcessError

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.repo_name }}'


def check_versioneer():
    try:
        check_output(['versioneer', '--version'])
    except:
        return False
    return True


def check_git():
    try:
        check_output('git --version'.split(' '))
    except:
        return False
    return True


if not re.match(MODULE_REGEX, module_name):
    print('ERROR: %s is not a valid Python module name!' % module_name)

    # exits with status 1 to indicate failure
    sys.exit(1)


if not check_versioneer():
    print('ERROR: versioneer is not installed!')

    # exits with status 1 to indicate failure
    sys.exit(1)


if not check_git():
    print('ERROR: git is not installed!')

    # exits with status 1 to indicate failure
    sys.exit(1)
