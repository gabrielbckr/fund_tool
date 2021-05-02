import pandas as pd
from fund_wrapper.constants.columns.cvm import DFP


def parse_data_set(df: pd.DataFrame) -> pd.DataFrame:
    df[DFP.DATE] = pd.to_datetime(df[DFP.DATE])
    df = filter_main_accounts(df)
    df = fix_account_value_scale(df)
    return df


def filter_main_accounts(df: pd.DataFrame) -> pd.DataFrame:
    main_accounts = df[DFP.ACCOUNT].apply(
        lambda x: len(x.replace(',', '.').split('.')) <= 2
    )
    df = df[main_accounts].copy()
    return df


def fix_account_value_scale(df: pd.DataFrame) -> pd.DataFrame:
    assert {DFP.ACCOUNT_VALUE, DFP.MONETARY_SCALE}.issubset(df.columns)

    factors = {'MIL': 1e3, 'UNIDADE': 1}

    multiplying_factor = df[DFP.MONETARY_SCALE].apply(lambda x: factors[x])
    df[DFP.ACCOUNT_VALUE] *= multiplying_factor

    df.drop(DFP.MONETARY_SCALE, axis=1, inplace=True)
    return df
