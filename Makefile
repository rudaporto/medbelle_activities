# ** Important **
# all commands can be adjusted for your enviroment

create_venv:
	virtualenv -p /usr/bin/python3 venv

packages:
	pip install --upgrade -r requirements.txt

migrate_db:
	python manage.py migrate

create_admin:
	python manage.py createsuperuser --email admin@medbelle.com --username=admin

run_server:
	python manage.py makemigrations
	python manage.py runserver 8089
