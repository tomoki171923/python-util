# -*- coding: utf-8 -*-
# the following is not necessary if Python version is 3.9 or over.
from __future__ import annotations

import pathlib
from typing import Generator


''' get path list of files.
Args:
    dir_path (str): target directory path.
    extension (str, optional): file extension.
Returns:
    generator: file path.
e.g.
    dir_path = '/home'
    extension = '.txt'
        # => ['/home/foo.txt', '/home/hoge.txt'] // <class 'generator'>
'''
def getFilesPath(dir_path: str, extension: str = None) -> Generator[str, None, None]:
    path_obj: pathlib.PosixPath = pathlib.Path(dir_path)
    if extension is not None:
        return path_obj.glob(f'**/*.{extension}')
    else:
        for p in path_obj.glob('**/*'):
            if p.is_file():
                yield str(p)

