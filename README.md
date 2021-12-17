# python-util

python 版 utility code を格納.
基本的に他ソースコードから import されること、もしくはただのメモ用として使用している.

This repository has a python utility code. Essentially, they are be imported from other sources.

## For User

### Install

```bash
pip install git+https://github.com/tomoki171923/python-util#egg=pyutil
```

OR

Pipfile

```python
[packages]
pyutil = {git = "https://github.com/tomoki171923/python-util.git", editable = true, ref = "main"}
```

OR

requirements.txt

```python
pyutil @ git+https://github.com/tomoki171923/python-util@main
```

### Usage

e.g. sample.py

```python
from pyutil.command import execCmd
from pyutil.datetime_jp import today, now

cmd = "ls -l"
execCmd(cmd)

print(today())
print(now())
```

## For Contributor

### Pre-Commit

```bash
brew install pre-commit
pre-commit install
```

### Unit Test

```bash
docker-compose up app
```

### Add Package

```bash
docker-compose run --rm app pipenv install PACKAGE_NAME
```
