#!/usr/bin/env python3
"""
Task 9
"""


from typing import List, Sequence, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    9-element_length.py
    """
    return [(i, len(i)) for i in lst]
