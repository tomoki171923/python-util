# -*- coding: utf-8 -*-
import unittest

from src.pyutil.date_time import DateTime
from datetime import datetime, timezone, timedelta, date
import time
import pytz

# reference : pytz timezone list
# https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568


class UtDateTime(unittest.TestCase):
    # constructor of unittest class
    @classmethod
    def setUpClass(self):
        self.date_time = DateTime()

    # destructor of unittest class
    @classmethod
    def tearDownClass(self):
        del self.date_time

    # the action before each of tests is executed in unittest
    def setUp(self):
        pass

    # the action after each of tests is executed in unittest
    def tearDown(self):
        pass

    def test_now(self):
        jst = pytz.timezone("Asia/Tokyo")
        expected: datetime = datetime.now(tz=jst)
        actual = self.date_time.now()
        # type test
        self.assertIs(type(actual), datetime)
        # value test (allowed an error of 1 second)
        self.assertAlmostEqual(expected, actual, delta=timedelta(seconds=1))

    def test_set_timezone(self):
        date_time_hst = DateTime()
        date_time_hst.setTimezone(-10, "HST")
        hst = pytz.timezone("US/Hawaii")
        expected: datetime = datetime.now(tz=hst)
        actual = date_time_hst.now()
        actual2 = date_time_hst.getTimezone()
        # type test
        self.assertIs(type(actual), datetime)
        self.assertIs(type(actual2), timezone)
        # value test (allowed an error of 1 second)
        self.assertAlmostEqual(expected, actual, delta=timedelta(seconds=1))

    def test_today(self):
        jst = pytz.timezone("Asia/Tokyo")
        expected: date = datetime.fromtimestamp(time.time(), tz=jst).date()
        actual = self.date_time.today()
        # type test
        self.assertIs(type(actual), date)
        # value test
        self.assertEqual(actual, expected)

    def test_isPast_case1(self):
        ut_arg: datetime = self.date_time.now() + timedelta(seconds=-1)
        expected: bool = True
        actual = self.date_time.isPast(ut_arg)
        # type test
        self.assertIs(type(actual), bool)
        # value test
        self.assertEqual(actual, expected)

    def test_isPast_case2(self):
        ut_arg: date = self.date_time.today() + timedelta(days=-1)
        expected: bool = True
        actual = self.date_time.isPast(ut_arg)
        # type test
        self.assertIs(type(actual), bool)
        # value test
        self.assertEqual(actual, expected)

    def test_isPast_case3(self):
        ut_arg: datetime = self.date_time.now() + timedelta(seconds=1)
        expected: bool = False
        actual = self.date_time.isPast(ut_arg)
        # type test
        self.assertIs(type(actual), bool)
        # value test
        self.assertEqual(actual, expected)

    def test_isPast_case4(self):
        ut_arg: date = self.date_time.today() + timedelta(days=1)
        expected: bool = False
        actual = self.date_time.isPast(ut_arg)
        # type test
        self.assertIs(type(actual), bool)
        # value test
        self.assertEqual(actual, expected)

    def test_isFuture_case1(self):
        ut_arg: datetime = self.date_time.now() + timedelta(seconds=1)
        expected: bool = True
        actual = self.date_time.isFuture(ut_arg)
        # type test
        self.assertIs(type(actual), bool)
        # value test
        self.assertEqual(actual, expected)

    def test_isFuture_case2(self):
        ut_arg: date = self.date_time.today() + timedelta(days=1)
        expected: bool = True
        actual = self.date_time.isFuture(ut_arg)
        # type test
        self.assertIs(type(actual), bool)
        # value test
        self.assertEqual(actual, expected)

    def test_isFuture_case3(self):
        ut_arg: datetime = self.date_time.now() + timedelta(seconds=-1)
        expected: bool = False
        actual = self.date_time.isFuture(ut_arg)
        # type test
        self.assertIs(type(actual), bool)
        # value test
        self.assertEqual(actual, expected)

    def test_isFuture_case4(self):
        ut_arg: date = self.date_time.today() + timedelta(days=-1)
        expected: bool = False
        actual = self.date_time.isFuture(ut_arg)
        # type test
        self.assertIs(type(actual), bool)
        # value test
        self.assertEqual(actual, expected)

    def test_changeTimezone(self):
        hawaii = pytz.timezone("US/Hawaii")
        ut_arg: datetime = self.date_time.now()  # tokyo datetime
        ut_arg2 = hawaii
        expected: datetime = datetime.now(tz=hawaii)  # hawaii datetime
        # change timezone to hawaii from tokyo.
        actual = self.date_time.changeTimezone(ut_arg, ut_arg2)
        # type test
        self.assertIs(type(actual), datetime)
        # value test (allowed an error of 1 second)
        self.assertAlmostEqual(expected, actual, delta=timedelta(seconds=1))

    def test_futureDate_case1(self):
        ut_arg: date = date(2020, 1, 1)
        ut_arg2: int = 30
        expected: date = date(2020, 1, 31)
        actual = self.date_time.futureDate(ut_arg, ut_arg2)
        # type test
        self.assertIs(type(actual), date)
        # value test
        self.assertEqual(actual, expected)

    def test_futureDate_case2(self):
        ut_arg: date = date(2020, 1, 1)
        ut_arg2: int = 1
        expected: date = date(2020, 2, 1)
        actual = self.date_time.futureDate(ut_arg, months=ut_arg2)
        # type test
        self.assertIs(type(actual), date)
        # value test
        self.assertEqual(actual, expected)

    def test_futureDate_case3(self):
        ut_arg: date = date(2020, 1, 1)
        expected = None
        actual = self.date_time.futureDate(ut_arg)
        # value test
        self.assertEqual(actual, expected)

    def test_pastDate_case1(self):
        ut_arg: date = date(2020, 1, 1)
        ut_arg2: int = 30
        expected: date = date(2019, 12, 2)
        actual = self.date_time.pastDate(ut_arg, ut_arg2)
        # type test
        self.assertIs(type(actual), date)
        # value test
        self.assertEqual(actual, expected)

    def test_pastDate_case2(self):
        ut_arg: date = date(2020, 1, 1)
        ut_arg2: int = 1
        expected: date = date(2019, 12, 1)
        actual = self.date_time.pastDate(ut_arg, months=ut_arg2)
        # type test
        self.assertIs(type(actual), date)
        # value test
        self.assertEqual(actual, expected)

    def test_pastDate_case3(self):
        ut_arg: date = date(2020, 1, 1)
        expected = None
        actual = self.date_time.futureDate(ut_arg)
        # value test
        self.assertEqual(actual, expected)

    def test_args(self):
        with self.assertRaises(TypeError):
            self.date_time.isPast("2021/01/01")
        with self.assertRaises(TypeError):
            self.date_time.isFuture("2021/01/01")
        with self.assertRaises(TypeError):
            self.date_time.changeTimezone(datetime.now())
        with self.assertRaises(TypeError):
            self.date_time.changeTimezone(datetime.now(), "US/Hawaii")
