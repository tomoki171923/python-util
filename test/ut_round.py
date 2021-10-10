import unittest

from pyutil.round import roundUp1, roundUp10, roundDown1, roundDown10
import decimal


class UtRound(unittest.TestCase):
    # constructor of unittest class
    @classmethod
    def setUpClass(self):
        pass

    # destructor of unittest class
    @classmethod
    def tearDownClass(self):
        pass

    # the action before each of tests is executed in unittest
    def setUp(self):
        pass

    # the action after each of tests is executed in unittest
    def tearDown(self):
        pass

    def test_roundUp1_case1(self):
        ut_arg: float = 123.456
        expected: int = 123
        actual = roundUp1(ut_arg)
        # type test
        self.assertIs(type(actual), int)
        # value test
        self.assertEqual(actual, expected)

    def test_roundUp1_case2(self):
        ut_arg: float = 123.567
        expected: int = 124
        actual = roundUp1(ut_arg)
        # type test
        self.assertIs(type(actual), int)
        # value test
        self.assertEqual(actual, expected)

    def test_roundUp10_case1(self):
        ut_arg: float = 1234.56
        expected: int = 1230
        actual = roundUp10(ut_arg)
        # type test
        self.assertIs(type(actual), int)
        # value test
        self.assertEqual(actual, expected)

    def test_roundUp10_case2(self):
        ut_arg: float = 1235.67
        expected: int = 1240
        actual = roundUp10(ut_arg)
        # type test
        self.assertIs(type(actual), int)
        # value test
        self.assertEqual(actual, expected)

    def test_roundUp10_case3(self):
        ut_arg: int = 1234
        expected: int = 1230
        actual = roundUp10(ut_arg)
        # type test
        self.assertIs(type(actual), int)
        # value test
        self.assertEqual(actual, expected)

    def test_roundUp10_case4(self):
        ut_arg: int = 1235
        expected: int = 1240
        actual = roundUp10(ut_arg)
        # type test
        self.assertIs(type(actual), int)
        # value test
        self.assertEqual(actual, expected)

    def test_roundDown1_case1(self):
        ut_arg: float = 123.456
        expected: int = 123
        actual = roundDown1(ut_arg)
        # type test
        self.assertIs(type(actual), int)
        # value test
        self.assertEqual(actual, expected)

    def test_roundDown1_case2(self):
        ut_arg: float = 123.567
        expected: int = 123
        actual = roundDown1(ut_arg)
        # type test
        self.assertIs(type(actual), int)
        # value test
        self.assertEqual(actual, expected)

    def test_roundDown10_case1(self):
        ut_arg: float = 1234.56
        expected: int = 1230
        actual = roundDown10(ut_arg)
        # type test
        self.assertIs(type(actual), int)
        # value test
        self.assertEqual(actual, expected)

    def test_roundDown10_case2(self):
        ut_arg: float = 1235.67
        expected: int = 1230
        actual = roundDown10(ut_arg)
        # type test
        self.assertIs(type(actual), int)
        # value test
        self.assertEqual(actual, expected)

    def test_roundDown10_case3(self):
        ut_arg: int = 1234
        expected: int = 1230
        actual = roundDown10(ut_arg)
        # type test
        self.assertIs(type(actual), int)
        # value test
        self.assertEqual(actual, expected)

    def test_roundDown10_case4(self):
        ut_arg: int = 1235
        expected: int = 1230
        actual = roundDown10(ut_arg)
        # type test
        self.assertIs(type(actual), int)
        # value test
        self.assertEqual(actual, expected)

    def test_args(self):
        with self.assertRaises(decimal.InvalidOperation):
            roundUp1("string")
        with self.assertRaises(decimal.InvalidOperation):
            roundUp10("string")
        with self.assertRaises(decimal.InvalidOperation):
            roundDown1("string")
        with self.assertRaises(decimal.InvalidOperation):
            roundDown10("string")


if __name__ == "__main__":
    unittest.main()
