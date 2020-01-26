import os
import pytest
from server.database.postgres import init_pg_pool
from server.routes.user import routes as user_routes
from server.utilities.config import config
from aiohttp import web

async def test_user_name(aiohttp_client, loop):
    app = web.Application()
    app["config"] = config
    await init_pg_pool(app)
    app.add_routes(user_routes)
    client = await aiohttp_client(app)
    payload = {"email": "admin@matta.dev", "password": os.environ['ADMIN_PASSWORD']}
    headers = { 'Content-Type': 'application/json' }
    async with client.post('/user/login', json=payload, headers=headers) as resp:
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
