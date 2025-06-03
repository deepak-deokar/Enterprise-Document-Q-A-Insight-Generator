# frontend/Dockerfile

# Build stage
FROM node:18-alpine AS build

WORKDIR /app

# Install deps
COPY package.json package-lock.json* ./
RUN npm install

# Copy app
COPY . .

# Build React app
RUN npm run build

# Production nginx stage
FROM nginx:stable-alpine

# Copy built React app to nginx
COPY --from=build /app/dist /usr/share/nginx/html

# Expose frontend port
EXPOSE 80

# Nginx will serve by default