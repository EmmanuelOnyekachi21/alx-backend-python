#!/usr/bin/env python3
"""
A type-annotated function sum_mixed_list which takes a list of integers,
and floats and returns their sum as a float.
"""

from typing import Union


def sum_mixed_list(mxd_lst: Union[int, float]) -> float:
    """
    takes a list of integers and floats and returns their sum as a float.
    """
    sum: float = 0.0

    for val in mxd_lst:
        sum += val

    return float(sum)
