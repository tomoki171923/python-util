# -*- coding: utf-8 -*-
""" How to use and import this class.
e.g.
~~~
import const as cst

class myconst:
    cst.END_POINT_URL_LOCAL = 'http://localhost:8000'
    cst.END_POINT_URL_DOCKER = 'http://host.docker.internal:8000'
    cst.REGION = 'ap-northeast-1'
    ...
~~~
"""


import sys


class _const(object):
    class ConstError(TypeError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError()
        self.__dict__[name] = value


sys.modules[__name__] = _const()
