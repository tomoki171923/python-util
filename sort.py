# -*- coding: utf-8 -*-
from typing import List

from enum import IntEnum, auto

class Enum(IntEnum):
    ASC = auto()
    DESC = auto()


""" sort a list contains dict objects.
Args:
    li (list): the target list.
    n (int): the number to split.
    order (int, optional): order type.
Returns:
    list: sorted list.
e.g.
    from base_enum import Enum
    l = [{'name': 'suzuki', 'score': 80}, {'name': 'tanaka', 'score': 30}, {'name': 'sato', 'score': 100}],
    sort_key="score",
    order = Enum.DESC
    # => [{'name': 'sato', 'score': 100}, {'name': 'suzuki', 'score': 80}, {'name': 'tanaka', 'score': 30}]
"""


def sortDict(li: List[dict], sort_key: str, order: int = Enum.DESC) -> List[dict]:
    if type(li) is not list:
        raise TypeError("li is invalid type.")
    reverse: bool
    if order is Enum.DESC:
        reverse = True
    elif order is Enum.ASC:
        reverse = False
    sorted_list = sorted(li, key=lambda x: x[sort_key], reverse=reverse)
    return sorted_list
