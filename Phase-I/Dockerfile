FROM python:3.13-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Set working directory
WORKDIR /app

# Copy dependency files
COPY pyproject.toml uv.lock README.md ./

# Install dependencies
# --frozen ensures we stick to the lockfile
# --no-cache keeps the image size down
# --no-install-project installs only dependencies first for caching
RUN uv sync --frozen --no-cache --no-install-project

# Copy source code
COPY src/ src/
COPY README.md .

# Install the project
RUN uv sync --frozen --no-cache

# Add virtual environment to PATH
ENV PATH="/app/.venv/bin:$PATH"

# Run the application
CMD ["todo"]
