FROM node:18-alpine

WORKDIR /app

# Copy package files
COPY package.json package-lock.json* ./

# Install dependencies
RUN npm install

# Copy the rest of the application
COPY . .

# Expose the port the app runs on
EXPOSE 4321

# The --host flag is required to expose the server on the network
CMD ["npm", "run", "dev", "--", "--host"]
