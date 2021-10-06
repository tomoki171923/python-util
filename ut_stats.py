import unittest

from stats import ranking


class UtSort(unittest.TestCase):
    def test_ranking_case1(self):
        ut_arg: list = [2, 5, 6, 8, 1, 9, 11]
        ut_arg2: int = 15
        expected_result: int = 1
        result = ranking(ut_arg, ut_arg2)
        # type test
        self.assertIs(type(result), int)
        # value test
        self.assertEqual(result, expected_result)

    def test_ranking_case2(self):
        ut_arg: list = [2, 5, 6, 8, 1, 9, 11]
        ut_arg2: int = 0
        expected_result: int = 8
        result = ranking(ut_arg, ut_arg2)
        # type test
        self.assertIs(type(result), int)
        # value test
        self.assertEqual(result, expected_result)

    def test_ranking_case3(self):
        ut_arg: list = [2, 5, 6, 8, 1, 9, 11]
        ut_arg2: int = 5
        expected_result: int = 5
        result = ranking(ut_arg, ut_arg2)
        # type test
        self.assertIs(type(result), int)
        # value test
        self.assertEqual(result, expected_result)

    def test_args(self):
        pass


if __name__ == "__main__":
    unittest.main()
