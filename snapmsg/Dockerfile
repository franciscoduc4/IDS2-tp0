# Use the official Python image from the Docker Hub
FROM python:3.10

# Set the working directory in the Docker container to /app
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install pytest and pytest-asyncio for running tests
RUN pip install --no-cache-dir pytest pytest-asyncio

# Copy the entire current directory contents into the container at /app
COPY . .

# Set an environment variable to include the /app directory in Python's module search path
ENV PYTHONPATH=/app

# Initialize the database
RUN python -c "from app.database import init_db; init_db()"

# Define the command to run the application using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
