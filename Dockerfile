FROM python:3.12-slim

WORKDIR /usr/src/app

# Install system dependencies required for build
RUN apt-get update && apt-get install -y --no-install-recommends \
    binutils \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry

# Copy application code to the container
COPY . .

# Install dependencies using Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Build application executable
RUN poetry run pyinstaller --onefile main/jitter.py