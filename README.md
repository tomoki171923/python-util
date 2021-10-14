# python-util

python 版 utility code を格納.
基本的に他ソースコードから import されること、もしくはただのメモ用として使用している.

This repository has a python utility code. Essentially, they are be imported from other sources.

## how to install

```
pip install git+https://github.com/tomoki171923/python-util
```

## how to use

e.g. sample.py

```
from pyutil.command import execCmd
from pyutil.datetime_jp import today, now

cmd = "ls -l"
execCmd(cmd)

print(today())
print(now())
```

## unit test

```
docker-compose up unittest
```

## pre-commit

```
brew install pre-commit
pre-commit sample-config > .pre-commit-config.yaml
vi .pre-commit-config.yaml
pre-commit install
```
