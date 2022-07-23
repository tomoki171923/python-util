# -*- coding: utf-8 -*-
from typing import List


""" remove duplicate dict with specified key.
Args:
    li (list): the target list.
    key (str): the specified key.
Returns:
    list: unique list.
e.g.
    li = [{'name': 'suzuki', 'score': 80}, {'name': 'tanaka', 'score': 30}, {'name': 'suzuki', 'score': 100}],
    key="name"
    # => [{'name': 'suzuki', 'score': 80}, {'name': 'tanaka', 'score': 30}]
"""


def uniqDicts(li: List[dict], key: str) -> List[dict]:
    key_list: list = [e[key] for e in li]
    uniq_list: list = [e for i, e in enumerate(li) if e[key] not in key_list[0:i]]
    return uniq_list
