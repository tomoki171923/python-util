# -*- coding: utf-8 -*-
import json
import yaml

''' Loading a file as yaml format
Args:
    file_path (str): target file path.
Returns:
    dict: file data
'''


def loadYaml(file_path: str):
    with open(file_path) as file:
        return yaml.safe_load(file)


''' Loading a file as json format
Args:
    file_path (str): target file path.
    return_type (int, optional): the type of return object
         1(defalt): dict  
         2: str
Returns:
    dict or str: file data
'''


def loadJson(file_path: str, return_type=1):
    with open(file_path) as file:
        json_data = json.load(file)
        if return_type == 2:
            json_data = json.dumps(json_data, sort_keys=True, indent=2)
        return json_data
