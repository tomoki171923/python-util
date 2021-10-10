# python-util

python 版 utility code を格納.
基本的に他ソースコードから import されること、もしくはただのメモ用として使用している.

This repository has a python utility code. Essentially, they are be imported from other sources.

## unit test

```
(local)
docker-compose run --rm py38 bash

(container)
pip install --no-cache-dir -r requirements.txt
python ut_all.py
```

## code format

```
find . -type f -name "*.py" | xargs black
```

## code lint

```
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
```

## pre-commit

```
brew install pre-commit
pre-commit sample-config > .pre-commit-config.yaml
vi .pre-commit-config.yaml
pre-commit install
```
