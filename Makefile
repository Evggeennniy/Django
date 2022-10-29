SHELL := /bin/bash

manage_py := python3 app/manage.py
# ^ Using variables to determine repeated references

runserver:
	$(manage_py) runserver

runshellplus:
	$(manage_py) shell_plus  --print-sql

showurls:
	$(manage_py) show_urls

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
	$(manage_py) makemigrations 
	$(manage_py) migrate 
	$(manage_py) runserver
# ^ Command launches a list of commands

pytest:
	pytest app/tests/

testcoverage:
	pytest --cov=app app/tests/ --cov-report html && coverage report --fail-under=80

showtestcov:
	python3 -c "import webbrowser; webbrowser.open('.pytest_cache/coverage/index.html')"

parse_privatbank_archive:
	$(manage_py) parser_privatbank_archive

gunicorn8001:
	cd app && gunicorn settings.wsgi:application --bind 0.0.0.0:8001 --workers 9 --threads 4 --log-level info --max-requests 1 --timeout 10

gunicorn8002:
	cd app && gunicorn settings.wsgi:application --bind 0.0.0.0:8002 --workers 9 --threads 4 --log-level info --max-requests 1 --timeout 10