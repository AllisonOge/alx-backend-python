#!/usr/bin/env python3
"""
Module that defines the function `wait_random`
a coroutine that takes an integer argument max_delay
which randomly waits between 0 and max_delay
"""
import random


def wait_random(max_delay=10):
    """return a random number between 0 and max_delay"""
    return random.randint(0, max_delay)
