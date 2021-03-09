# -*- coding: utf-8 -*-
import os


''' extract an extension from the file path.
e.g.
    test/test.json # => json
    sample.csv # => csv
Args:
    file_path (str): file name or path.
Returns:
    str: the extension of the file.
'''


def extension(file_path: str) -> str:
    return os.path.splitext(file_path)[1][1:]


''' extract the name of directory which contains target file from file path.
e.g.
    parent/child/test.json # => child
Args:
    file_path (str): file path.
Returns:
    str: the name of directory which contains target file.
'''
def currentDirName(file_path: str) -> str:
    return os.path.basename(os.path.dirname(file_path))


''' extract the name of file from file path.
e.g.
    parent/child/test.json # => test.json
Args:
    file_path (str): file path.
Returns:
    str: the name of file.
'''
def fileName(file_path: str) -> str:
    return os.path.basename(file_path)



