# Use the official Node.js image as the base image
FROM node:20

# Set the working directory
WORKDIR /app

# COPY frontend/package*.json ./
COPY frontend ./

WORKDIR /app/frontend

# Install Node.js dependencies
RUN npm install

# Build the React application
RUN npm run build

# Expose the React app port
EXPOSE 3000

# Start the React app
CMD ["npm", "start"]

# Dockerfile

# pull the official docker image
FROM python:3.8-slim

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY frontend ./

WORKDIR /app/frontend

# install dependencies
COPY backend/requirements.txt /app/backend/requirements.txt
RUN pip install --no-cache-dir -r /app/backend/requirements.txt

# Expose the FastAPI port
EXPOSE 8000

# Start the FastAPI application
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]

