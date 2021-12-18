# python-util

Python package, which has utility code like files, http-request, convert, datetime, command, and so on.

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
