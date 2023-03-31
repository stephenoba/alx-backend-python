#!/usr/bin/env python3
"""
Module contains function `sum_list`
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    function: sum_list(input_list: list[float]) -> float

    Takes a list of floating point number and sums them

    Args
    ----
    n: list[floats]

    Returns
    -------
    Sum of all numbers
    """
    return sum(input_list)
