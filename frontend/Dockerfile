# Use the official Node.js image as the base image
FROM node:latest

# Set the working directory
WORKDIR /app/frontend

COPY public ./public
COPY src ./src
COPY package.json ./

RUN mkdir -p ./build
RUN mkdir -p ./node_modules

# Install Node.js dependencies
# RUN npm install

RUN npm cache clean --force
RUN npm cache verify

RUN NODE_ENV=development npm install

# Build the React application
RUN npm run build

# Expose the React app port
EXPOSE 3000

# Start the React app
CMD ["npm", "start"]
