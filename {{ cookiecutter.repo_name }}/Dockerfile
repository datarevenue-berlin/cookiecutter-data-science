FROM drtools/drtools:latest
USER root

# Add required linux packages
# RUN apk --update add graphviz


# Copy over requirements and install them
COPY requirements.txt /home/drtools/requirements.txt
RUN pip install -r /home/drtools/requirements.txt && \
    rm /home/drtools/requirements.txt

# Copy over repository and install
COPY . /home/drtools/{{ cookiecutter.repo_name }}
RUN pip install -e /home/drtools/{{ cookiecutter.repo_name }}

# Copy configurations into place if needed
COPY conf/dask-config.yml /home/drtools/.dask/config.yml
COPY conf/logging.cfg /etc/luigi/luigi-logging.cfg
COPY conf/luigi.cfg /etc/luigi/client.cfg

USER drtools