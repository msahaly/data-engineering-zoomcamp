FROM python:3.13.11-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /code 
ENV PATH="/code/.venv/bin:$PATH"

COPY "pyproject.toml" "uv.lock" ".python-version" ./
RUN uv sync --locked
RUN apt-get update && apt-get install -y wget

COPY ingest_data.py ingest_data.py
COPY ./data/green_tripdata_2025-11.parquet data/green_tripdata_2025-11.parquet
COPY ./data/taxi_zone_lookup.csv data/taxi_zone_lookup.csv

ENTRYPOINT ["python", "ingest_data.py"]