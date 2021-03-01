import unittest

from sort import sortDict, ranking
from base_enum import BaseEnum


class UtSort(unittest.TestCase):

    def test_sortDict_case1(self):
        ut_arg: list = [
            {'name': 'suzuki', 'score': 80},
            {'name': 'tanaka', 'score': 30},
            {'name': 'sato', 'score': 100}]
        ut_arg2: str = "score"
        ut_arg3: str = BaseEnum.DESC
        expected_result: list = [
            {'name': 'sato', 'score': 100},
            {'name': 'suzuki', 'score': 80},
            {'name': 'tanaka', 'score': 30}]
        result = sortDict(ut_arg, ut_arg2, ut_arg3)
        # type test
        self.assertIs(type(result), list)
        # value test
        self.assertEqual(expected_result, result)

    def test_sortDict_case2(self):
        ut_arg: list = [
            {'name': 'suzuki', 'score': 80},
            {'name': 'tanaka', 'score': 30},
            {'name': 'sato', 'score': 100}]
        ut_arg2: str = "score"
        ut_arg3: str = BaseEnum.ASC
        expected_result: list = [
            {'name': 'tanaka', 'score': 30},
            {'name': 'suzuki', 'score': 80},
            {'name': 'sato', 'score': 100}]
        result = sortDict(ut_arg, ut_arg2, ut_arg3)
        # type test
        self.assertIs(type(result), list)
        # value test
        self.assertEqual(expected_result, result)

    def test_ranking_case1(self):
        ut_arg: list = [2,5,6,8,1,9,11]
        ut_arg2: int = 15
        expected_result: int = 1
        result = ranking(ut_arg, ut_arg2)
        # type test
        self.assertIs(type(result), int)
        # value test
        self.assertEqual(expected_result, result)

    def test_ranking_case2(self):
        ut_arg: list = [2,5,6,8,1,9,11]
        ut_arg2: int = 0
        expected_result: int = 8
        result = ranking(ut_arg, ut_arg2)
        # type test
        self.assertIs(type(result), int)
        # value test
        self.assertEqual(expected_result, result)

    def test_ranking_case3(self):
        ut_arg: list = [2,5,6,8,1,9,11]
        ut_arg2: int = 5
        expected_result: int = 5
        result = ranking(ut_arg, ut_arg2)
        # type test
        self.assertIs(type(result), int)
        # value test
        self.assertEqual(expected_result, result)

    def test_args(self):
        pass


if __name__ == "__main__":
    unittest.main()
