#!/usr/bin/env python

import sys
import click
from logging import (
    getLogger,
    StreamHandler,
    DEBUG, INFO,
    Formatter
)
from nlib.utils import appliable_functions
import nlib
from nlib import csprovs
from nlib import utils

_logger = getLogger(__name__)
sh = StreamHandler()
fmt = Formatter('%(asctime)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
sh.setFormatter(fmt)
sh.setLevel(DEBUG)

@click.version_option(nlib.__version__)
@click.group()
def cli():
    """CSV操作ツール
    """

@cli.command("csvprovs")
@click.option("--file", help="Name of csv file")
@click.option("--groupby", help="GroupBy Column Name")
@click.option("--applyname", help="Apply Column Name")
@click.option("--func", help="Appliable Function")
def agg(file, groupby, applyname, func):
    """CSVファイルの列にグループ化を行い、関数を適用する

    Parameters
    ----------
    file : [type]
        [description]
    groupby : [type]
        [description]
    applyname : [type]
        [description]
    func : [type]
        [description]
    """
    if not file and not groupby and not applyname and not func:
        click.echo("--file and --column and --applyname and --func are required")
        sys.exit(1)
    
    click.echo(f"Processing csvfile: {file} and groupby name: {groupby} and applyname] {applyname}")
    plugins = utils.plugins_map()
    appliable_func = plugins[func]
    res = csprovs.group_by_operations(
                                    data=file,
                                    groupby_column_name=groupby,
                                    apply_column_name=applyname,
                                    func=appliable_func
                                    )
    click.echo(res)

@cli.command("listfuncs")
def listfuncs():
    """グループ化操作に使用できる関数のリストを作成
    """
    funcs = utils.appliable_functions()
    click.echo(f"Appliable Functions: {funcs}")

if __name__ == "__main__":
    cli()
