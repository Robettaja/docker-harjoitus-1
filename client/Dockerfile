FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY pyproject.toml uv.lock ./
RUN uv sync --no-dev

COPY main.py .

ENTRYPOINT ["sh", "-c", "uv run main.py \"$1\"", "--"]
