# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/engine/reference/builder/

ARG NODE_VERSION=21.3.0

################################################################################
# Use node image for base image for all stages.
FROM node:${NODE_VERSION}-alpine as base

# Set working directory for all build stages.
WORKDIR /usr/src/solve-weaver-fe

# Magic from ChatGPT to let recent Node version use old OpenSSL library
ENV NODE_OPTIONS=--openssl-legacy-provider
ENV publicPath /usr/src/solve-weaver-fe/

COPY package.json .
COPY package-lock.json .

RUN npm ci 

RUN npm install

# Copy the rest of the source files into the image.
COPY src src/
COPY public public/

RUN npm run build

EXPOSE 3000

# Run the application.
CMD [ "npm", "start" ]
