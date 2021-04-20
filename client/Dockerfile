FROM node:15.14.0-alpine3.10
WORKDIR /client
COPY . .
RUN npm install
EXPOSE 8080
CMD ["npm", "run", "serve"]