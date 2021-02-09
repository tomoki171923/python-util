# -*- coding: utf-8 -*-

from decimal import Decimal, ROUND_HALF_UP, ROUND_DOWN

''' round up the number to the nearest integer.
e.g. from 123.456 to 123
e.g. from 123.567 to 124

Args:
    num (Decimal): the target number.
Returns:
    int: the number rounded up to the nearest integer
'''


def roundUp1(num: Decimal):
    if type(num) is not Decimal:
        num = Decimal(num)
    return int(num.quantize(Decimal('1'), rounding=ROUND_HALF_UP))


''' round up the number to the nearest ten.
e.g. from 1234.56 to 1230
e.g. from 1235.67 to 1240

Args:
    num (Decimal): the target number.
Returns:
    int: the number rounded up to the nearest ten
'''


def roundUp10(num: Decimal):
    if type(num) is not Decimal:
        num = Decimal(num)
    return int(num.quantize(Decimal('1E1'), rounding=ROUND_HALF_UP))


''' round down the number to the nearest integer.
e.g. from 123.456 to 123
e.g. from 123.567 to 123

Args:
    num (Decimal): the target number.
Returns:
    int: the number rounded down to the nearest integer
'''


def roundDown1(num: Decimal):
    if type(num) is not Decimal:
        num = Decimal(num)
    return int(num.quantize(Decimal('1'), rounding=ROUND_DOWN))


''' round down the number to the nearest ten.
e.g. from 1234.56 to 1230
e.g. from 1235.67 to 1230

Args:
    num (Decimal): the target number.
Returns:
    int: the number rounded down to the nearest ten
'''


def roundDown10(num: Decimal):
    if type(num) is not Decimal:
        num = Decimal(num)
    return int(num.quantize(Decimal('1E1'), rounding=ROUND_DOWN))
