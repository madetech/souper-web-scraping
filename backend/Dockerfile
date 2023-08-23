# Dockerfile

# pull the official docker image
FROM python:3.10-slim

WORKDIR /app/backend

COPY . .

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DATABASE_URL postgresql://eu-west-2:551085516078@arn:aws/secretsmanager

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the FastAPI port
EXPOSE 8000

# Start the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
