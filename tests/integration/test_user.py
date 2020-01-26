import pytest
from api.routes.user import routes as user_routes
from aiohttp import web

async def test_user_name(aiohttp_client, loop):
    app = web.Application()
    app.add_routes(user_routes)
    client = await aiohttp_client(app)
    resp = await client.get('/users/Enrique')
    assert resp.status == 200
    text = await resp.json()
    data = {"success": True, "user": "Enrique"}
    assert data == text
