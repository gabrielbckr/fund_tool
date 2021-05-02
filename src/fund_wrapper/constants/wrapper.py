import os
from pathlib import Path


class WRAPPER:
    TEMP_FILE = 'tempfile.zip'
    CVM_DATA_PATH = os.getenv('CVM_DATA_PATH', Path(__file__).parents[3].joinpath('data'))
    ADDR = 'http://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/'
    ALL_ON_ONE_DF_DIR = os.getenv('CVM_DATA_PATH', Path(__file__).parents[3].joinpath('data/all_in_one.pickle'))
