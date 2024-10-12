#!/usr/bin/env python3
"""
Takes a string k and an int OR float v as arguments and returns a tuple.
"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple where the first element is a string,
    and the second is the square of v."""
    return (k, float(v ** 2))
