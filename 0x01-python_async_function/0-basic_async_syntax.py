#!/usr/bin/env python3
"""Introduces the Basic syntax of asyncio"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Takinteger representing seconds to be delayed and returns actual
       timetaken. """
    if max_delay > 10:
        max_delay = 10
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
