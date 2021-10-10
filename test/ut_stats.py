import unittest

from pyutil.stats import ranking, median


class UtSort(unittest.TestCase):
    def test_ranking_case1(self):
        ut_arg: list = [2, 5, 6, 8, 1, 9, 11]
        ut_arg2: int = 15
        expected: int = 1
        actual = ranking(ut_arg, ut_arg2)
        # type test
        self.assertIs(type(actual), int)
        # value test
        self.assertEqual(actual, expected)

    def test_ranking_case2(self):
        ut_arg: list = [2, 5, 6, 8, 1, 9, 11]
        ut_arg2: int = 0
        expected: int = 8
        actual = ranking(ut_arg, ut_arg2)
        # type test
        self.assertIs(type(actual), int)
        # value test
        self.assertEqual(actual, expected)

    def test_ranking_case3(self):
        ut_arg: list = [2, 5, 6, 8, 1, 9, 11]
        ut_arg2: int = 5
        expected: int = 5
        actual = ranking(ut_arg, ut_arg2)
        # type test
        self.assertIs(type(actual), int)
        # value test
        self.assertEqual(actual, expected)

    def test_median_case1(self):
        ut_arg: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected: int = 5
        actual = median(ut_arg)
        # type test
        self.assertIs(type(actual), int)
        # value test
        self.assertEqual(actual, expected)

    def test_median_case2(self):
        ut_arg: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected: float = 5.5
        actual = median(ut_arg)
        # type test
        self.assertIs(type(actual), float)
        # value test
        self.assertEqual(actual, expected)

    def test_args(self):
        pass


if __name__ == "__main__":
    unittest.main()
