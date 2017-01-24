FROM drtools/base:main
RUN pip3 install {{cookiecutter.repo_name}} --no-index -f /wheelhouse
ENV DRTOOLS_SETTINGS_MODULE={{ cookiecutter.repo_name }}.settings.settings