#!/usr/bin/env python3
"""
Contains coroutine measure_runtime
"""
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the time to run four async comprehensions

    Args
    ----
    None

    Returns
    -------
    The total time it takes
    """
    start = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    return time.perf_counter() - start
