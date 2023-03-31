#!/usr/bin/env python3
"""
Module contains function to_kv"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    function: to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]

    Args
    ----
    k: string
    v: int or  float

    Returns
    -------
    A Tuple of  string k and square of v
    """
    return k, v ** 2
