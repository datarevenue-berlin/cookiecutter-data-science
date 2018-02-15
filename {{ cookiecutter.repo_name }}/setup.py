# coding=utf-8
from setuptools import setup, find_packages

packages = find_packages()

with open('deploz/requirements.txt') as fp:
      deps = fp.readlines()

setup(name='{{cookiecutter.repo_name}}',
      version='0.1',
      description='{{cookiecutter.description}}',
      author='Datarevenue UHG',
      author_email='info@datarevenue.de',
      install_requires=deps,
      packages=packages,
      zip_safe=False
      )