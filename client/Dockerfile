# Nodejs image
FROM node:15.14.0-alpine3.10

# Path on container
WORKDIR /client

# Install packages for npm
COPY package.json .
COPY package-lock.json .

# It was noted that this npm version should be used instead
RUN npm install -g npm@7.10.0
# Installing from the package.json
RUN npm install

# Exposing the port 8080 to the rest of the swarm
EXPOSE 8080
COPY . .

# Run the client app
CMD ["npm", "run", "serve"]