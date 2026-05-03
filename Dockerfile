FROM python:3.12.7-bookworm

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y curl wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python -

ENV PATH="/root/.local/bin:$PATH"

RUN poetry install

CMD ["tail", "-f", "/dev/null"]