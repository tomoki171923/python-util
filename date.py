# -*- coding: utf-8 -*-

from datetime import datetime, timedelta, timezone
import time

''' Get the current time in Japanese timezone.
Returns:
    datetime: the current time 
'''


def now():
    JST = timezone(timedelta(hours=+9), 'JST')
    return datetime.fromtimestamp(time.time(), JST)


''' Get today in Japanese timezone.
Returns:
    datetime.date: today
'''


def today():
    return now().date()


''' Checking whether the date is future or not
Args:
    date (datetime.date): date for comparison.
Returns:
    bool: True / False
'''


def isFuture(date: datetime.date):
    return today() <= date


''' Add days to date object.
Args:
    datetime.date (str): date object.
    number (int): the number of days to add.
Returns:
    datetime.date: date object
'''


def addDays(date: datetime.date, number: int):
    return date + timedelta(days=number)


''' Subtract days to date object.
Args:
    datetime.date (str): date object.
    number (int): the number of days to subtract.
Returns:
    datetime.date: date object
'''


def subtractDays(date: datetime.date, number: int):
    return date + timedelta(days=-number)
