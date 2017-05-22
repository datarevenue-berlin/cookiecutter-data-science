FROM drtools/base:dev
COPY requirements.txt /requirements.txt
COPY luigi.cfg /etc/luigi/client.cfg
COPY luigi_logging.cfg /etc/luigi/luigi_logging.cfg
RUN pip3 install -r requirements.txt
