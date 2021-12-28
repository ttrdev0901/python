import numpy as np

def tanimoto(list1: list, list2:list) -> float:
    """tanimoto係数

    Parameters
    ----------
    list1 : list
        
    list2 : list
    
    Returns
    ----------
    float
    """

    # 共通部分の集合
    intersection = set(list1).intersection(set(list2))
    return float(len(intersection)/(len(list1) + len(list2) - len(intersection)))

def npsum(x) -> float:
    """Numpyのsum関数

    Parameters
    ----------
    x : array-like

    Return
    ----------
    float
    """
    return np.sum(x)

def npmedian(x) -> float:
    """Numpyのmedian関数

    Parameters
    ----------
    x : array-like

    Returns
    -------
    float
    """
    return np.median(x)
