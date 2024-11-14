FROM node:22-bullseye-slim

WORKDIR /frontend

COPY package*.json /frontend/
RUN npm install

COPY ./ /frontend

EXPOSE 3000

CMD ["npm","start"]