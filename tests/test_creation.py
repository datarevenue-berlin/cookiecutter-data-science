import os
import shutil
import subprocess

from cookiecutter import main
import pytest
import docker

CCDS_ROOT = os.path.abspath(
                os.path.join(
                    __file__,
                    os.pardir,
                    os.pardir
                )
            )


@pytest.fixture(scope='function')
def default_baked_project(tmpdir):
    out_dir = str(tmpdir.mkdir('data-project'))

    main.cookiecutter(
        CCDS_ROOT,
        no_input=True,
        extra_context={},
        output_dir=out_dir
    )

    # default project name is project_name
    yield os.path.join(out_dir, 'project_name')

    # cleanup after
    shutil.rmtree(out_dir)


def test_docker_build(default_baked_project):
    c = docker.from_env()
    c.images.build(path=default_baked_project,
                   tag='test-template')


def test_example(default_baked_project):
    c = docker.from_env()
    compose_file = os.path.join(default_baked_project, 'deploy',
                                'docker-compose.yml')

    c.images.build(path=default_baked_project,
                   tag='test-template')

    cmd = 'docker-compose -f {} up -d'.format(compose_file).split()
    subprocess.check_output(cmd)

    cmd = 'DRTOOLS_SETTINGS_MODULE=project_name.settings.default ' \
          'PYTHONPATH={}:$PYTHONPATH luigi ' \
          '--scheduler-host localhost ' \
          '--module project_name.task Example'\
        .format(default_baked_project)
    o = subprocess.check_output(cmd.split(),
                                shell=True, stderr=subprocess.STDOUT)


def test_readme(default_baked_project):
    readme_path = os.path.join(default_baked_project, 'README.md')

    assert os.path.exists(readme_path)
    assert no_curlies(readme_path)


def test_license(default_baked_project):
    license_path = os.path.join(default_baked_project, 'LICENSE')

    assert os.path.exists(license_path)
    assert no_curlies(license_path)


def test_requirements(default_baked_project):
    reqs_path = os.path.join(default_baked_project, 'deploy/requirements.txt')

    assert os.path.exists(reqs_path)
    assert no_curlies(reqs_path)


def test_folders(default_baked_project):
    expected_dirs = [
        'data',
        os.path.join('data', 'external'),
        os.path.join('data', 'interim'),
        os.path.join('data', 'processed'),
        os.path.join('data', 'raw'),
        'docs',
        'models',
        'notebooks',
        'references',
        'reports',
        os.path.join('reports', 'figures'),
        'project_name',
        os.path.join('project_name', 'data'),
        os.path.join('project_name', 'settings'),
        os.path.join('project_name', 'models'),
        os.path.join('project_name', 'analysis')
    ]

    ignored_dirs = [
        default_baked_project,
        ]

    abs_expected_dirs = [os.path.join(default_baked_project, d) for
                            d in expected_dirs]

    abs_dirs, _, _ = list(zip(*os.walk(default_baked_project)))

    assert len(set(abs_expected_dirs + ignored_dirs) - set(abs_dirs)) == 0


def no_curlies(filepath):
    """ Utility to make sure no curly braces appear in a file.
        That is, was jinja able to render everthing?
    """
    with open(filepath, 'r') as f:
        data = f.read()

    template_strings = [
        '{{',
        '}}',
        '{%',
        '%}'
    ]

    template_strings_in_file = [s in data for s in template_strings]

    return not any(template_strings_in_file)
