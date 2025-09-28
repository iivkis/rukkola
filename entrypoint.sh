#!/bin/sh

uv run alembic upgrade head

uv run uvicorn rukkola.src:main --host 0.0.0.0 --port 8000