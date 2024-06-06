#!/usr/bin/env python3
"""
Module for type-annotated function `sum_mixed_list`
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    sums the values (floating point numbers or integers) of a list

    params:
      input_list: List[Union[int, float]]

    returns:
      sum: float
    """
    return float(sum(mxd_lst))
