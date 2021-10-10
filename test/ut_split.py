import unittest

from pyutil.split import splitList


class UtSplit(unittest.TestCase):
    def test_splitList(self):
        ut_arg: list = [1, 2, 3, 4, 5, 6, 7]
        ut_arg2: int = 3
        expected1: list = [1, 2, 3]
        expected2: list = [4, 5, 6]
        expected3: list = [7]
        i = 1
        for actual in splitList(ut_arg, ut_arg2):
            # type test
            self.assertIs(type(actual), list)
            # value test
            if i == 1:
                self.assertEqual(actual, expected1)
            elif i == 2:
                self.assertEqual(actual, expected2)
            elif i == 3:
                self.assertEqual(actual, expected3)
            i += 1

    def test_args(self):
        with self.assertRaises(TypeError):
            splitList([1, 2, 3, 4, 5, 6, 7])
        with self.assertRaises(TypeError):
            actual = splitList("[1,2,3,4,5,6,7]", "3")
            next(actual)


if __name__ == "__main__":
    unittest.main()
