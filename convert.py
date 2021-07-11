# -*- coding: utf-8 -*-
# the following is not necessary if Python version is 3.9 or over.
from __future__ import annotations

import ast
from decimal import Decimal
import base64
import json
from datetime import datetime, date
from typing import Any


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


''' convert Json Document to Python Object.
the conversion table is to refer to the following.
https://docs.python.org/3/library/json.html#json-to-py-table
Args:
    obj (str): json document.
Returns:
    Any: python object.
e.g.1
    obj = '["foo", {"bar":["baz", null, 1.0, 2]}]'
        # => ['foo', {'bar': ['baz', None, 1.0, 2]}] // <class 'list'>
e.g.2
    obj = '{"bar":["baz", null, 1.0, 2]}'
        # => {'bar': ['baz', None, 1.0, 2]} // <class 'dict'>
'''


def jsonDecoder(obj: bytes | str) -> Any:
    return json.loads(obj)


''' convert Python Object to Json Document.
the conversion table is to refer to the following.
https://docs.python.org/3/library/json.html#py-to-json-table
Args:
    obj (Any): python object.
Returns:
    str: json document.
e.g.1
    obj = ['foo', {'bar': ['baz', None, 1.0, 2]}]
        # => '["foo", {"bar":["baz", null, 1.0, 2]}]'
e.g.2
    obj = {'bar': ['baz', None, 1.0, 2]}
        # => '{"bar":["baz", null, 1.0, 2]}'
'''


def jsonEncoder(obj: Any) -> str:
    return json.dumps(obj, default=__jsonEncoder)


def __jsonEncoder(obj: Any):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError


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


''' Converting string object to datetime object.
Args:
    date_string (str): the time with string object.
    format (str): time format.

Returns:
    datetime: datetime object
'''


def strToDatetime(date_string: str, format: str) -> datetime:
    return datetime.strptime(date_string, format)


''' Converting string object to date object.
Args:
    date_string (str): the date with string object.
    format (str): date format.

Returns:
    datetime.date: date object
'''


def strToDate(date_string: str, format: str) -> date:
    return strToDatetime(date_string, format).date()
