import unittest

from directory import getFilesPath, dirName
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
        expected_result1: str = "/usr/src/app/README.md"
        expected_result2: str = "/usr/src/app/ut_test.md"
        result = getFilesPath(ut_arg, ut_arg2)
        for index, result in enumerate(getFilesPath(ut_arg, ut_arg2)):
            # type test
            self.assertIs(type(result), str)
            # value test
            if index == 0:
                self.assertEqual(result, expected_result1)
            elif index == 1:
                self.assertEqual(result, expected_result2)

    def test_dirName_case1(self):
        ut_arg: str = "/usr/src/app/ut_test.md"
        ut_arg2: int = 1
        expected_result: str = "usr"
        result = dirName(ut_arg, ut_arg2)
        # type test
        self.assertIs(type(result), str)
        # value test
        self.assertEqual(result, expected_result)

    def test_dirName_case2(self):
        ut_arg: str = "/usr/src/app/ut_test.md"
        ut_arg2: int = 3
        expected_result: str = "app"
        result = dirName(ut_arg, ut_arg2)
        # type test
        self.assertIs(type(result), str)
        # value test
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
