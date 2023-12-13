# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/engine/reference/builder/

ARG NODE_VERSION=21.2.0

################################################################################
# Use node image for base image for all stages.
FROM node:${NODE_VERSION}-alpine as base

# Set working directory for all build stages.
WORKDIR /usr/src/solve-weaver-fe

# Magic from ChatGPT to let recent Node version use old OpenSSL library
ENV NODE_OPTIONS=--openssl-legacy-provider

# Copy the rest of the source files into the image.
COPY src/ /usr/src/solve-weaver-fe/src
COPY public/ /usr/src/solve-weaver-fe/public
COPY package.json /usr/src/solve-weaver-fe/

RUN npm install

# Run the application.
CMD [ "npm", "start" ]
