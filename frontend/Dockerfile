# Use the official Node.js image as the base image
FROM node:20

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY frontend/package*.json ./

# Install Node.js dependencies
RUN npm install

# Copy the application code
COPY frontend ./

# Build the React application
RUN npm run build

# Expose the React app port
EXPOSE 3000

# Start the React app
CMD ["npm", "start"]
