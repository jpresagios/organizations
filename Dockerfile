FROM python:3.8-slim-buster
RUN mkdir /code
WORKDIR /code
COPY . /code/
WORKDIR /code/requirements
RUN pip install -r production.txt