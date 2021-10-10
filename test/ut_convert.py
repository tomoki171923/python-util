import unittest

from pyutil.convert import (
    strToDict,
    strToList,
    strToListByKey,
    dictToBytes,
    bytesToDict,
    strToDatetime,
    strToDate,
    jsonDecoder,
    jsonEncoder,
)
from datetime import datetime, date, timedelta, timezone
import json
from decimal import Decimal


class UtConvert(unittest.TestCase):
    def test_strToDict_case1(self):
        ut_arg: str = '{"key1":"value1", "key2":123}'
        expected: dict = {"key1": "value1", "key2": 123}
        actual = strToDict(ut_arg)
        # type test
        self.assertIs(type(actual), dict)
        # value test
        self.assertEqual(actual, expected)

    def test_strToDict_case2(self):
        ut_arg: str = '{"key1":"value1", "key2":123}'
        expected: dict = {"key1": "value1", "key2": "123"}
        actual = strToDict(ut_arg)
        # type test
        self.assertIs(type(actual), dict)
        # value test
        self.assertNotEqual(actual, expected)

    def test_strToList_case1(self):
        ut_arg: str = '[1, "aaa", 3]'
        expected: list = [1, "aaa", 3]
        actual = strToList(ut_arg)
        # type test
        self.assertIs(type(actual), list)
        # value test
        self.assertEqual(actual, expected)

    def test_strToList_case2(self):
        ut_arg: str = '[1, "aaa", 3]'
        expected: list = [1, "aaa", "3"]
        actual = strToList(ut_arg)
        # type test
        self.assertIs(type(actual), list)
        # value test
        self.assertNotEqual(actual, expected)

    def test_strToListByKey_case1(self):
        ut_arg: str = "aa bb cc"
        ut_arg2: str = " "
        expected: list = ["aa", "bb", "cc"]
        actual = strToListByKey(ut_arg, ut_arg2)
        # type test
        self.assertIs(type(actual), list)
        # value test
        self.assertEqual(actual, expected)

    def test_strToListByKey_case2(self):
        ut_arg: str = "aa,bb,cc"
        ut_arg2: str = ","
        expected: list = ["aa", "bb", "cc"]
        actual = strToListByKey(ut_arg, ut_arg2)
        # type test
        self.assertIs(type(actual), list)
        # value test
        self.assertEqual(actual, expected)

    def test_jsonDecoder_case1(self):
        ut_arg: str = '["foo", {"bar":["baz", null, 1.0, 2]}]'
        expected: list = ["foo", {"bar": ["baz", None, 1.0, 2]}]
        actual = jsonDecoder(ut_arg)
        # type test
        self.assertIs(type(actual), list)
        # value test
        self.assertEqual(actual, expected)

    def test_jsonDecoder_case2(self):
        ut_arg: str = '{"bar":["baz", null, 1.0, 2]}'
        expected: dict = {"bar": ["baz", None, 1.0, 2]}
        actual = jsonDecoder(ut_arg)
        # type test
        self.assertIs(type(actual), dict)
        # value test
        self.assertEqual(actual, expected)

    def test_jsonDecoder_case3(self):
        ut_arg: bytes = b'["foo", {"bar":["baz", null, 1.0, 2]}]'
        expected: list = ["foo", {"bar": ["baz", None, 1.0, 2]}]
        actual = jsonDecoder(ut_arg)
        # type test
        self.assertIs(type(actual), list)
        # value test
        self.assertEqual(actual, expected)

    def test_jsonEncoder_case1(self):
        ut_arg: list = ["foo", {"bar": ["baz", None, 1.0, 2]}]
        expected: str = '["foo", {"bar": ["baz", null, 1.0, 2]}]'
        actual = jsonEncoder(ut_arg)
        # type test
        self.assertIs(type(actual), str)
        # value test
        self.assertEqual(actual, expected)

    def test_jsonEncoder_case2(self):
        ut_arg: dict = {"bar": ["baz", None, 1.0, 2]}
        expected: str = '{"bar": ["baz", null, 1.0, 2]}'
        actual = jsonEncoder(ut_arg)
        # type test
        self.assertIs(type(actual), str)
        # value test
        self.assertEqual(actual, expected)

    def test_jsonEncoder_case3(self):
        ut_arg: dict = {"bar": ["baz", None, Decimal(1.0), 2]}
        expected: str = '{"bar": ["baz", null, 1.0, 2]}'
        actual = jsonEncoder(ut_arg)
        # type test
        self.assertIs(type(actual), str)
        # value test
        self.assertEqual(actual, expected)

    def test_jsonEncoder_case4(self):
        ut_arg: dict = {"bar": ["baz", None, "アイウエオ", 2]}
        expected: str = '{"bar": ["baz", null, "アイウエオ", 2]}'
        actual = jsonEncoder(ut_arg)
        # type test
        self.assertIs(type(actual), str)
        # value test
        self.assertEqual(actual, expected)

    def test_dictToBytes(self):
        ut_arg: dict = {
            "key1": "value1",
            "key2": 123,
            "key3": "https://www.google.com/",
        }
        expected: bytes = b"eyJrZXkxIjogInZhbHVlMSIsICJrZXkyIjogMTIzLCAia2V5MyI6ICJodHRwczovL3d3dy5nb29nbGUuY29tLyJ9"
        actual = dictToBytes(ut_arg)
        # type test
        self.assertIs(type(actual), bytes)
        # value test
        self.assertEqual(actual, expected)

    def test_bytesToDict(self):
        ut_arg: bytes = b"eyJrZXkxIjogInZhbHVlMSIsICJrZXkyIjogMTIzLCAia2V5MyI6ICJodHRwczovL3d3dy5nb29nbGUuY29tLyJ9"
        expected: dict = {
            "key1": "value1",
            "key2": 123,
            "key3": "https://www.google.com/",
        }
        actual = bytesToDict(ut_arg)
        # type test
        self.assertIs(type(actual), dict)
        # value test
        self.assertEqual(actual, expected)

    def test_strToDatetime(self):
        ut_arg: str = "2021-01-01 00:00:00.000000+09:00"
        ut_arg2: str = "%Y-%m-%d %H:%M:%S.%f%z"
        expected: datetime = datetime(
            2021,
            1,
            1,
            hour=0,
            minute=0,
            second=0,
            microsecond=0,
            tzinfo=timezone(timedelta(hours=9)),
        )
        actual = strToDatetime(ut_arg, ut_arg2)
        # type test
        self.assertIs(type(actual), datetime)
        # value test
        self.assertEqual(actual, expected)

    def test_strToDate(self):
        ut_arg: str = "2021/01/01"
        ut_arg2: str = "%Y/%m/%d"
        expected: date = date(2021, 1, 1)
        actual = strToDate(ut_arg, ut_arg2)
        # type test
        self.assertIs(type(actual), date)
        # value test
        self.assertEqual(actual, expected)

    def test_args(self):
        with self.assertRaises(ValueError):
            strToDict(123)
        with self.assertRaises(ValueError):
            strToList(123)
        with self.assertRaises(TypeError):
            strToListByKey(123)
        with self.assertRaises(AttributeError):
            strToListByKey(123, 1)
        with self.assertRaises(TypeError):
            dictToBytes([1, 2, 3])
        with self.assertRaises(json.decoder.JSONDecodeError):
            jsonDecoder("{'hoge':'hoge'}")
        with self.assertRaises(TypeError):
            jsonEncoder({"hoge": 123}, 2)
        with self.assertRaises(TypeError):
            bytesToDict(
                "eyJrZXkxIjogInZhbHVlMSIsICJrZXkyIjogMTIzLCAia2V5MyI6ICJodHRwczovL3d3dy5nb29nbGUuY29tLyJ9"
            )
        with self.assertRaises(TypeError):
            strToDatetime("2021-01-01 00:00:00.000000+09:00")
        with self.assertRaises(TypeError):
            strToDatetime("2021-01-01 00:00:00.000000+09:00", 123)
        with self.assertRaises(TypeError):
            strToDate("2021-1-1")
        with self.assertRaises(TypeError):
            strToDate("2021-1-1", 123)
