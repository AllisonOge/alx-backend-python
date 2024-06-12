#!/usr/bin/env python3
"""
Module for a coroutine `async_generator` that takes no arguments
but loops 10 times, each time asynchronously waiting 1 second then
yeilding a random number between 0 and 10
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """coroutine doc"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
