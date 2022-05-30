FROM python:3.10-slim-buster
RUN apt update && apt install libpq-dev gcc -y
RUN adduser --disabled-login django
COPY ./requirements /requirements
COPY ./compose/local/django/start /start
RUN chmod +x /start
COPY ./compose/local/django/entrypoint /entrypoint
RUN chmod +x /entrypoint
RUN pip install -r /requirements/local.txt
USER django
WORKDIR /app

ENTRYPOINT ["/entrypoint"]