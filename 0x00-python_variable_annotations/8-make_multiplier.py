#!/usr/bin/env python3
"""
Module contains function `make_multiplier`"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    function: make_multiplier(multiplier: float) -> Callable[[float], float]

    Args
    ----
    multiplier: float

    Returns
    -------
    A function that takes another float as argument an multiplie by multiplier
    """
    return lambda x: x * multiplier
