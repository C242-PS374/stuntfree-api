FROM python:3.12-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt


RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install --no-cache-dir -r requirements.txt

COPY ./app /code/app

CMD ["fastapi", "run", "--port", "8080"]