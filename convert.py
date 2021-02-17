# -*- coding: utf-8 -*-

import ast

''' convert String to List.
Args:
    obj (str): the target obj.
    split_key (str, optional): split key.
Returns:
    list: the target obj.
e.g.1
    obj="1 2 3" # => [1, 2, 3]
e.g.2
    obj="1,2,3", split_key="," # => [1, 2, 3]
'''


def strToList(obj: str, split_key=None):
    if split_key is not None:
        return obj.split(split_key)
    return obj.split()


''' convert String to Dict.
Args:
    obj (str): the target obj.
Returns:
    dict or list: the target obj.
e.g.1
    obj = '{"key1":"value1", "key2":123}'
        # => {'key1': 'value1', 'key2': 123}
e.g.2
    obj = '[1, "aaa", 3]'
        # => [1, 'aaa', 3]
'''


def strToDict(obj: str):
    return ast.literal_eval(obj)
