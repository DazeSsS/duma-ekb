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

runserver:
	python src/manage.py runserver

makemigrations:
	python src/manage.py makemigrations

migrate:
	python src/manage.py migrate

flush:
	python src/manage.py flush

drop:
	python src/manage.py migrate $(app) zero

createsuperuser:
	python src/manage.py createsuperuser

collectstatic:
	python src/manage.py collectstatic --no-input

shell:
	python src/manage.py shell
