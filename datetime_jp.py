# -*- coding: utf-8 -*-
# the following is not necessary if Python version is 3.9 or over.
from __future__ import annotations

from datetime import datetime, timedelta, timezone, date


''' Get the current time in Japanese timezone.
Returns:
    datetime: the current time 
'''


def now() -> datetime:
    JST = timezone(timedelta(hours=+9), 'JST')
    return datetime.now(tz=JST)


''' Get today in Japanese timezone.
Returns:
    datetime.date: today
'''


def today() -> date:
    return now().date()


''' Checking whether the date is past or not
Args:
    date (datetime.datetime | datetime.date): date for comparison.
Returns:
    bool: True / False
'''


def isPast(d: datetime | date) -> bool:
    if isinstance(d, datetime):
        return d <= now()
    elif isinstance(d, date):
        return d <= today()
    else:
        raise TypeError('d is invalid type.')


''' Checking whether the date is future or not
Args:
    date (datetime.datetime | datetime.date): date for comparison.
Returns:
    bool: True / False
'''


def isFuture(d: datetime | date) -> bool:
    if isinstance(d, datetime):
        return now() <= d
    elif isinstance(d, date):
        return today() <= d
    else:
        raise TypeError('d is invalid type.')


''' Change timezone.
Args:
    dt (datetime): datetime object.
    tz (timezone): the timezone to change.
Returns:
    datetime.datetime: datetime object
'''


def changeTimezone(dt: datetime, tz: timezone) -> datetime:
    return dt.astimezone(tz)
