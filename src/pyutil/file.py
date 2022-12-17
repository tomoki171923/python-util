# -*- coding: utf-8 -*-
# the following is not necessary if Python version is 3.9 or over.
from __future__ import annotations
import json
import yaml
import gzip
import io
import ast
from enum import IntEnum, auto
from typing import Generator


class Enum(IntEnum):
    TYPE_STRING = auto()
    TYPE_INT = auto()
    TYPE_LIST = auto()
    TYPE_DICT = auto()


""" Loading a file as yaml format
Args:
    file_path (str): target file path.
Returns:
    dict: file data
"""


def loadYaml(file_path: str) -> dict:
    with open(file=file_path) as file:
        return yaml.safe_load(file)


""" Loading a file as json format
Args:
    file_path (str): target file path.
    return_type (int, optional): the type of return object
         Enum.TYPE_DICT  (defalt): dict
         Enum.TYPE_STRING    2: str
Returns:
    dict or str: file data
"""


def loadJson(file_path: str, return_type: int = Enum.TYPE_DICT) -> dict | str:
    with open(file=file_path) as file:
        json_data = json.load(file)
        if return_type == Enum.TYPE_STRING:
            json_data = json.dumps(json_data, sort_keys=True, indent=2)
        return json_data


""" Loading a streaming data file like the following.
-----
{ 'time': yyyy-MM-ddThh:mm:ss, 'message': 'hogehoge', 'status': 200, ...}
{ 'time': yyyy-MM-ddThh:mm:ss, 'message': 'hogehoge', 'status': 200, ...}
{ 'time': yyyy-MM-ddThh:mm:ss, 'message': 'hogehoge', 'status': 200, ...}
...
-----
Args:
    file_path (str): target file path.
Returns:
    generator: a line data of the file
e.g.
    file_path = 'yyyy-mm-dd-log.gz'
    for line in loadStream(file_path):
        print(line)
"""


def loadStream(file_path: str) -> Generator[str]:
    with open(file=file_path) as file:
        for line in file:
            yield ast.literal_eval(line)


""" Loading file data as gzip format
Args:
    file_data (bytes): target file data.
Returns:
    str: file data
"""


def loadGzipData(file_data: bytes) -> str:
    with gzip.open(filename=io.BytesIO(file_data), mode="rt") as file:
        try:
            return file.read()
        except OSError:
            return False


""" Creating a file as yaml format.
Args:
    file_path (str): target file path.
    data (list|dict): file data
    encoding (str, optional): encoding. the default is utf-8.
"""


def createYaml(file_path: str, data: list | dict, encoding="utf-8") -> None:
    with open(file=file_path, mode="w", encoding=encoding) as file:
        yaml.dump(
            data, file, encoding=encoding, default_flow_style=False, allow_unicode=True
        )


""" Creating a file as json format.
Args:
    file_path (str): target file path.
    data (list|dict): file data
    encoding (str, optional): encoding. the default is utf-8.
"""


def createJson(file_path: str, data: list | dict, encoding="utf-8") -> None:
    with open(file=file_path, mode="w", encoding=encoding) as file:
        json.dump(data, file, ensure_ascii=False)
