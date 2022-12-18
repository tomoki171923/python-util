import unittest

from src.pyutil.file import (
    createJson,
    createYaml,
    loadYaml,
    loadJson,
    loadGzip,
    createGzip,
)
from src.pyutil.convert import (
    jsonEncoder,
    jsonlEncoder,
    strToBytes,
    bytesToStr,
    strToDict,
)
import os


class UtFile(unittest.TestCase):
    # constructor of unittest class
    @classmethod
    def setUpClass(self):
        # testdata
        self.json_file: str = "./test/ut_file.json"
        self.json_data: dict = {"type": "json", "contents": ["hoge", "あいう"]}
        self.yaml_file: str = "./test/ut_file.yaml"
        self.yaml_data: dict = {"type": "json", "contents": ["hoge", "あいう"]}
        self.gzip_file: str = "./test/ut_file_case1.json.gz"
        self.gzip_data: dict = {"type": "json", "contents": ["hoge", "あいう"]}
        self.gzip_file2: str = "./test/ut_file_case2.json.gz"
        self.gzip_data2: list = [
            {"message": "foo", "number": 123},
            {"message": "bar", "number": 234},
            {"message": "baz", "number": 567},
        ]

    # destructor of unittest class
    @classmethod
    def tearDownClass(self):
        # delete ut files.
        os.remove(self.json_file)
        os.remove(self.yaml_file)
        os.remove(self.gzip_file)
        os.remove(self.gzip_file2)

    def test_createJson_loadJson(self):
        ut_arg: str = self.json_file
        ut_arg2: dict = self.json_data
        expected: dict = self.json_data
        createJson(ut_arg, ut_arg2)
        actual: dict = loadJson(ut_arg)
        # type test
        self.assertIs(type(actual), dict)
        # value test
        self.assertEqual(actual, expected)

    def test_createYaml_loadYaml(self):
        ut_arg: str = self.yaml_file
        ut_arg2: dict = self.yaml_data
        expected: dict = self.yaml_data
        createYaml(ut_arg, ut_arg2)
        actual: dict = loadYaml(ut_arg)
        # type test
        self.assertIs(type(actual), dict)
        # value test
        self.assertEqual(actual, expected)

    def test_createGzip_loadGzip_case1(self):
        ut_arg: str = self.gzip_file
        ut_arg2: bytes = strToBytes(jsonEncoder(self.gzip_data))
        expected: dict = self.gzip_data
        createGzip(ut_arg, ut_arg2)
        actual: dict = strToDict(bytesToStr(loadGzip(ut_arg)))
        # type test
        self.assertIs(type(actual), dict)
        # value test
        self.assertEqual(actual, expected)

    def test_createGzip_loadGzip_case2(self):
        ut_arg: str = self.gzip_file2
        ut_arg2: bytes = strToBytes(jsonlEncoder(self.gzip_data2))
        expected: str = """{"message": "foo", "number": 123}
{"message": "bar", "number": 234}
{"message": "baz", "number": 567}
"""
        createGzip(ut_arg, ut_arg2)
        actual: str = bytesToStr(loadGzip(ut_arg))
        # type test
        self.assertIs(type(actual), str)
        # value test
        self.assertEqual(actual, expected)
