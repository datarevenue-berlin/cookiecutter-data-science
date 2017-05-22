# coding=utf-8
from setuptools import setup, find_packages

packages = find_packages()

setup(name='{{cookiecutter.repo_name}}',
      version='0.1',
      description='{{cookiecutter.description}}',
      author='Datarevenue UHG',
      author_email='info@datarevenue.de',
      dependency_links = ['git+ssh://git@github.com/datarevenue-berlin/drtools_base.git@master#egg=drtools-{{cookiecutter.drtools_version}}'],
      install_requires=['drtools>={{cookiecutter.drtools_version}}'],
      packages=packages,
      package_data={'{{cookiecutter.repo_name}}.features': ['*.csv']},
      zip_safe=False
      )