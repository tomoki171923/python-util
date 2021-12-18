# -*- coding: utf-8 -*-

""" trim prefix / suffix.
Args:
    string (str): the string object.
    search_key (str): the keyword to trim.
Returns:
    str: trimmed string.
e.g.
    trimPrefix
        striing = "prod_2.5.8"
        search_key = "_"
            # => "prod"
    trimSuffix
        striing = "prod_2.5.8"
        search_key = "_"
            # => "2.5.8"
"""


def trimPrefix(string: str, search_key: str) -> str:
    pos: int = string.rfind(search_key)
    return string[:pos]


def trimSuffix(string: str, search_key: str) -> str:
    pos: int = string.rfind(search_key)
    return string[pos + 1 :]
