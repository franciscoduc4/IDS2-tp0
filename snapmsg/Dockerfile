# Use the official Python image from the Docker Hub
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY . /app

# Install the application dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install additional dependencies for testing
ARG TESTING
RUN if [ "$TESTING" = "true" ]; then \
    pip install --no-cache-dir pytest fastapi[all] sqlalchemy; \
    fi

# Set environment variables for testing
ENV TESTING=${TESTING}
ENV PYTHONPATH=/app

# Default command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
