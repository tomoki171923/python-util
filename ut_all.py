# the following is not necessary if Python version is 3.9 or over.
from __future__ import annotations

import subprocess
from subprocess import PIPE
import termcolor
import sys

UT_LIST: list[str] = [
    "convert",
    "datetime_jp",
    "extract",
    "round",
    "sort",
    "split",
]

# execute all unit test
if __name__ == "__main__":
    for ut in UT_LIST:
        print(f"************ Unit Test {ut}.py ************")
        cmd = f"python ut_{ut}.py"
        result = subprocess.run(cmd, shell=True, stdout=PIPE, stderr=PIPE, text=True)
        message = result.stderr
        error_keyword = ("FAILED", "ERROR", "Error")
        if any(x in message for x in error_keyword):
            # failed
            print(termcolor.colored(message, "red"))
            sys.exit(1)
        else:
            # ok
            print(termcolor.colored(message, "green"))
