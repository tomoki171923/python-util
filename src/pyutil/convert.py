# -*- coding: utf-8 -*-
# the following is not necessary if Python version is 3.9 or over.
from __future__ import annotations

import ast
from decimal import Decimal
import base64
import json
import gzip
import io
from datetime import datetime, date
from typing import Any


""" convert String to Bytes.
Args:
    obj (str): the target obj.
Returns:
    bytes: the target obj.
e.g. strToBytes
    obj = '{"key1":"value1", "key2":123}'
        # => b'{"key1":"value1", "key2":123}'
e.g. strToBase64
    obj = '{"key1":"value1", "key2":123}'
        # =>b'eyJrZXkxIjoidmFsdWUxIiwgImtleTIiOjEyM30='
"""


def strToBytes(obj: str, encoding="utf-8") -> bytes:
    return bytes(obj, encoding=encoding)


def strToBase64(obj: str, encoding="utf-8") -> bytes:
    return base64.urlsafe_b64encode(obj.encode(encoding=encoding))


""" convert String to Dict.
Args:
    obj (str): the target obj.
Returns:
    dict: the target obj.
e.g.
    obj = '{"key1":"value1", "key2":123}'
        # => {'key1': 'value1', 'key2': 123}
"""


def strToDict(obj: str) -> dict:
    return ast.literal_eval(obj)


""" convert String to Dict.
Args:
    obj (str): the target obj.
Returns:
    list: the target obj.
e.g.
    obj = '[1, "aaa", 3]'
        # => [1, 'aaa', 3]
"""


def strToList(obj: str) -> list:
    return ast.literal_eval(obj)


""" convert String to List by split key.
Args:
    obj (str): the target obj.
    split_key (str, optional): split key.
Returns:
    list: the target obj.
e.g.1
    obj='aa bb cc', split_key=' ' # => ['aa', 'bb', 'cc']
e.g.2
    obj='aa,bb,cc', split_key=',' # => ['aa', 'bb', 'cc']
"""


def strToListByKey(obj: str, split_key: str) -> list:
    return obj.split(split_key)


""" Converting string object to datetime object.
Args:
    date_string (str): the time with string object.
    format (str): time format.

Returns:
    datetime: datetime object
"""


def strToDatetime(date_string: str, format: str) -> datetime:
    return datetime.strptime(date_string, format)


""" Converting string object to date object.
Args:
    date_string (str): the date with string object.
    format (str): date format.

Returns:
    datetime.date: date object
"""


def strToDate(date_string: str, format: str) -> date:
    return strToDatetime(date_string, format).date()


""" convert Json Document to Python Object.
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
"""


def jsonDecoder(obj: bytes | str) -> Any:
    return json.loads(obj)


""" convert Python Object to Json Document.
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
"""


def jsonEncoder(obj: Any) -> str:
    return json.dumps(obj, ensure_ascii=False, default=__jsonEncoder)


def __jsonEncoder(obj: Any):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError


""" convert Python Object to Json Line Document.
Args:
    obj (Any): python object.
Returns:
    str: json line document.
e.g.
    obj = [{"message": "foo", "number": 123}, {"message": "bar", "number": 234}, {"message": "baz", "number": 567}]
        # =>
{"message": "foo", "number": 123}
{"message": "bar", "number": 234}
{"message": "baz", "number": 567}
"""


def jsonlEncoder(obj: Any) -> str:
    jsonl: str = ""
    for entry in obj:
        jsonl += jsonEncoder(entry)
        jsonl += "\n"
    return jsonl


""" convert Python Object to Json Line Document.
Args:
    obj (Any): python object.
    json_type (str, optional): json document type. "line": json line document, "document": normal json format. the default is lines.
    encoding (str, optional): encoding. the default is utf-8.
Returns:
    io.BytesIO: BytesIO object.
e.g.
    obj = [{"message": "foo", "number": 123}, {"message": "bar", "number": 234}, {"message": "baz", "number": 567}]
        # => <_io.BytesIO object at 0x7fe65abcce00>
"""


def jsonGzEncoder(obj: Any, json_type="lines", encoding="utf-8") -> io.BytesIO:
    if json_type == "lines":
        contents: str = jsonlEncoder(obj)
    elif json_type == "document":
        contents: str = jsonEncoder(obj)
    else:
        raise TypeError("json_type is invalid type.")
    bio: io.BytesIO = io.BytesIO()
    with gzip.GzipFile(fileobj=bio, mode="wb") as fh:
        with io.TextIOWrapper(fh, encoding=encoding) as wrapper:
            wrapper.write(contents)
    bio.seek(0)
    return bio


""" convert Dict to Bytes. (Encode)
Args:
    obj (dict): the target obj.
Returns:
    bytes: the target obj.
e.g.
    obj = {"key1": "value1", "key2": 123, "key3": "https://www.google.com/"}
        # => b'eyJrZXkxIjogInZhbHVlMSIsICJrZXkyIjogMTIzLCAia2V5MyI6ICJodHRwczovL3d3dy5nb29nbGUuY29tLyJ9'
"""


def dictToBytes(obj: dict) -> bytes:
    if type(obj) is not dict:
        raise TypeError("obj is invalid type.")
    return strToBase64(jsonEncoder(obj))


""" convert Bytes to Dict. (Decode)
Args:
    obj (bytes): the target obj.
Returns:
    dict: the target obj.
e.g.
    obj = b'eyJrZXkxIjogInZhbHVlMSIsICJrZXkyIjogMTIzLCAia2V5MyI6ICJodHRwczovL3d3dy5nb29nbGUuY29tLyJ9'
        # => {"key1": "value1", "key2": 123, "key3": "https://www.google.com/"}
"""


def bytesToDict(obj: bytes) -> dict:
    if type(obj) is not bytes:
        raise TypeError("obj is invalid type.")
    return strToDict(base64ToStr(obj))


""" convert Bytes to String.
Args:
    obj (bytes): the target obj.
Returns:
    str: the target obj.
e.g. bytesToStr
    obj = b'{"key1":"value1", "key2":123}'
        # => '{"key1":"value1", "key2":123}'
e.g. strToBase64
    obj = b'eyJrZXkxIjoidmFsdWUxIiwgImtleTIiOjEyM30='
        # => '{"key1":"value1", "key2":123}'
"""


def bytesToStr(obj: bytes, encoding="utf-8") -> str:
    return obj.decode(encoding)


def base64ToStr(obj: bytes, encoding="utf-8") -> str:
    return base64.urlsafe_b64decode(obj).decode(encoding=encoding)
