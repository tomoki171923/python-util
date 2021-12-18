FROM python:3.8-slim

WORKDIR /usr/src/app

COPY Pipfile* ./

RUN apt-get update \
    && apt-get -y install locales \
    && pip install --upgrade pip \
    && pip install --upgrade setuptools \
    && pip install --upgrade pipenv \
    && pipenv install

COPY . .
