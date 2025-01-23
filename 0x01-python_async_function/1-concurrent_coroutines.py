#!/usr/bin/env python3
"""Introduces the Basic syntax of asyncio to perform concurrency"""

from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Runs the wait_random coroutine n times"""
    tasks = [wait_random(max_delay) for i in range(n)]
    wait_times = []
    for future in asyncio.as_completed(tasks):
        result = await future
        wait_times.append(result)
    return wait_times
