FROM python:3.10-slim-buster
RUN apt update && apt install libpq-dev gcc -y \
    # Only for development
    && apt install git default-jdk -y
RUN adduser --disabled-login fast
COPY ./requirements /requirements
COPY ./compose/local/fastapi/start /start
RUN chmod +x /start
COPY ./compose/local/fastapi/entrypoint /entrypoint
RUN chmod +x /entrypoint
RUN pip install -r /requirements/local.txt
USER fast
WORKDIR /app