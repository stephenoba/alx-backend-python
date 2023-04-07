#!/usr/bin/env python3
"""
Module contains function `wait_n` that takes in 2 int arguments
n and max_delay. It will spawn `wait_random` n times with the
specified max_delay
"""
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay

    Args
    ----
    n(int): number of times to spawn wait_random
    max_delay(int): maximum delay

    Returns
    -------
    List of return values from wait_random
    """
    li = [await wait_random(max_delay) for i in range(0, n)]
    return li
