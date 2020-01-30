SHELL = /bin/bash
.DEFAULT_GOAL := all

FILE := ''
SERVER_ROOT = ./server

.PHONY: all
all: venv check local

.PHONY: server
server:
	@. .venv/bin/activate; \
	gunicorn server.run:init_app --bind localhost:8080 --worker-class aiohttp.GunicornWebWorker

.PHONY: local
local:
	@. .venv/bin/activate; \
	adev runserver;

.PHONY: destroy
destroy:
	@rm -rf .venv; \

.PHONY: venv
venv:
	@if [ ! -d .venv ]; then \
		python3 -m venv .venv; \
		. .venv/bin/activate; \
		pip install --upgrade pip; \
		pip install -r requirements.txt; \
	fi

.PHONY: check
check: mypy black flake8 static packages

.PHONY: check-file
check-file:
	@. .venv/bin/activate; mypy $(FILE); black $(FILE); flake8 $(FILE);


.PHONY: mypy
mypy: 
	@. .venv/bin/activate; $(foreach file, $(shell find server -name '*.py'), echo $(file); mypy $(file);)

.PHONY: black
black:
	@. .venv/bin/activate; \
	black server --exclude .venv; \

.PHONY: flake8
flake8:
	@. .venv/bin/activate; \
	flake8 server --exclude .venv;

.PHONY: report
report:
	@. .venv/bin/activate; \
	coverage html

.PHONY: packages
packages:
	@. .venv/bin/activate; \
	safety check -r requirements.txt;

.PHONY: static
static:
	@. .venv/bin/activate; \
	bandit -r server

.PHONY: integration-test
integration-test:
	@. .venv/bin/activate; \
	pytest -s tests/integration

.PHONY: unit-test
unit-test:
	@. .venv/bin/activate; \
	coverage run -m unittest discover tests/unit -v