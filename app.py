import os

from aiohttp import web

from mattadev.run import init_app

web.run_app(init_app(), port=os.getenv('APP_API_PORT', 3000))
