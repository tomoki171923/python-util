import unittest

from round import roundUp1, roundUp10, roundDown1, roundDown10
import decimal


class UtCalculation(unittest.TestCase):
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
        expected_result: int = 123
        result = roundUp1(ut_arg)
        # type test
        self.assertIs(type(result), int)
        # value test
        self.assertEqual(expected_result, result)

    def test_roundUp1_case2(self):
        ut_arg: float = 123.567
        expected_result: int = 124
        result = roundUp1(ut_arg)
        # type test
        self.assertIs(type(result), int)
        # value test
        self.assertEqual(expected_result, result)

    def test_roundUp10_case1(self):
        ut_arg: float = 1234.56
        expected_result: int = 1230
        result = roundUp10(ut_arg)
        # type test
        self.assertIs(type(result), int)
        # value test
        self.assertEqual(expected_result, result)

    def test_roundUp10_case2(self):
        ut_arg: float = 1235.67
        expected_result: int = 1240
        result = roundUp10(ut_arg)
        # type test
        self.assertIs(type(result), int)
        # value test
        self.assertEqual(expected_result, result)

    def test_roundDown1_case1(self):
        ut_arg: float = 123.456
        expected_result: int = 123
        result = roundDown1(ut_arg)
        # type test
        self.assertIs(type(result), int)
        # value test
        self.assertEqual(expected_result, result)

    def test_roundDown1_case2(self):
        ut_arg: float = 123.567
        expected_result: int = 123
        result = roundDown1(ut_arg)
        # type test
        self.assertIs(type(result), int)
        # value test
        self.assertEqual(expected_result, result)

    def test_roundDown10_case1(self):
        ut_arg: float = 1234.56
        expected_result: int = 1230
        result = roundDown10(ut_arg)
        # type test
        self.assertIs(type(result), int)
        # value test
        self.assertEqual(expected_result, result)

    def test_roundDown10_case2(self):
        ut_arg: float = 1235.67
        expected_result: int = 1230
        result = roundDown10(ut_arg)
        # type test
        self.assertIs(type(result), int)
        # value test
        self.assertEqual(expected_result, result)

    def test_args(self):
        with self.assertRaises(decimal.InvalidOperation):
            roundUp1('string')
        with self.assertRaises(decimal.InvalidOperation):
            roundUp10('string')
        with self.assertRaises(decimal.InvalidOperation):
            roundDown1('string')
        with self.assertRaises(decimal.InvalidOperation):
            roundDown10('string')


if __name__ == "__main__":
    unittest.main()
