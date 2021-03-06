from setuptools import setup


install_requires = [
    'aiodns==2.0.0',
    'aiohttp==3.6.2',
    'aiohttp-cors==0.7.0',
    'aiohttp-jinja2==1.2.0',
    'aiohttp-session==2.9.0',
    'aioredis==1.3.1',
    'asyncpg==0.20.1',
    'bcrypt==3.1.7',
    'brotlipy==0.7.0',
    'cchardet==2.1.5',
    'cryptography==2.8',
    'dropbox==9.4.0',
    'gunicorn==20.0.4',
    'Jinja2==2.10.3',
    'Markdown==3.1.1',
    'psycopg2==2.8.4',
    'PyJWT==1.7.1',
    'pytoml==0.1.21',
]

setup(
    name='server.matta.dev',
    version='0.1',
    install_requires=install_requires,
)
