#!/usr/bin/env python3
"""
A type-annotated function sum_list which takes a list of floats as argument,
and returns their sum as a float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """takes a list of floats as argument and returns their sum as a float

    Args:
        input_list (List[float]): List containing the floats

    Returns:
        float: sum of the floats in the list
    """
    sum: float = 0.0
    for val in input_list:
        sum += val
        
    return sum
