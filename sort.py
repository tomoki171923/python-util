# -*- coding: utf-8 -*-
from typing import List
import os

if "AWS_LAMBDA_FUNCTION_VERSION" in os.environ:
    from .base_enum import BaseEnum  # "." is required on AWS Lambda Layer.
else:
    from base_enum import BaseEnum


""" sort a list contains dict objects.
Args:
    li (list): the target list.
    n (int): the number to split.
    order (int, optional): order type.
Returns:
    list: sorted list.
e.g.
    from base_enum import BaseEnum
    l = [{'name': 'suzuki', 'score': 80}, {'name': 'tanaka', 'score': 30}, {'name': 'sato', 'score': 100}],
    sort_key="score",
    order = BaseEnum.DESC
    # => [{'name': 'sato', 'score': 100}, {'name': 'suzuki', 'score': 80}, {'name': 'tanaka', 'score': 30}]
"""


def sortDict(li: List[dict], sort_key: str, order: int = BaseEnum.DESC) -> List[dict]:
    if type(li) is not list:
        raise TypeError("li is invalid type.")
    reverse: bool
    if order is BaseEnum.DESC:
        reverse = True
    elif order is BaseEnum.ASC:
        reverse = False
    sorted_list = sorted(li, key=lambda x: x[sort_key], reverse=reverse)
    return sorted_list
