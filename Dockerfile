FROM python:3.12.4-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY pyproject.toml /app

RUN pip install --upgrade pip
RUN pip install uv

RUN uv pip install .

COPY . /app/