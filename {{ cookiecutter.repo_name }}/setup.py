# coding=utf-8
import versioneer
from setuptools import setup, find_packages

packages = find_packages()

with open('requirements.txt') as fp:
    dependencies = fp.readlines()

setup(name='{{cookiecutter.repo_name}}',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='{{cookiecutter.description}}',
      author='Datarevenue GmbH',
      author_email='info@datarevenue.de',
      install_requires=dependencies,
      packages=packages,
      zip_safe=False,
      include_package_data=True
      )
