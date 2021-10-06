import unittest

from sort import sortDict
from base_enum import BaseEnum


class UtSort(unittest.TestCase):
    def test_sortDict_case1(self):
        ut_arg: list = [
            {"name": "suzuki", "score": 80},
            {"name": "tanaka", "score": 30},
            {"name": "sato", "score": 100},
        ]
        ut_arg2: str = "score"
        expected_result: list = [
            {"name": "sato", "score": 100},
            {"name": "suzuki", "score": 80},
            {"name": "tanaka", "score": 30},
        ]
        result = sortDict(ut_arg, ut_arg2)
        # type test
        self.assertIs(type(result), list)
        # value test
        self.assertEqual(result, expected_result)

    def test_sortDict_case2(self):
        ut_arg: list = [
            {"name": "suzuki", "score": 80},
            {"name": "tanaka", "score": 30},
            {"name": "sato", "score": 100},
        ]
        ut_arg2: str = "score"
        ut_arg3: str = BaseEnum.ASC
        expected_result: list = [
            {"name": "tanaka", "score": 30},
            {"name": "suzuki", "score": 80},
            {"name": "sato", "score": 100},
        ]
        result = sortDict(ut_arg, ut_arg2, ut_arg3)
        # type test
        self.assertIs(type(result), list)
        # value test
        self.assertEqual(result, expected_result)

    def test_args(self):
        pass


if __name__ == "__main__":
    unittest.main()
