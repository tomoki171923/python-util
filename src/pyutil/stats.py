# -*- coding: utf-8 -*-
from typing import List

import statistics

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


""" get the median of numbers.
Args:
    li (list): the numbers list.
Returns:
    float: the median of li.
e.g.1
    score_list = [2,5,6,8,1,9,11], target_score = 15
    # => 1
"""


def median(
    li: List[int],
) -> float:
    return statistics.median(li)
