# -*- coding: utf-8 -*-
# the following is not necessary if Python version is 3.9 or over.
from __future__ import annotations

import subprocess
from subprocess import PIPE
import termcolor
import sys
import traceback
import inspect

from enum import IntEnum, auto

class Enum(IntEnum):
    STOP = auto()
    CONTINUE = auto()


""" execute a command.
Args:
    cmd (str): the command executing.
    output (bool): whether this command outputs or not
    error_option (int, optional): the option when an error happens.
        STOP(defalt): stop the processing.
        CONTINUE: continue the processing.
Returns:
    subprocess.CompletedProcess: the result of executing command.
"""


def execCmd(
    cmd: str, output: bool = True, error_option=Enum.STOP
) -> subprocess.CompletedProcess:
    try:
        if output is True:
            print(f" **************** {cmd} **************** ")
        result = subprocess.run(cmd, shell=True, stdout=PIPE, stderr=PIPE, text=True)
        if result.returncode == 0:
            # command succeeded
            if output is True:
                __output(result, "green")
            return result
        else:
            # command failed
            if error_option == Enum.STOP:
                # stop
                if output is True:
                    __output(result, "red")
                raise Exception("ERROR happened. Stop this process.")
            elif error_option == Enum.CONTINUE:
                # continue
                if output is True:
                    __output(result, "yellow")
                return result
    except Exception as e:
        print(termcolor.colored(f"{e}", "red"))
        for stack in inspect.stack():
            print(
                termcolor.colored(
                    f"{stack.filename},{stack.function},{stack.lineno}", "red"
                )
            )
        print(termcolor.colored(f"Stacktrace : {traceback.format_exc()}", "red"))
        sys.exit()


def __output(result: subprocess.CompletedProcess, color: str) -> None:
    print(termcolor.colored(result.returncode, color))
    print(termcolor.colored(result.stdout, color))
    print(termcolor.colored(result.stderr, color))
