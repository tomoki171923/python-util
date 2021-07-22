# python-base

各システムで汎用的に使用するPythonのベーシックな機能郡を格納.
基本的に本ソースコードは他からimportされること、もしくはただのメモ用として使用.

This repository has some basic Python functions to be used by a general system.
Basically, they are to be imported from other sources or to be used as just notes.


## unit test

~~~
(local)
docker-compose run --rm py38 bash

(container)
pip install --no-cache-dir -r requirements.txt
python ut_all.py 
~~~

## code format

~~~
find . -type f -name "*.py" | xargs black
~~~

## code lint

~~~
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
~~~