#!/usr/bin/env python3
"""
100-safe_first_element.py
"""


from typing import Sequence, Any, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """_summary_

    Args:
        lst (Sequence[Any]): _description_

    Returns:
        Union[Any, None]: _description_
    """
    if lst:
        return lst[0]
    else:
        return None
