FROM postgres:15-alpine
WORKDIR /app
ENV POSTGRES_PASSWORD ${POSTGRES_PASSWORD}
ENV POSTGRES_USER ${POSTGRES_USER}
ENV POSTGRES_DB ${POSTGRES_DB}

# Copy .env to app root
COPY .env .

# COPY world.sql /docker-entrypoint-initdb.d/

# # Use the official Node.js image as the base image
# FROM node:20

# # Set the working directory
# WORKDIR /app/frontend

# # COPY frontend/package*.json ./
# COPY frontend/ /app/frontend/

# RUN ls /app/frontend
# RUN ls /app/frontend/src

# # Install Node.js dependencies
# RUN npm install

# # # Build the React application
# RUN npm run build --prod

# # Expose the React app port
# EXPOSE 3000

# # Start the React app
# CMD ["npm", "start"]

# Dockerfile

# # pull the official docker image
FROM python:3.8-slim

# # set work directory
# WORKDIR /app

# Set the working directory
WORKDIR /app/backend

COPY backend/ /app/backend/

RUN ls /app/backend

# # set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DATABASE_URL postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@db:5432/${POSTGRES_DB}

# # install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# # Expose the FastAPI port
EXPOSE 8000

# # Start the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

