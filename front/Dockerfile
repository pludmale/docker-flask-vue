# build stage
FROM node:lts-alpine as build-stage

# Add nginx and nodejs
RUN apk add --update nginx nodejs

# Create the directories we will need
RUN mkdir -p /var/log/nginx
RUN mkdir -p /var/www/html

COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/default.conf /etc/nginx/conf.d/default.conf

WORKDIR /front
ENV PATH /app/node_modules/.bin:$PATH
#COPY ./package.json ./
RUN npm install
RUN npm install @vue/cli@3.7.0 -g
COPY . .
RUN npm run build

# copy the built app to our served directory
RUN cp -r . /var/www/html

EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]
