FROM python:3.8-slim

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN apt-get update \
    && apt-get -y install locales \
    && pip install --upgrade pip \
    && pip install --upgrade setuptools \
    && pip install --no-cache-dir -r requirements.txt

COPY . .
