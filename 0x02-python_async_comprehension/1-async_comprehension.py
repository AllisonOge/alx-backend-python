#!/usr/bin/env python3
"""
Module for coroutine `async_comprehension` that takes no args
but the coroutine will collect 10 random numbers using an async
comprehensing over `async_generator` then return the 10 random numbers
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """coroutine doc"""
    return [random async for random in async_generator()]
