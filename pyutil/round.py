# -*- coding: utf-8 -*-
# the following is not necessary if Python version is 3.9 or over.
from __future__ import annotations

from decimal import Decimal, ROUND_HALF_UP, ROUND_DOWN

""" round up the number to the nearest integer.
e.g. num = 123.456 # => 123
e.g. num = 123.567 # => 124

Args:
    num (float): the target number.
Returns:
    int: the number rounded up to the nearest integer
"""


def roundUp1(num: float) -> int:
    return int(Decimal(num).quantize(Decimal("1"), rounding=ROUND_HALF_UP))


""" round up the number to the nearest ten.
e.g. num = 1234.56 # => 1230
e.g. num = 1235.67 # => 1240

Args:
    num (int | float): the target number.
Returns:
    int: the number rounded up to the nearest ten
"""


def roundUp10(num: int | float) -> int:
    return int(Decimal(num).quantize(Decimal("1E1"), rounding=ROUND_HALF_UP))


""" round down the number to the nearest integer.
e.g. num = 123.456 # => 123
e.g. num = 123.567 # => 123

Args:
    num (float): the target number.
Returns:
    int: the number rounded down to the nearest integer
"""


def roundDown1(num: float) -> int:
    return int(Decimal(num).quantize(Decimal("1"), rounding=ROUND_DOWN))


""" round down the number to the nearest ten.
e.g. num = 1234.56 # => 1230
e.g. num = 1235.67 # => 1230

Args:
    num (int | float): the target number.
Returns:
    int: the number rounded down to the nearest ten
"""


def roundDown10(num: int | float) -> int:
    return int(Decimal(num).quantize(Decimal("1E1"), rounding=ROUND_DOWN))
