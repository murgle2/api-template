FROM python:3.9.5-slim-buster

RUN apt-get update && apt-get install -y curl

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY ./pyproject.toml ./poetry.lock* /app/

COPY ./app /app

RUN python -m pip install --upgrade pip

RUN pip install psycopg2-binary

RUN cd app && poetry install --no-root

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
