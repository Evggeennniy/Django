SHELL := /bin/bash

manage_py := python3 app/manage.py
# ^ Using variables to determine repeated references

runserver:
	$(manage_py) runserver

runshellplus:
	$(manage_py) shell_plus  --print-sql

makemigrate:
	$(manage_py) makemigrations

migrate:
	$(manage_py) migrate

runrabbitmq:
	systemctl start rabbitmq-server

runcelwork:
	cd app & celery -A settings worker --loglevel=INFO

runcelbeat:
	cd app & celery -A settings beat --loglevel=INFO
# ^ Combining commands using &

build_and_run:
	makemigrate /
	migrate /
	runserver
# ^ Command launches a list of commands


