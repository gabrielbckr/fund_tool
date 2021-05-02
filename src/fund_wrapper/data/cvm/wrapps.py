import os
import zipfile
import requests
import pandas as pd
from bs4 import BeautifulSoup

from fund_wrapper.data.cvm.load import load_parsed_csv_dataset
from fund_wrapper import constants


def get_available_file_names_from_cvm():
    html_page = requests.get(constants.WRAPPER.ADDR).content
    soup = BeautifulSoup(html_page, features='html.parser')
    page_item_list = soup.find_all('td', attrs={'class': 'indexcolname'})
    page_item_list_content = [i.find('a').text for i in page_item_list]
    available_files = list(filter(lambda x: 'zip' in x, page_item_list_content))
    return available_files


def download_file_and_extract_csv(file):
    assert 'zip' in file
    temp_filename = constants.WRAPPER.TEMP_FILE
    zip_temp_filename = constants.WRAPPER.CVM_DATA_PATH

    response = requests.get(constants.WRAPPER.ADDR + file)
    with open(temp_filename, 'wb+') as zip_file:
        zip_file.write(response.content)

    with zipfile.ZipFile(temp_filename) as zip:
        zip.extractall(zip_temp_filename)

    os.remove(temp_filename)


def download_all_csv_files():
    files = get_available_file_names_from_cvm()
    for file in files:
        download_file_and_extract_csv(file)


def preprocess_all_dataset():
    data_path = constants.WRAPPER.CVM_DATA_PATH

    ballance_codes = {'BPA', 'BPP'}
    is_ballance_doc = lambda x: any(map(lambda b: b in x, ballance_codes))
    files = list(filter(is_ballance_doc, os.listdir(data_path)))

    prepared_datasets = []
    for file in files:
        prepared_datasets.append(
            load_parsed_csv_dataset(data_path.joinpath(file))
        )

    all_in_one_df = pd.concat(prepared_datasets)
    return all_in_one_df


def process_and_save_all_cvm_datasets():
    df = preprocess_all_dataset()
    df.to_pickle(constants.WRAPPER.ALL_ON_ONE_DF_DIR)
