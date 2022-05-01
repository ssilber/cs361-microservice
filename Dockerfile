FROM python:3.10-buster

RUN mkdir -p /microservice
WORKDIR /microservice

COPY pyproject.toml /microservice/pyproject.toml
COPY poetry.lock /microservice/poetry.lock
RUN pip install poetry==1.1.4
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-dev

COPY . /microservice
