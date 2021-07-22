import unittest

from extract import extension, currentDirName


class UtExtract(unittest.TestCase):
    def test_extension(self):
        ut_arg: str = "/tmp/sample.json"
        expected_result: str = "json"
        result = extension(ut_arg)
        # type test
        self.assertIs(type(result), str)
        # value test
        self.assertEqual(expected_result, result)

    def test_currentDirName(self):
        ut_arg: str = "/tmp/sample.json"
        expected_result: str = "tmp"
        result = currentDirName(ut_arg)
        # type test
        self.assertIs(type(result), str)
        # value test
        self.assertEqual(expected_result, result)

    def test_args(self):
        with self.assertRaises(TypeError):
            extension(123)
        with self.assertRaises(TypeError):
            currentDirName(123)


if __name__ == "__main__":
    unittest.main()
