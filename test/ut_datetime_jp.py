import unittest

from pyutil.datetime_jp import (
    now,
    today,
    isPast,
    isFuture,
    changeTimezone,
    futureDate,
    pastDate,
)
from datetime import datetime, timedelta, date
import time
import pytz

# reference : pytz timezone list
# https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568


class UtDatetimeJp(unittest.TestCase):
    def test_now(self):
        jst = pytz.timezone("Asia/Tokyo")
        expected: datetime = datetime.now(tz=jst)
        actual = now()
        # type test
        self.assertIs(type(actual), datetime)
        # value test (allowed an error of 1 second)
        self.assertAlmostEqual(expected, actual, delta=timedelta(seconds=1))

    def test_today(self):
        jst = pytz.timezone("Asia/Tokyo")
        expected: date = datetime.fromtimestamp(time.time(), tz=jst).date()
        actual = today()
        # type test
        self.assertIs(type(actual), date)
        # value test
        self.assertEqual(actual, expected)

    def test_isPast_case1(self):
        ut_arg: datetime = now() + timedelta(seconds=-1)
        expected: bool = True
        actual = isPast(ut_arg)
        # type test
        self.assertIs(type(actual), bool)
        # value test
        self.assertEqual(actual, expected)

    def test_isPast_case2(self):
        ut_arg: date = today() + timedelta(days=-1)
        expected: bool = True
        actual = isPast(ut_arg)
        # type test
        self.assertIs(type(actual), bool)
        # value test
        self.assertEqual(actual, expected)

    def test_isPast_case3(self):
        ut_arg: datetime = now() + timedelta(seconds=1)
        expected: bool = False
        actual = isPast(ut_arg)
        # type test
        self.assertIs(type(actual), bool)
        # value test
        self.assertEqual(actual, expected)

    def test_isPast_case4(self):
        ut_arg: date = today() + timedelta(days=1)
        expected: bool = False
        actual = isPast(ut_arg)
        # type test
        self.assertIs(type(actual), bool)
        # value test
        self.assertEqual(actual, expected)

    def test_isFuture_case1(self):
        ut_arg: datetime = now() + timedelta(seconds=1)
        expected: bool = True
        actual = isFuture(ut_arg)
        # type test
        self.assertIs(type(actual), bool)
        # value test
        self.assertEqual(actual, expected)

    def test_isFuture_case2(self):
        ut_arg: date = today() + timedelta(days=1)
        expected: bool = True
        actual = isFuture(ut_arg)
        # type test
        self.assertIs(type(actual), bool)
        # value test
        self.assertEqual(actual, expected)

    def test_isFuture_case3(self):
        ut_arg: datetime = now() + timedelta(seconds=-1)
        expected: bool = False
        actual = isFuture(ut_arg)
        # type test
        self.assertIs(type(actual), bool)
        # value test
        self.assertEqual(actual, expected)

    def test_isFuture_case4(self):
        ut_arg: date = today() + timedelta(days=-1)
        expected: bool = False
        actual = isFuture(ut_arg)
        # type test
        self.assertIs(type(actual), bool)
        # value test
        self.assertEqual(actual, expected)

    def test_changeTimezone(self):
        hawaii = pytz.timezone("US/Hawaii")
        ut_arg: datetime = now()  # tokyo datetime
        ut_arg2 = hawaii
        expected: datetime = datetime.now(tz=hawaii)  # hawaii datetime
        # change timezone to hawaii from tokyo.
        actual = changeTimezone(ut_arg, ut_arg2)
        # type test
        self.assertIs(type(actual), datetime)
        # value test (allowed an error of 1 second)
        self.assertAlmostEqual(expected, actual, delta=timedelta(seconds=1))

    def test_futureDate(self):
        ut_arg: date = date(2020, 1, 1)
        ut_arg2: int = 30
        expected: date = date(2020, 1, 31)
        actual = futureDate(ut_arg, ut_arg2)
        # type test
        self.assertIs(type(actual), date)
        # value test
        self.assertEqual(actual, expected)

    def test_pastDate(self):
        ut_arg: date = date(2020, 1, 1)
        ut_arg2: int = 30
        expected: date = date(2019, 12, 2)
        actual = pastDate(ut_arg, ut_arg2)
        # type test
        self.assertIs(type(actual), date)
        # value test
        self.assertEqual(actual, expected)

    def test_args(self):
        with self.assertRaises(TypeError):
            isPast("2021/01/01")
        with self.assertRaises(TypeError):
            isFuture("2021/01/01")
        with self.assertRaises(TypeError):
            changeTimezone(datetime.now())
        with self.assertRaises(TypeError):
            changeTimezone(datetime.now(), "US/Hawaii")


if __name__ == "__main__":
    unittest.main()
