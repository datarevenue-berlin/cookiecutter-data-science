import os
import pandas as pd

DEBUG = True

DATA_DIR = "{{ cookiecutter.storage_protocol }}://{{ cookiecutter.bucket }}/data/"
RAW_DIR = "{{ cookiecutter.storage_protocol }}://{{ cookiecutter.bucket }}/data/raw"
PROCESSED_DIR = "{{ cookiecutter.storage_protocol }}://{{ cookiecutter.bucket }}/data/processed"


# ---------------------- DEFAULT COLS --------------------

ID_COL = "id"
DATE_COL = "date"
TARGET_COL = "target"

# ====== FEATURES =======

DEFAULT_TRAIN_DATES = pd.date_range("2016-10-01", "2016-10-31").date
DEFAULT_N_TEST_DAYS = 6

# Slicing
DATA_DELAY = {{ cookiecutter.data_delay }}
DEFAULT_N_AGG_DAYS = {{ cookiecutter.aggregation_window }}
LEAD_WINDOW_SIZE = {{ cookiecutter.lead_window }}

DEFAULT_TRAIN_SAMPLE = 10
DEFAULT_TEST_SAMPLE = 1

TIME_BINS = [
    (0, DEFAULT_N_AGG_DAYS)
]
