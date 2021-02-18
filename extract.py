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
