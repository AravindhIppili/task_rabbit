FROM python:3.10-slim

WORKDIR /backend

RUN pip install poetry

COPY pyproject.toml poetry.lock /backend/

RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-dev

COPY ./app /backend/app

EXPOSE 8000

CMD ["fastapi", "run", "app/main.py", "--port", "8000"]
