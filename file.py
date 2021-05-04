# -*- coding: utf-8 -*-
import json
import yaml
import gzip
import ast
from .base_enum import BaseEnum

''' Loading a file as yaml format
Args:
    file_path (str): target file path.
Returns:
    dict: file data
'''


def loadYaml(file_path: str):
    with open(file=file_path) as file:
        return yaml.safe_load(file)


''' Loading a file as json format
Args:
    file_path (str): target file path.
    return_type (int, optional): the type of return object
         BaseEnum.TYPE_DICT  (defalt): dict  
         BaseEnum.TYPE_STRING    2: str
Returns:
    dict or str: file data
'''


def loadJson(file_path: str, return_type: int = BaseEnum.TYPE_DICT):
    with open(file=file_path) as file:
        json_data = json.load(file)
        if return_type == BaseEnum.TYPE_STRING:
            json_data = json.dumps(json_data, sort_keys=True, indent=2)
        return json_data


''' Loading a streming data file like the following.
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
'''


def loadStream(file_path: str):
    with open(file=file_path) as file:
        for line in file:
            yield ast.literal_eval(line)


''' Loading file data as gzip format
Args:
    file_data (bytes): target file data.
Returns:
    str: file data
'''


def loadGzipData(file_data: bytes):
    with gzip.open(filename=io.BytesIO(file_data), mode='rt') as file:
        try:
            return file.read()
        except OSError:
            return False
