import unittest

from src.pyutil.sort import sortDicts, Enum


class UtSort(unittest.TestCase):
    def test_sortDicts_case1(self):
        ut_arg: list = [
            {"name": "suzuki", "score": 80},
            {"name": "tanaka", "score": 30},
            {"name": "sato", "score": 100},
        ]
        ut_arg2: str = "score"
        expected: list = [
            {"name": "sato", "score": 100},
            {"name": "suzuki", "score": 80},
            {"name": "tanaka", "score": 30},
        ]
        actual = sortDicts(ut_arg, ut_arg2)
        # type test
        self.assertIs(type(actual), list)
        # value test
        self.assertEqual(actual, expected)

    def test_sortDicts_case2(self):
        ut_arg: list = [
            {"name": "suzuki", "score": 80},
            {"name": "tanaka", "score": 30},
            {"name": "sato", "score": 100},
        ]
        ut_arg2: str = "score"
        ut_arg3: str = Enum.ASC
        expected: list = [
            {"name": "tanaka", "score": 30},
            {"name": "suzuki", "score": 80},
            {"name": "sato", "score": 100},
        ]
        actual = sortDicts(ut_arg, ut_arg2, ut_arg3)
        # type test
        self.assertIs(type(actual), list)
        # value test
        self.assertEqual(actual, expected)

    def test_args(self):
        pass
