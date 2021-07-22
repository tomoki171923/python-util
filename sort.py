# -*- coding: utf-8 -*-
from typing import Generator
from .base_enum import BaseEnum  # "." is required on AWS Lambda Layer.
from typing import List

""" sort a list contains dict objects.
Args:
    l (list): the target list.
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


def sortDict(l: List[dict], sort_key: str, order: int = BaseEnum.DESC) -> List[dict]:
    if type(l) is not list:
        raise TypeError("l is invalid type.")
    reverse: bool
    if order is BaseEnum.DESC:
        reverse = True
    elif order is BaseEnum.ASC:
        reverse = False
    sorted_list = sorted(l, key=lambda x: x[sort_key], reverse=reverse)
    return sorted_list


""" get ranking of target score using binary search algorithm.
Args:
    score_list (list): the score list.
    target_score (int): the target score.
Returns:
    int: the rank of target score in score list.
e.g.1
    score_list = [2,5,6,8,1,9,11], target_score = 15
    # => 1
e.g.2
    score_list = [2,5,6,8,1,9,11], target_score = 5
    # => 5
e.g.3
    score_list = [2,5,6,8,1,9,11], target_score = 0
    # => 8
"""


def ranking(score_list: List[int], target_score: int) -> int:
    # sort the score list.
    score_list.sort(reverse=True)
    length: int = len(score_list)
    # the element of the highest score on the scorelist
    high: int = 0
    # the element of the lowest score on the scorelist
    low: int = length - 1
    mid: int
    mid_score: int
    # using binary search algorithm.
    while high <= low:
        # get middle score
        mid = (high + low) // 2
        mid_score = score_list[mid]
        if mid_score == target_score:
            # find target score.
            return mid + 1
        elif mid_score > target_score:
            high = mid + 1
        else:
            low = mid - 1
    if target_score < score_list[length - 1]:
        return length + 1
    return mid + 1
