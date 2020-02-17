FROM python:3.8.1-buster

LABEL maintainer="Enrique Matta <enrique@matta.dev>"

RUN apt-get update
RUN apt-get install -y libpq-dev

COPY ./ /app

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 8080