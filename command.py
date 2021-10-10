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
            print(f"**************** [exec command] {cmd} ****************")
        result = subprocess.run(cmd, shell=True, stdout=PIPE, stderr=PIPE, text=True)
        kwargs = __makeKwargs(result, error_option)
        if output is True:
            __output(**kwargs)
        if not result.returncode == 0 and error_option == Enum.STOP:
            raise Exception("ERROR happened. Stop this process.")
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


def __makeKwargs(result: subprocess.CompletedProcess, error_option: int) -> dict:
    kwargs: dict = dict()
    kwargs["result"] = result
    if result.returncode == 0:
        kwargs["color"] = "green"
    else:
        # command failed
        if error_option == Enum.STOP:
            kwargs["color"] = "red"
        elif error_option == Enum.CONTINUE:
            kwargs["color"] = "yellow"
    return kwargs


def __output(result: subprocess.CompletedProcess, color: str) -> None:
    print(termcolor.colored(result.returncode, color))
    print(termcolor.colored(result.stdout, color))
    print(termcolor.colored(result.stderr, color))
