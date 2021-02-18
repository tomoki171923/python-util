import unittest

from convert import strToDict, strToList, strToListByKey, dictToBytes, bytesToDict, strToDatetime, strToDate
from datetime import datetime, date, timedelta, timezone


class UtConvert(unittest.TestCase):

    def test_strToDict_case1(self):
        ut_arg: str = '{"key1":"value1", "key2":123}'
        expected_result: dict = {
            "key1": "value1",
            "key2": 123
        }
        result = strToDict(ut_arg)
        # type test
        self.assertIs(type(result), dict)
        # value test
        self.assertEqual(expected_result, result)

    def test_strToDict_case2(self):
        ut_arg: str = '{"key1":"value1", "key2":123}'
        expected_result: dict = {
            "key1": "value1",
            "key2": "123"
        }
        result = strToDict(ut_arg)
        # type test
        self.assertIs(type(result), dict)
        # value test
        self.assertNotEqual(expected_result, result)

    def test_strToList_case1(self):
        ut_arg: str = '[1, "aaa", 3]'
        expected_result: list = [1, 'aaa', 3]
        result = strToList(ut_arg)
        # type test
        self.assertIs(type(result), list)
        # value test
        self.assertEqual(expected_result, result)

    def test_strToList_case2(self):
        ut_arg: str = '[1, "aaa", 3]'
        expected_result: list = [1, 'aaa', '3']
        result = strToList(ut_arg)
        # type test
        self.assertIs(type(result), list)
        # value test
        self.assertNotEqual(expected_result, result)

    def test_strToListByKey_case1(self):
        ut_arg: str = 'aa bb cc'
        ut_arg2: str = ' '
        expected_result: list = ['aa', 'bb', 'cc']
        result = strToListByKey(ut_arg, ut_arg2)
        # type test
        self.assertIs(type(result), list)
        # value test
        self.assertEqual(expected_result, result)

    def test_strToListByKey_case2(self):
        ut_arg: str = 'aa,bb,cc'
        ut_arg2: str = ','
        expected_result: list = ['aa', 'bb', 'cc']
        result = strToListByKey(ut_arg, ut_arg2)
        # type test
        self.assertIs(type(result), list)
        # value test
        self.assertEqual(expected_result, result)

    def test_dictToBytes(self):
        ut_arg: dict = {
            "key1": "value1",
            "key2": 123,
            "key3": "https://www.google.com/"
        }
        expected_result: bytes = b'eyJrZXkxIjogInZhbHVlMSIsICJrZXkyIjogMTIzLCAia2V5MyI6ICJodHRwczovL3d3dy5nb29nbGUuY29tLyJ9'
        result = dictToBytes(ut_arg)
        # type test
        self.assertIs(type(result), bytes)
        # value test
        self.assertEqual(expected_result, result)

    def test_bytesToDict(self):
        ut_arg: bytes = b'eyJrZXkxIjogInZhbHVlMSIsICJrZXkyIjogMTIzLCAia2V5MyI6ICJodHRwczovL3d3dy5nb29nbGUuY29tLyJ9'
        expected_result: dict = {
            "key1": "value1",
            "key2": 123,
            "key3": "https://www.google.com/"
        }
        result = bytesToDict(ut_arg)
        # type test
        self.assertIs(type(result), dict)
        # value test
        self.assertEqual(expected_result, result)

    def test_strToDatetime(self):
        ut_arg: str = '2021-01-01 00:00:00.000000+09:00'
        ut_arg2: str = '%Y-%m-%d %H:%M:%S.%f%z'
        expected_result: datetime = datetime(2021, 1, 1, hour=0, minute=0, second=0, microsecond=0, tzinfo=timezone(timedelta(hours=9)))
        result = strToDatetime(ut_arg, ut_arg2)
        # type test
        self.assertIs(type(result), datetime)
        # value test
        self.assertEqual(expected_result, result)

    def test_strToDate(self):
        ut_arg: str = '2021/01/01'
        ut_arg2: str = '%Y/%m/%d'
        expected_result: date = date(2021, 1, 1)
        result = strToDate(ut_arg, ut_arg2)
        # type test
        self.assertIs(type(result), date)
        # value test
        self.assertEqual(expected_result, result)

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
        with self.assertRaises(TypeError):
            bytesToDict(
                'eyJrZXkxIjogInZhbHVlMSIsICJrZXkyIjogMTIzLCAia2V5MyI6ICJodHRwczovL3d3dy5nb29nbGUuY29tLyJ9')
        with self.assertRaises(TypeError):
            strToDatetime('2021-01-01 00:00:00.000000+09:00')
        with self.assertRaises(TypeError):
            strToDatetime('2021-01-01 00:00:00.000000+09:00', 123)
        with self.assertRaises(TypeError):
            strToDate('2021-1-1')
        with self.assertRaises(TypeError):
            strToDate('2021-1-1', 123)


if __name__ == "__main__":
    unittest.main()
    
