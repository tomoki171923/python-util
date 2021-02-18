import unittest

from split import splitList


class UtExtract(unittest.TestCase):

    def test_splitList(self):
        ut_data: list = [1, 2, 3, 4, 5, 6, 7]
        ut_data2: int = 3
        expected_result1: list = [1, 2, 3]
        expected_result2: list = [4, 5, 6]
        expected_result3: list = [7]
        i = 1
        for result in splitList(ut_data, ut_data2):
            # type test
            self.assertIs(type(result), list)
            # value test
            if i == 1:
                self.assertEqual(expected_result1, result)
            elif i == 2:
                self.assertEqual(expected_result2, result)
            elif i == 3:
                self.assertEqual(expected_result3, result)
            i += 1

    def test_args(self):
        with self.assertRaises(TypeError):
            splitList([1, 2, 3, 4, 5, 6, 7])
        with self.assertRaises(TypeError):
            result = splitList('[1,2,3,4,5,6,7]', '3')
            next(result)


if __name__ == "__main__":
    unittest.main()
