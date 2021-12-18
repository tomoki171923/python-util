import unittest

from src.pyutil.trim import trimPrefix, trimSuffix


class UtTrim(unittest.TestCase):
    def test_trimPrefix(self):
        ut_arg: str = "prod_2.5.8"
        ut_arg2: str = "_"
        expected: str = "prod"
        actual: str = trimPrefix(ut_arg, ut_arg2)
        # type test
        self.assertIs(type(actual), str)
        # value test
        self.assertEqual(actual, expected)

    def test_trimSuffix(self):
        ut_arg: str = "prod_2.5.8"
        ut_arg2: str = "_"
        expected: str = "2.5.8"
        actual: str = trimSuffix(ut_arg, ut_arg2)
        # type test
        self.assertIs(type(actual), str)
        # value test
        self.assertEqual(actual, expected)
