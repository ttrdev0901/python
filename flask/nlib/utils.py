import importlib
import inspect
from logging import (
    getLogger,
    StreamHandler,
    DEBUG, INFO,
    Formatter
)
from typing import List, Dict, Callable

_logger = getLogger(__name__)
sh = StreamHandler()
fmt = Formatter('%(asctime)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
sh.setFormatter(fmt)
sh.setLevel(DEBUG)

def appliable_function() -> List[str]:
    """グループ化操作で使用できる関数のリストを返す関数
    
    Parameters:
    ---------------
    なし

    Returns:
    ---------------
    List[str]
    """
    from . import applicable
    # (funcname, funcobject)
    return [i[0] for i in inspect.getmembers(applicable)]

def plugins_map() -> Dict[str, Callable]:
    """呼び出し可能な関数一覧を辞書型として返す

    Parameters:
    ---------------
    なし

    Returns:
    ---------------
    Dict[]
    """
    plugins = {}
    funcs = appliable_function()
    for func in funcs:
        plugin_load_msg = f"Loading appliable functions/plugins: {func}"
        _logger.info(plugin_load_msg)
        # getattr: モジュールからfuncを取得(func objectとして)
        plugins[func] = getattr(
                            importlib.import_module("nlib.applicable"), 
                            func
                        )
    return plugins