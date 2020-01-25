# Matta.dev

## DB Migrate

Run migrations for database by executing `python migrate.py`.

Make sure you are running `docker-compose up -d` to get postgres up and running. You will also need to make sure you set these environmental variables:

```
- POSTGRES_URL
- POSTGRES_PORT
- POSTGRES_USER
- POSTGRES_PASSWORD
- POSTGRES_DB
```

## CONFIGURATION

This app loads the configs from root under `[environment].toml`. Make sure to set `AIOHTTP_ENV` to either `development`, `testing`, or `production`.

### TOML Structure

```ini
[app]
LOGGER_LEVEL = 10 # https://docs.python.org/3.8/library/logging.html#logging-levels

[database]

POSTGRES_URL = ''
POSTGRES_PORT = 000
POSTGRES_USER = ''
POSTGRES_PASSWORD = ''
POSTGRES_DB = ''

[redis]

REDIS_HOST = ''
REDIS_PORT = 000
```

## Logging Level

We are setting this via the [integer level](https://docs.python.org/3.8/library/logging.html#logging-levels) instead of the constant (read the docs).