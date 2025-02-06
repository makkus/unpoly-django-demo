#!/usr/bin/env bash

set -e

rm -f db.sqlite3

export DEBUG=true

rm -f src/unpoly_app/migrations/0*.py

source .venv/bin/activate

python manage.py makemigrations

python manage.py migrate

