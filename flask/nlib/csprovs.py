from logging import (
    getLogger,
    StreamHandler,
    Formatter,
    INFO,DEBUG
)
import pandas as pd
from typing import List

_logger = getLogger(__name__)
sh = StreamHandler()
fmt = Formatter('%(asctime)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
sh.setFormatter(fmt)
sh.setLevel(DEBUG)

def ingest_csv(data) -> pd.DataFrame:
    """Pandasのread_csvでCSVを読み込んでDataframeで返す関数

    Parameters
    ----------
    data : [type]
    
    Returns
    ----------
    pd.DataFrame
    """
    return pd.read_csv(data)

def list_csv_column_names(data) -> List[str]:
    """CSVの列名をリストで返す関数

    Parameters
    ----------
    data : [type]
        
    Returns
    ----------
    List[str]
    """
    df = ingest_csv(data)
    colnames = df.columns.tolist()
    colnames_msg = f"Column Names: {colnames}"
    _logger.info(colnames_msg)
    return colnames

def aggregate_column_name(data, groupby_column_name, apply_column_name) -> pd.DataFrame:
    """CSVを列名で集計した結果をJSON形式で返す関数

    Parameters
    ----------
    data : [type]
        [description]
    groupby_column_name : [type]
        [description]
    apply_column_name : [type]
        [description]
    """
    df = ingest_csv(data)
    return df.groupby(groupby_column_name)[apply_column_name].sum()

def group_by_operations(data, groupby_column_name, apply_column_name, func):
    """関数を無作為に選択してグループ化操作を行う

    Parameters
    ----------
    data : [type]
        [description]
    groupby_column_name : [type]
        [description]
    apply_column_name : [type]
        [description]
    func : [type]
        [description]
    """
    df = ingest_csv(data)
    grouped = df.groupby(groupby_column_name)[apply_column_name]
    applied_data = grouped.apply(func)
    return applied_data