import unittest

from extract import extension, currentDirName


class UtExtract(unittest.TestCase):
    def test_extension(self):
        ut_arg: str = "/tmp/sample.json"
        expected: str = "json"
        actual = extension(ut_arg)
        # type test
        self.assertIs(type(actual), str)
        # value test
        self.assertEqual(actual, expected)

    def test_currentDirName(self):
        ut_arg: str = "/tmp/sample.json"
        expected: str = "tmp"
        actual = currentDirName(ut_arg)
        # type test
        self.assertIs(type(actual), str)
        # value test
        self.assertEqual(actual, expected)

    def test_args(self):
        with self.assertRaises(TypeError):
            extension(123)
        with self.assertRaises(TypeError):
            currentDirName(123)


if __name__ == "__main__":
    unittest.main()
