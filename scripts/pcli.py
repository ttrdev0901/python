#!/usr/local/bin/python
"""
PAWSライブラリを動かすコマンドラインツール
"""
import sys

import click
import paws
from paws import s3

@click.version_option(paws.__version__)
@click.group()
def cli():
    """PAWS Tool"""

@cli.command("download")
@click.option("--bucket", help="Name of S3 Bucket")
@click.option("--key", help="Name of S3 key")
@click.option("--filepath", help="Name of file")
def download(bucket, key, filepath):
    """Downloads an S3 file
    ./paws-cli.py download --bucket gdelt-open-data --key events/1979.csv --filename 1979.csv
    """

    if not bucket and not key and not filepath:
        click.echo("--bucket and --key and --filepath are required")
        sys.exit(1)
    click.echo(
            f"Downloading s3 file with: bucket-{bucket}, key-{key}, filepath-{filepath}"
        )
    res = s3.download(bucket=bucket, key=key, filepath=filepath)
    click.echo(res)

if __name__ == '__main__':
    cli()