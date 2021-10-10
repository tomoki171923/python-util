# the following is not necessary if Python version is 3.9 or over.
from __future__ import annotations

import command

UT_LIST: list[str] = [
    "convert",
    "datetime_jp",
    "directory",
    "extract",
    "round",
    "sort",
    "split",
    "stats",
]

# execute all unit test
if __name__ == "__main__":
    for ut in UT_LIST:
        print(f"**************** Unit Test {ut}.py ****************")
        cmd = f"python ut_{ut}.py"
        command.execCmd(cmd)
