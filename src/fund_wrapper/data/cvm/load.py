import pandas as pd
from fund_wrapper.data.cvm.preprocess import parse_data_set


def load_cvm_dataset(path):
    return pd.read_csv(
        path, encoding='latin2', sep=';'
    )


def load_parsed_csv_dataset(path) -> pd.DataFrame:
    df = load_cvm_dataset(path)
    df = parse_data_set(df)
    return df
