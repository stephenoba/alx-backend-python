#!/usr/bin/env python3
"""
Module contains fix for  function element_length
"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Fix for function
    """
    return [(i, len(i)) for i in lst]
