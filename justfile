# Justfile

# Default recipe (optional)
default:
    @just --list

# Create a new database
new-db:
    ./scripts/new_db.sh
    # snapshot
    cp ./db.sqlite3 ./db_empty.sqlite3


db-snapshot:
    cp ./db.sqlite3 ./db_snapshot.sqlite3

db-restore:
    cp ./db_snapshot.sqlite3 ./db.sqlite3

db-clean:
    cp ./db_empty.sqlite3 ./db.sqlite3

ruff:
    uv run ruff check carbonsheet --fix

reformat-templates:
    uv run djlint --reformat src/unpoly_app/templates

runserver:
    uv run python manage.py runserver --force-color 0.0.0.0:8001

tailwind:
    FORCE_COLOR=true ./bin/tailwindcss -c tailwind.config.js -i ./src/unpoly_app/static/css/input.css -o src/unpoly_app/static/css/tailwind.css --watch
migrations:
    uv run manage.py makemigrations unpoly_app && python manage.py migrate

