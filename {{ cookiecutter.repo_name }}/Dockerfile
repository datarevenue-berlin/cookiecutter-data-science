FROM drtools/drtools:latest
USER root
# Copy over requirements and install them
COPY deploy/requirements.txt /home/drtools/requirements.txt
RUN pip install -r /home/drtools/requirements.txt && \
    rm /home/drtools/requirements.txt

# afterwards copy repository and install
COPY . /home/drtools/{{ cookiecutter.repo_name }}
RUN pip install -e /home/drtools/{{ cookiecutter.repo_name }}

USER drtools