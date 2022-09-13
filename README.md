# python-util

Python package, which has utility code like files, http-request, convert, datetime, command, trim, round, and so on.

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
from src.pyutil.date_time import DateTime

cmd = "ls -l"
execCmd(cmd)

date_time:DateTime = DateTime()
print(date_time.today())
print(date_time.now())
```

## For Contributor

### Pre-Commit

```bash
brew install pre-commit
pre-commit install
```

### Build

```bash
docker-compose build
```

### Add Python Package

```bash
docker-compose run --rm app pipenv install PACKAGE_NAME
```

### Update Python Packages

```bash
docker-compose run --rm app pipenv update
```

### Unit Test

```bash
docker-compose up app
```
