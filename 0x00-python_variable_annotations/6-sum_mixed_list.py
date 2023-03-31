#!/usr/bin/env python3
"""
Module contains function `sum_mixed_list`
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    function: sum_mixed_list(mxd_lst: List[int | float]) -> float

    Takes a list of numbers and sums them

    Args
    ----
    mxd_lst: list[int | floats]

    Returns
    -------
    Sum of all numbers
    """
    return sum(mxd_lst)
