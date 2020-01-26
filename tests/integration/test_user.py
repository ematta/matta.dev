import os
import pytest
from api.database.engine import init_db_pool
from api.routes.user import routes as user_routes
from api.utilities.config import config
from aiohttp import web

async def test_user_name(aiohttp_client, loop):
    app = web.Application()
    app["config"] = config
    await init_db_pool(app)
    app.add_routes(user_routes)
    client = await aiohttp_client(app)
    payload = {"email": "admin@matta.dev", "password": os.environ['ADMIN_PASSWORD']}
    async with client.post('/user/login', data=payload) as resp:
        assert resp.status == 200
        real_data = await resp.json()
        check_data = {
            'id': 1,
            'name': 'root',
            'email': 'admin@matta.dev',
            'role_id': 1,
            'approved': True
        }
        assert real_data['user'] == check_data
        assert len(real_data['token']) > 0
