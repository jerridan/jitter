init: create-venv install
	. .venv/bin/activate

create-venv:
	python -m venv .venv

install:
	. .venv/bin/activate; \
	poetry install --with dev --sync

build:
	. .venv/bin/activate; \
	poetry run pyinstaller --onefile main/jitter.py