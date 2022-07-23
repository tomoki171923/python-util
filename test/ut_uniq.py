import unittest

from src.pyutil.uniq import uniqDicts


class UtUniq(unittest.TestCase):
    def test_uniqDicts_case1(self):
        ut_arg: list = [
            {"name": "suzuki", "score": 80},
            {"name": "tanaka", "score": 30},
            {"name": "suzuki", "score": 100},
        ]
        ut_arg2: str = "name"
        expected: list = [
            {"name": "suzuki", "score": 80},
            {"name": "tanaka", "score": 30},
        ]
        actual = uniqDicts(ut_arg, ut_arg2)
        # type test
        self.assertIs(type(actual), list)
        # value test
        self.assertEqual(actual, expected)

    def test_args(self):
        pass
