import click
import pandas as pd
from dask import delayed
from distributed import Client
from drtools.utils.log import get_logger

from ..structure import PATH


@click.command()
def cli():
    c = Client('dask-scheduler:8786')
    log = get_logger(__name__)

    log.info('Connected to scheduler')

    df = delayed(pd.read_csv)(PATH['CS_IN']).compute()

    log.info('Clickstream loaded:\n{}'.format(str(df)))

    df.to_pickle(PATH['CS_OUT'])


if __name__ == '__main__':
    cli()
