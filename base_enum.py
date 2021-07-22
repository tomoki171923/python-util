from enum import IntEnum, auto


class BaseEnum(IntEnum):
    ASC = auto()
    DESC = auto()

    TYPE_STRING = auto()
    TYPE_INT = auto()
    TYPE_LIST = auto()
    TYPE_DICT = auto()

    STOP = auto()
    CONTINUE = auto()
