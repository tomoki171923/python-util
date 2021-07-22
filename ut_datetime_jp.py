import unittest

from datetime_jp import (
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
        expected_result: datetime = datetime.now(tz=jst)
        result = now()
        # type test
        self.assertIs(type(result), datetime)
        # value test (allowed an error of 1 second)
        self.assertAlmostEqual(expected_result, result, delta=timedelta(seconds=1))

    def test_today(self):
        jst = pytz.timezone("Asia/Tokyo")
        expected_result: date = (
            datetime.fromtimestamp(time.time(), tz=jst).today().date()
        )
        result = today()
        # type test
        self.assertIs(type(result), date)
        # value test
        self.assertEqual(result, expected_result)

    def test_isPast_case1(self):
        ut_arg: datetime = now() + timedelta(seconds=-1)
        expected_result: bool = True
        result = isPast(ut_arg)
        # type test
        self.assertIs(type(result), bool)
        # value test
        self.assertEqual(result, expected_result)

    def test_isPast_case2(self):
        ut_arg: date = today() + timedelta(days=-1)
        expected_result: bool = True
        result = isPast(ut_arg)
        # type test
        self.assertIs(type(result), bool)
        # value test
        self.assertEqual(result, expected_result)

    def test_isPast_case3(self):
        ut_arg: datetime = now() + timedelta(seconds=1)
        expected_result: bool = False
        result = isPast(ut_arg)
        # type test
        self.assertIs(type(result), bool)
        # value test
        self.assertEqual(result, expected_result)

    def test_isPast_case4(self):
        ut_arg: date = today() + timedelta(days=1)
        expected_result: bool = False
        result = isPast(ut_arg)
        # type test
        self.assertIs(type(result), bool)
        # value test
        self.assertEqual(result, expected_result)

    def test_isFuture_case1(self):
        ut_arg: datetime = now() + timedelta(seconds=1)
        expected_result: bool = True
        result = isFuture(ut_arg)
        # type test
        self.assertIs(type(result), bool)
        # value test
        self.assertEqual(result, expected_result)

    def test_isFuture_case2(self):
        ut_arg: date = today() + timedelta(days=1)
        expected_result: bool = True
        result = isFuture(ut_arg)
        # type test
        self.assertIs(type(result), bool)
        # value test
        self.assertEqual(result, expected_result)

    def test_isFuture_case3(self):
        ut_arg: datetime = now() + timedelta(seconds=-1)
        expected_result: bool = False
        result = isFuture(ut_arg)
        # type test
        self.assertIs(type(result), bool)
        # value test
        self.assertEqual(result, expected_result)

    def test_isFuture_case4(self):
        ut_arg: date = today() + timedelta(days=-1)
        expected_result: bool = False
        result = isFuture(ut_arg)
        # type test
        self.assertIs(type(result), bool)
        # value test
        self.assertEqual(result, expected_result)

    def test_changeTimezone(self):
        hawaii = pytz.timezone("US/Hawaii")
        ut_arg: datetime = now()  # tokyo datetime
        ut_arg2 = hawaii
        expected_result: datetime = datetime.now(tz=hawaii)  # hawaii datetime
        # change timezone to hawaii from tokyo.
        result = changeTimezone(ut_arg, ut_arg2)
        # type test
        self.assertIs(type(result), datetime)
        # value test (allowed an error of 1 second)
        self.assertAlmostEqual(expected_result, result, delta=timedelta(seconds=1))

    def test_futureDate(self):
        ut_arg: date = date(2020, 1, 1)
        ut_arg2: int = 30
        expected_result: date = date(2020, 1, 31)
        result = futureDate(ut_arg, ut_arg2)
        # type test
        self.assertIs(type(result), date)
        # value test
        self.assertEqual(result, expected_result)

    def test_pastDate(self):
        ut_arg: date = date(2020, 1, 1)
        ut_arg2: int = 30
        expected_result: date = date(2019, 12, 2)
        result = pastDate(ut_arg, ut_arg2)
        # type test
        self.assertIs(type(result), date)
        # value test
        self.assertEqual(result, expected_result)

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
