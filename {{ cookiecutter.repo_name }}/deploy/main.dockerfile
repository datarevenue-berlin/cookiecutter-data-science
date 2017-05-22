FROM drtools/base:main
COPY luigi.cfg /etc/luigi/client.cfg
COPY luigi_logging.cfg /etc/luigi/luigi_logging.cfg
RUN curl https://bootstrap.pypa.io/ez_setup.py -o - | python3.5 && easy_install pip

COPY wheelhouse /home/ubuntu/wheelhouse
RUN apt-get install -y libgomp1 libsnappy-dev

RUN pip install /home/ubuntu/wheelhouse/xgboost-0.6a2-cp35-cp35m-linux_x86_64.whl \
    --no-index \
    -f /home/ubuntu/wheelhouse

RUN pip install {{cookiecutter.repo_name}} \
    --no-index \
    -f /home/ubuntu/wheelhouse

# CUSTOM SECTION
# Add feature files, credentials, run tests..