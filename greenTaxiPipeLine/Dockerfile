FROM python:3.13.11-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /code 
ENV PATH="/code/.venv/bin:$PATH"

COPY "pyproject.toml" "uv.lock" ".python-version" ./
RUN uv sync --locked
RUN wget https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet
RUN wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv

COPY ingest_data.py ingest_data.py

ENTRYPOINT ["python", "ingest_data.py"]