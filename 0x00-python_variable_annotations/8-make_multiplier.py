#!/usr/bin/env python3
"""
Module for type-annotated function `make_multipler`
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns a callable that multiplies a float by multiplier

    params:
      multiplier: float


    returns:
      Callable[[float], float]
    """
    return lambda x: multiplier * x
