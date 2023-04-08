#!/usr/bin/env python3
"""
Contains coroutine `async_comprehension
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collect 10 random numbers using an async
    comprehensing over async_generator, then
    return the 10 random numbers.

    Args
    ----
    None

    Returns
    -------
    10 random numbers from async_generator
    """
    return [i async for i in async_generator()]
