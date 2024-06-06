#!/usr/bin/env python3
"""
Module for type-annotated function `safe_first_element`
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    wrapper around list
    """
    if lst:
        return lst[0]
    else:
        return None
