import os

from aiohttp import web

from mattadev.run import init_app

if __name__ == "__main__":
    web.run_app(init_app(), port=os.getenv('APP_API_PORT', 3000))
