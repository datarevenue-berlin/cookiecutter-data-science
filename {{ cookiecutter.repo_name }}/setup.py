# coding=utf-8
import versioneer
from setuptools import setup, find_packages

packages = find_packages()

with open('deploy/requirements.txt') as fp:
      deps = fp.readlines()

setup(name='{{cookiecutter.repo_name}}',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='{{cookiecutter.description}}',
      author='Datarevenue UHG',
      author_email='info@datarevenue.de',
      install_requires=deps,
      packages=packages,
      zip_safe=False
      )