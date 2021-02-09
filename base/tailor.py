# -*- coding: utf-8 -*-
import os

''' split a list.
e.g.
    l=[1,2,3,4,5,6,7], m=3 # => [[1, 2, 3], [4, 5, 6], [7]]
Args:
    l (list): the target list.
    n (int): the number to split.
Returns:
    generator: splited lists.
'''


def splitList(l: list, n: int):
    for idx in range(0, len(l), n):
        yield l[idx:idx + n]


''' get an extension of the file.
e.g.
    test/test.json # => json
    sample.csv # => csv
Args:
    file (str): file name or path.
Returns:
    generator: the extension of the file.
'''


def getExtension(file: str):
    return os.path.splitext(file)[1]
