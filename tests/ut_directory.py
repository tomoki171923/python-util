import unittest

from src.pyutil.directory import getFilesPath, dirName
import os


class UtDirectory(unittest.TestCase):
    # constructor of unittest class
    @classmethod
    def setUpClass(self):
        # create an ut file on local.
        f = open("./ut_test.md", "w")
        f.write("this is unit test.")
        f.close()

    # destructor of unittest class
    @classmethod
    def tearDownClass(self):
        # delete ut files on local.
        os.remove("./ut_test.md")

    def test_getFilesPath(self):
        ut_arg: str = "./"
        ut_arg2: str = ".md"
        expected1: str = "/usr/src/app/README.md"
        expected2: str = "/usr/src/app/ut_test.md"
        actual = getFilesPath(ut_arg, ut_arg2)
        for index, actual in enumerate(getFilesPath(ut_arg, ut_arg2)):
            # type test
            self.assertIs(type(actual), str)
            # value test
            if index == 0:
                self.assertEqual(actual, expected1)
            elif index == 1:
                self.assertEqual(actual, expected2)

    def test_dirName_case1(self):
        ut_arg: str = "/usr/src/app/ut_test.md"
        ut_arg2: int = 1
        expected: str = "usr"
        actual = dirName(ut_arg, ut_arg2)
        # type test
        self.assertIs(type(actual), str)
        # value test
        self.assertEqual(actual, expected)

    def test_dirName_case2(self):
        ut_arg: str = "/usr/src/app/ut_test.md"
        ut_arg2: int = 3
        expected: str = "app"
        actual = dirName(ut_arg, ut_arg2)
        # type test
        self.assertIs(type(actual), str)
        # value test
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
