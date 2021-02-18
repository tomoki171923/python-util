import unittest

from extract import extension


class UtExtract(unittest.TestCase):

    def test_extension(self):
        ut_arg: str = '/tmp/sample.json'
        expected_result: str = 'json'
        result = extension(ut_arg)
        # type test
        self.assertIs(type(result), str)
        # value test
        self.assertEqual(expected_result, result)

    def test_args(self):
        with self.assertRaises(TypeError):
            extension(123)


if __name__ == "__main__":
    unittest.main()
