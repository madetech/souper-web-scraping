# Use the official Node.js image as the base image
FROM node:20

# Set the working directory
WORKDIR /app/frontend

COPY public ./public
COPY src ./src
COPY package*.json ./

# Install Node.js dependencies
# RUN npm install
RUN NODE_ENV=development npm install

# Build the React application
RUN npm run build

# Expose the React app port
EXPOSE 3000

# Start the React app
CMD ["npm", "start"]
