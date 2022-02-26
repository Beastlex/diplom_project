FROM node:alpine

WORKDIR /app
USER node

COPY --chown=node:node package.json .
RUN npm install
COPY --chown=node:node . .

CMD ["npm", "start"]