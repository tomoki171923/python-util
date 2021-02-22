# the following is not necessary if Python version is 3.9 or over.
from __future__ import annotations

import subprocess
from subprocess import PIPE
import termcolor

UT_LIST: list[str] = [
    'convert',
    'extract',
    'round',
    'split',
    'datetime_jp',
]

# execute all unit test
if __name__ == "__main__":
    for ut in UT_LIST:
        print(f'************ Unit Test {ut}.py ************')
        cmd = f'python ut_{ut}.py'
        result = subprocess.run(
            cmd, shell=True, stdout=PIPE, stderr=PIPE, text=True)
        message = result.stderr
        color: str = 'green'
        if 'FAILED' in message or 'ERROR' in message:
            color = 'red'
        print(termcolor.colored(message, color))
