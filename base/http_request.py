# -*- coding: utf-8 -*-

import json
import urllib.request
import base64


''' HTTP GET REQUEST
Args:
    url (str): target URL.
Returns:
    bytes: response from this http request.
e.g.
    requestGet('https://google.com')
e.g. (in case of basic authentication) 
    url = 'https://example.com/admin'
    user = 'admin'
    password = 'password123'
    headers = getBasicAuthHeader(user, password)
    requestGet(url, headers)
'''
def requestGet(url: str, headers=None):
    if headers==None:
        req = urllib.request.Request(url=url)
    else:
        req = urllib.request.Request(url=url, headers=headers)
    with urllib.request.urlopen(req) as res:
        response = res.read()
    return response


''' HTTP POST REQUEST
Args:
    url (str): target URL.
Returns:
    bytes: response from this http request.
e.g.
    url = 'https://example.com/api'
    headers = {
        'Content-Type': 'application/json',
        'x-api-key' : '*******************************'
    }
    data = {
        'postdata' : 123456
    }
    requestPost(url, data, headers)
'''
def requestPost(url: str, data: dict, headers: dict):
    req = urllib.request.Request(url=url, data=json.dumps(data).encode(), headers=headers)
    with urllib.request.urlopen(req) as res:
        response = res.read()
    return response


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
def getBasicAuthHeader(user: str, password: str):
    base64_user_pasword = base64.b64encode('{}:{}'.format(user, password).encode('utf-8'))
    return {"Authorization": "Basic " + base64_user_pasword.decode('utf-8')}
