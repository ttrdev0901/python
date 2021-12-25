import boto3
from logging import getLogger
from typing import Optional, Dict, List

_logger = getLogger("paws")




def create_boto_s3_resource():
    """Boto3 s3リソース作成

    Parameters:
    -----------------
    なし

    Returns:
    -----------------
    s3 resource
    """
    return boto3.resource('s3')

def download(bucket: str, key: str, filepath: str, resource=None) -> str:
    """s3からファイルをダウンロードする関数

    Parameters
    ----------
    bucket : str
        バケット名
    key : str
        キー
    filename : str
        保存ファイル名
    resource : boto3.resource, optional
        , by default None
    """
    if resource is None:
        resource = create_boto_s3_resource()
    
    log_msg = f"Attempting download: {bucket}, {key}, {filepath}"
    _logger.info(log_msg)

    resource.Object(bucket_name=bucket, key=key).download_file(filepath)

    return filepath
    