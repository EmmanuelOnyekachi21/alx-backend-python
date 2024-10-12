#!/usr/bin/env python3
"""
102-type_checking.py
"""


from typing import List, Any


def zoom_array(lst: List[Any], factor: int = 2) -> List[Any]:
    """_summary_

    Args:
        lst (List[Any]): _description_
        factor (int, optional): _description_. Defaults to 2.

    Returns:
        List[Any]: _description_
    """
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
