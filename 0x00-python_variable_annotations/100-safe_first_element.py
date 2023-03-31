#!/usr/bin/env python3
"""
Module contains function safe_first_element
"""
from typing import Any, Sequence, Union


# The types of the elements of the input are now know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Anottatded funcctionß
    """
    if lst:
        return lst[0]
    else:
        return None
