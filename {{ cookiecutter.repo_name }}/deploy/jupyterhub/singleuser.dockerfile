FROM drtools/{{cookiecutter.repo_name}}-worker:dev

COPY start-singleuser.sh /usr/local/bin/start-singleuser.sh

EXPOSE 8888
RUN pip install jupyterhub==0.7.2
RUN sh /usr/local/bin/start-singleuser.sh -h
RUN rm -rf /usr/etc/jupyter
CMD ["tini", "sh", "/usr/local/bin/start-singleuser.sh"]