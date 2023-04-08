#!/usr/bin/env python3
"""
Contains the async_generator function
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Generator that yields a random number between 0 - 10

    Args
    ----
    None

    Returns
    -------
    A generator of random floats
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
