# -*- coding: utf-8 -*-
from typing import Generator
from .base_enum import BaseEnum

''' sort a list contains dict objects.

Args:
    l (list): the target list.
    n (int): the number to split.
Returns:
    list: sorted list.
e.g.
    from base_enum import BaseEnum
    l = [{'name': 'suzuki', 'score': 80}, {'name': 'tanaka', 'score': 30}, {'name': 'sato', 'score': 100}],
    sort_key="score",
    order = BaseEnum.DESC

    # => [{'name': 'sato', 'score': 100}, {'name': 'suzuki', 'score': 80}, {'name': 'tanaka', 'score': 30}]
'''


def sortDict(l: list, sort_key: str, order: int) -> list:
    if type(l) is not list:
        raise TypeError('l is invalid type.')
    reverse: bool
    if order is BaseEnum.DESC:
        reverse = True
    elif order is BaseEnum.ASC:
        reverse = False
    sorted_list = sorted(l, key=lambda x: x[sort_key], reverse=reverse)
    return sorted_list



def ranking_simple_search(scorelist:list, target:int) -> int:
    scorelist.sort(reverse=True)
    rank:int = 1
    for score in scorelist:
        if score <= target:
            return rank
        rank += 1


def ranking_binary_search(scorelist:list, target_score:int) -> int:
    # sort the score list.
    scorelist.sort(reverse=True)
    length:int = len(scorelist)
    # the element of the highest score on the scorelist
    high:int = 0
    # the element of the lowest score on the scorelist
    low:int = length - 1
    mid:int
    mid_score:int
    # using binary search algorithm.
    while high <= low:
        # get middle score
        mid = (high + low) // 2
        mid_score = scorelist[mid]
        if mid_score == target_score:
            # find target score.
            return mid +1
        elif mid_score > target_score:
            high = mid + 1
        else:
            low = mid - 1
    if target_score< scorelist[length-1]:
        return length + 1
    return mid + 1 
