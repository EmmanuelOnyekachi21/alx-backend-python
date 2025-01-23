#!/usr/bin/env python3
"""Uses a task creator to run multiple task concurrently"""

from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Runs the wait_random coroutine n times"""
    tasks = [task_wait_random(max_delay) for i in range(n)]
    wait_times = []
    for future in asyncio.as_completed(tasks):
        result = await future
        wait_times.append(result)
    return wait_times
