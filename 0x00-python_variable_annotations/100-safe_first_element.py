#!/usr/bin/env python3
"""
Module contains function safe_first_element
"""
from typing import Any, Iterable


# The types of the elements of the input are now know
def safe_first_element(lst: Iterable[Any]) -> Any:
    if lst:
        return lst[0]
    else:
        return None
