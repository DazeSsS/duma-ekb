# PROD

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


# TEST

rebuild-test: build-test down-test up-test

build-test:
	docker compose -f docker-compose.test.yaml build

up-test:
	docker compose -f docker-compose.test.yaml up -d

start-test:
	docker compose -f docker-compose.test.yaml start

stop-test:
	docker compose -f docker-compose.test.yaml stop

down-test:
	docker compose -f docker-compose.test.yaml down

restart-test:
	docker compose -f docker-compose.test.yaml restart

pull-test:
	docker compose -f docker-compose.test.yaml pull

push-test:
	docker compose -f docker-compose.test.yaml push

db-test:
	docker compose -f docker-compose.test.yaml up -d db

import-test:
	docker compose -f docker-compose.test.yaml run --build --rm app python3 src/manage.py import_data

makemigrations-test:
	docker compose -f docker-compose.test.yaml run --build --rm app python3 src/manage.py makemigrations

createsuperuser-test:
	docker compose -f docker-compose.test.yaml exec app python src/manage.py createsuperuser

flush-test:
	docker compose -f docker-compose.test.yaml run --build --rm app python3 src/manage.py flush

drop-test:
	docker compose -f docker-compose.test.yaml run --build --rm app python3 src/manage.py migrate $(app) zero
