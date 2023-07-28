FROM python:3.11.4-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV POETRY_VERSION=1.5.1

ENV PORT=8000
ENV HOME=eco_challenge

EXPOSE $PORT

RUN apt-get update && apt-get install -y \
    dumb-init --no-install-recommends \
    && pip install "poetry==$POETRY_VERSION"\
    && rm -rf /var/lib/apt/lists/*

WORKDIR $HOME

COPY . .

RUN poetry config virtualenvs.create false \
    && poetry install --without dev

ENTRYPOINT ["/usr/bin/dumb-init", "--"]

CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
