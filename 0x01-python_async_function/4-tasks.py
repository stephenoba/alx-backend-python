#!/usr/bin/env python3
"""
Contains function `task_wait_n`
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Identical to the `wait_n` function, this calls task_wait_random instead

    Args
    ----
    n(int): number of times  to spawn
    max_delay(int): Max Delay

    Returns
    -------
    A List of random float numbers
    """
    li = [await task_wait_random(max_delay) for i in range(0, n)]
    return sorted(li)
