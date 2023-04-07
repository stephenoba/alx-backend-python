#!/usr/bin/env python3
"""
Module contains a measure_time function
"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay):
    """
    Measures the total execution time for wait_n(n, max_delay)

    Args
    ----
    n(int): number of times to spawn wait_random
    max_delay(int): maximum delay

    Returns
    -------
    Total time divided by the number or times to spawn wait_random
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start
    return total_time / n
