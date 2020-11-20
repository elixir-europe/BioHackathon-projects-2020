FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /code
COPY . /code

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN apt-get update && \
    apt-get install -y vim

RUN python django/manage.py migrate
