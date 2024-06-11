#!/usr/bin/env python3
"""
Module that defines an async routine, `wait_n` that takes 2 integer
arguments (n, max_delay) and spawns wait_random n times with the
specified max_delay
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawn `wait_random` n times"""
    lst_delays = []
    for _ in range(n):
        lst_delays.append(asyncio.create_task(wait_random(max_delay)))
    return sorted(await asyncio.gather(*lst_delays))
