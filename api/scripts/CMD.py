import os
from abc import ABC
from math import *  # Main pint for support math functions


class CMD(ABC):
    """
    The main class for running python scripts dependent from type [ complex or simple ]
    """
    _code: str
    result: str = None

    def __init__(self, code):
        self._code = code

    def execute(self):
        pass

    @property
    def get_code(self):
        return self._code


class ComplexCMD(CMD):
    def execute(self):
        BR_FILE = 'browser_script.py'

        with open(BR_FILE, 'w') as f:
            f.writelines(self._code)

        exec(open(BR_FILE).read())
        self.result = 'Success'


class SimpleCMD(CMD):
    def execute(self):
        self.result = eval(self._code)


class CMDFactory:

    @staticmethod
    def get(cmd, code):
        return ComplexCMD(code) if cmd == 'complex' else SimpleCMD(code)
