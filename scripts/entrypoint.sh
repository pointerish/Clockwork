#!/bin/sh

set -e
python manage.py migrate
python manage.py loaddata moviesapp/fixtures/movie.json
python manage.py createsuperuser
python manage.py collectstatic --noinput

uwsgi --socket :8000 --master --enable-threads --wsgi-file config/wsgi.py