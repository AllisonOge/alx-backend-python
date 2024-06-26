#!/usr/bin/env python3
"""
Module for type-annotated function `zoom_array`
"""
from typing import List


def zoom_array(lst: List[int], factor: int = 2) -> List:
    """scale list by factor

    params:
      lst: List[int]
      factor: int default = 2
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
