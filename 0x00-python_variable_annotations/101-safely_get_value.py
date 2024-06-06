#!/usr/bin/env python3
"""
Module for type-annotated function `safely_get_value`
"""
from typing import Mapping, Any, Union, TypeVar


T = TypeVar("T")
def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """function with more involved type annotations"""
    if key in dct:
        return dct[key]
    else:
        return default
