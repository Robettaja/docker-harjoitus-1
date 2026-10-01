FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY pyproject.toml uv.lock ./
RUN uv sync --no-dev

COPY main.py .

VOLUME ["serverdata/"]

ENTRYPOINT ["uv", "run", "uvicorn", "main:app","--host","0.0.0.0"]
CMD [ "--port", "8001"]
