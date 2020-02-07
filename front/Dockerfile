# build stage
FROM node:lts-alpine as build-stage
WORKDIR /front
ENV PATH /app/node_modules/.bin:$PATH
#COPY ./package.json ./
RUN npm install
RUN npm install @vue/cli@3.7.0 -g
COPY . .
RUN npm run build

# production stage
FROM nginx:stable-alpine as production-stage
#COPY --from=build-stage /front/dist /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/nginx.conf /etc/nginx/conf.d
EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]
