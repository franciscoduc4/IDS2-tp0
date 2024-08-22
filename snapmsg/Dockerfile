# Dockerfile

FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENV PYTHONPATH=/app

# Crear las tablas en la base de datos
RUN python -c "from app.database import init_db; init_db()"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
