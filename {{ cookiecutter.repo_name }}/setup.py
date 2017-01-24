# coding=utf-8
from setuptools import setup, find_packages

packages = find_packages()

setup(name='{{cookiecutter.pkg_name}}',
      version='0.1',
      description='{{cookiecutter.project_description}}',
      url='{{cookiecutter.project_url}}',
      author='Datarevenue',
      author_email='info@datarevenue.de',
      dependency_links = ['git+ssh://git@github.com/Haikane/drtools_base.git@master#egg=drtools-{{cookiecutter.drtools_version}}'],
      install_requires=['drtools>={{cookiecutter.drtools_version}}'],
      packages=packages,
      zip_safe=False)