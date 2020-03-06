FROM node:lts-alpine

# Add nginx and nodejs
RUN apk add --update nginx nodejs

# Create the directories we will need
RUN mkdir -p /var/log/nginx
RUN mkdir -p /var/www/html

COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/default.conf /etc/nginx/conf.d/default.conf

WORKDIR /var/www
COPY ./package.json ./
RUN npm install
RUN npm install @vue/cli@3.7.0 -g
ENV PATH /var/www/node_modules/.bin:$PATH
COPY . .
RUN npm run build

# copy the built app to our served directory
RUN cp -r ./src/* /var/www/html

EXPOSE 8080
CMD ["vue-cli-service", "serve", "--host ${FRONT_HOST}"]
