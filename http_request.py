# -*- coding: utf-8 -*-

import json
import urllib.request
import base64

''' HTTP GET REQUEST
Args:
    url (str): target URL.
    data (dict, optional): post data
    headers (dict, optional): http request header.
Returns:
    bytes: response from this http request.
e.g.1
    from base.http_request import requestGet
    requestGet('https://google.com')
e.g.2 (in case of basic authentication) 
    from base.http_request import requestGet
    url = 'https://example.com/admin'
    user = 'admin'
    password = 'password123'
    headers = getBasicAuthHeader(user, password)
    requestGet(url, headers)
'''


def requestGet(url: str, data=None, headers=None):
    if headers is None and data is None:
        req = urllib.request.Request(url=url, method='GET')
    elif headers is not None and data is None:
        req = urllib.request.Request(url=url, headers=headers, method='GET')
    elif headers is None and data is not None:
        req = urllib.request.Request(
            url=url, data=json.dumps(data).encode(), method='GET')
    else:
        req = urllib.request.Request(
            url=url, headers=headers, mdata=json.dumps(data).encode(), method='GET')
    with urllib.request.urlopen(req) as res:
        return res.read()


''' HTTP POST/PUT REQUEST
Args:
    url (str): target URL.
    data (dict): post data
    headers (dict): http request header.
Returns:
    bytes: response from this http request.
e.g.1
    from base.http_request import requestPost
    url = 'https://example.com/api'
    headers = {
        'Content-Type': 'application/json',
        'x-api-key' : '*******************************'
    }
    data = {
        'postdata' : 123456
    }
    requestPost(url, data, headers)
e.g.2
    from base.http_request import requestPost
    import concurrent.futures as confu
    url = 'https://example.com/api'
    headers = {
        'Content-Type': 'application/json'
    }
    headers.update(getBasicAuthHeader('user', 'password'))
    data = [
        {'postdata' : 123456},
        ...
        {'postdata' : 123456},
    ]
    # "max_workers=None" means "5 * os.cpu_count()"
    with confu.ThreadPoolExecutor(max_workers=None) as executor:
        futures = [executor.submit(requestPost, url=url, data=d, headers=headers) for d in data]
        for future in confu.as_completed(futures):
            future.result()
'''


def requestPost(url: str, data: dict, headers: dict):
    req = urllib.request.Request(url=url, data=json.dumps(
        data).encode(), headers=headers, method='POST')
    with urllib.request.urlopen(req) as res:
        return res.read()

def requestPut(url: str, data: dict, headers: dict):
    req = urllib.request.Request(url=url, data=json.dumps(
        data).encode(), headers=headers, method='PUT')
    with urllib.request.urlopen(req) as res:
        return res.read()


''' get http header of basic authentication from the user and the password in plain text.
Args:
    user (str): user of basic authentication.
    password (str): password of basic authentication.
Returns:
    dict: http header of basic authentication.
e.g.
    caller
        user = 'admin'
        password = 'password123'
        print(getBasicAuthHeader(user,password))
    output
        {'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='}
'''


def makeBasicAuthHeader(user: str, password: str):
    base64_user_pasword = base64.b64encode(
        '{}:{}'.format(user, password).encode('utf-8'))
    return {"Authorization": "Basic " + base64_user_pasword.decode('utf-8')}
