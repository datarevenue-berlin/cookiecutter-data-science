FROM drtools/base:main
RUN pip3 install git@github.com/daterevenue-berlin/{{cookiecutter
.repo_name}}.git --no-index -f /wheelhouse
ENV DRTOOLS_SETTINGS_MODULE={{ cookiecutter.repo_name }}.settings.production