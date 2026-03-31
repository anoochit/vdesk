FROM python:3.13-slim

WORKDIR /app

# Install uv
RUN pip install uv

# Copy project files and install dependencies
COPY pyproject.toml uv.lock ./
RUN uv sync --system

# Copy the rest of the application
COPY . .

# Expose the port the app runs on
EXPOSE 8080

# Command to run the application
CMD ["uv", "run", "main.py", "--host", "0.0.0.0"]
