FROM python:3.10-slim-buster
RUN useradd django
COPY ./requirements /requirements
RUN pip install -r /requirements/local.txt
USER django
WORKDIR /app