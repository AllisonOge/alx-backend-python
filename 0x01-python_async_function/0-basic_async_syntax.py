#!/usr/bin/env python3
"""
Module that defines the function `wait_random`
a coroutine that takes an integer argument max_delay
which randomly waits between 0 and max_delay
"""
import random
import asyncio


async def wait_random(max_delay:int = 10) -> float:
    """return a random number between 0 and max_delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
