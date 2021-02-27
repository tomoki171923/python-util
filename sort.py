# -*- coding: utf-8 -*-
from typing import Generator

''' sort a list contains dict objects.

Args:
    l (list): the target list.
    n (int): the number to split.
Returns:
    list: sorted list.
e.g.
    l = [
        {
            "name": "suzuki",
            "score": 80
        },
        {
            "name": "tanaka",
            "score": 30
        },
        {
            "name": "sato",
            "score": 100
        }
    ], sort_key="score"
    # => [
        {
            "name": "sato",
            "score": 100
        },
        {
            "name": "suzuki",
            "score": 80
        },
        {
            "name": "tanaka",
            "score": 30
        }
    ]
'''


def sortDict(l: list, sort_key: str) -> list:
    if type(l) is not list:
        raise TypeError('l is invalid type.')
    sorted_list = sorted(l, key=lambda x:x[sort_key], reverse=True)
    return sorted_list

