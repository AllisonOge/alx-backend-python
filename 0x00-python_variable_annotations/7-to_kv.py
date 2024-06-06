#!/usr/bin/env python3
""""
Module for type-annotated function `to_kv`
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    convert key (str) and value (integer or floating point number) to tuple

    params:
      k: str
      v: Union[int, float]

    returns:
      Tuple[str, float]
    """
    return (k, v**2)
