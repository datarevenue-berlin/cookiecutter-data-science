FROM drtools/drtools:latest
# Copy over requirements and install them
COPY deploy/requirements.txt /home/drtools/requirements.txt
RUN pip install -r /home/drtools/requirements.txt

# afterwards copy repository and install
COPY {{ cookiecutter.repo_name }} /home/drtools
pip install -e /home/drtools/{{ cookiecutter.repo_name }}