# -*- coding: utf-8 -*-
from typing import Generator

""" split a list.
e.g.
    li=[1,2,3,4,5,6,7], m=3 # => [[1, 2, 3], [4, 5, 6], [7]]
Args:
    li (list): the target list.
    n (int): the number to split.
Returns:
    generator: splited lists.
"""


def splitList(li: list, n: int) -> Generator[list, None, None]:
    if type(li) is not list:
        raise TypeError("l is invalid type.")
    if type(n) is not int:
        raise TypeError("n is invalid type.")
    for idx in range(0, len(li), n):
        yield li[idx: idx + n]
