# -*- coding: utf-8 -*-

import ast
import pickle
import base64
import json


''' convert String to Dict.
Args:
    obj (str): the target obj.
Returns:
    dict: the target obj.
e.g.
    obj = '{"key1":"value1", "key2":123}'
        # => {'key1': 'value1', 'key2': 123}
'''


def strToDict(obj: str) -> dict:
    return ast.literal_eval(obj)


''' convert String to Dict.
Args:
    obj (str): the target obj.
Returns:
    list: the target obj.
e.g.
    obj = '[1, "aaa", 3]'
        # => [1, 'aaa', 3]
'''


def strToList(obj: str) -> list:
    return ast.literal_eval(obj)


''' convert String to List by split key.
Args:
    obj (str): the target obj.
    split_key (str, optional): split key.
Returns:
    list: the target obj.
e.g.1
    obj='aa bb cc', split_key=' ' # => ['aa', 'bb', 'cc']
e.g.2
    obj='aa,bb,cc', split_key=',' # => ['aa', 'bb', 'cc']
'''


def strToListByKey(obj: str, split_key: str) -> list:
    return obj.split(split_key)


''' convert Dict to Bytes. (Endode)
Args:
    obj (dict): the target obj.
Returns:
    bytes: the target obj.
e.g.
    obj = {"key1": "value1", "key2": 123, "key3": "https://www.google.com/"}
        # => b'eyJrZXkxIjogInZhbHVlMSIsICJrZXkyIjogMTIzLCAia2V5MyI6ICJodHRwczovL3d3dy5nb29nbGUuY29tLyJ9'
'''


def dictToBytes(obj: dict) -> bytes:
    if type(obj) is not dict:
        raise TypeError('obj is invalid type.')
    return base64.urlsafe_b64encode(json.dumps(obj).encode())


''' convert Bytes to Dict. (Dedode)
Args:
    obj (bytes): the target obj.
Returns:
    dict: the target obj.
e.g.
    obj = b'eyJrZXkxIjogInZhbHVlMSIsICJrZXkyIjogMTIzLCAia2V5MyI6ICJodHRwczovL3d3dy5nb29nbGUuY29tLyJ9'
        # => {"key1": "value1", "key2": 123, "key3": "https://www.google.com/"}
'''


def bytesToDict(obj: bytes) -> dict:
    if type(obj) is not bytes:
        raise TypeError('obj is invalid type.')
    return strToDict(base64.urlsafe_b64decode(obj).decode())
