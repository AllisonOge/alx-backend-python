#!/usr/bin/env python3
"""
Module for coroutine `measure_runtime` that will execute
`async_comprehension` four times in parallel using
asyncio.gather
"""
import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """coroutine doc"""
    start_tm = time.perf_counter()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension()
                         )
    end_tm = time.perf_counter()
    return end_tm - start_tm
