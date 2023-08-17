# Dockerfile

# pull the official docker image
FROM python:3.10-slim

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Install Python dependencies
COPY backend/requirements.txt /app/backend/requirements.txt
RUN pip install --no-cache-dir -r backend/requirements.txt

# Copy the application code
COPY backend /app/backend

# Expose the FastAPI port
EXPOSE 8000

# Start the FastAPI application
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
