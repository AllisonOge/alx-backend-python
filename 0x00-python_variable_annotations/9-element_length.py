#!/usr/bin/env python3
"""
Module for type-annotated function `element_length`
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    list of tuple of iterable sequence

    params:
      lst: Iterable[Sequence]
    """
    return[(i, len(i)) for i in lst]
