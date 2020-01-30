FROM ubuntu:18.10

LABEL maintainer="Enrique Matta <enrique@matta.dev>"

RUN apt-get update
RUN apt-get install -y python3 python3-dev python3-pip libpq-dev

COPY ./ /app

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 8080

CMD gunicorn server.run:init_app --bind localhost:8080 --worker-class aiohttp.GunicornWebWorker