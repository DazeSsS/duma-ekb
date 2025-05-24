rebuild: build down up

build:
	docker compose build

up:
	docker compose up -d

start:
	docker compose start

stop:
	docker compose stop

down:
	docker compose down

restart:
	docker compose restart

pull:
	docker compose pull

push:
	docker compose push

prune:
	docker system prune

db:
	docker compose up -d db

import:
	docker compose run --build --rm app python3 src/manage.py import_data

makemigrations:
	docker compose run --build --rm app python3 src/manage.py makemigrations

createsuperuser:
	docker compose exec app python src/manage.py createsuperuser

flush:
	docker compose run --build --rm app python3 src/manage.py flush

drop:
	docker compose run --build --rm app python3 src/manage.py migrate $(app) zero
