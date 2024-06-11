#!/usr/bin/env python3
"""
Module that alters the `wait_n` function into `task_wait_n` function
"""
import asyncio
import random
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """alters `wait_n` into `task_wait_n`"""
    lst_delays = []
    for _ in range(n):
        lst_delays.append(task_wait_random(max_delay))
    return sorted(await asyncio.gather(*lst_delays))
