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
    date: today
'''
def today():
    return now().date()


''' Checking whether the date is future or not
Args:
    date (date): date for comparison.
Returns:
    bool: True / False
'''
def isFuture(date: datetime.date):
    return today() <= date


''' Converting string object to date object.
Args:
    date (str): the date with string object.
    format (str, optional): date format.

Returns:
    date: date object
'''
def toDate(date: str, format='%Y/%m/%d'):
    return datetime.strptime(date, format).date()
