#!/usr/bin/env python3
"""
Module for type-annotated function `sum_list`
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    sums the values (floating point numbers) of a list

    params:
      input_list: list[float]

    returns:
      sum: float
    """
    return sum(input_list)
