import unittest

from src.pyutil.file import createJson, createYaml, loadYaml, loadJson
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

    # destructor of unittest class
    @classmethod
    def tearDownClass(self):
        # delete ut files.
        os.remove(self.json_file)
        os.remove(self.yaml_file)

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
