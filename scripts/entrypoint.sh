#!/bin/sh

set -e
python manage.py migrate
python manage.py loaddata moviesapp/fixtures/movie.json
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | python manage.py shell
python manage.py collectstatic --noinput

uwsgi --socket :8000 --master --enable-threads --wsgi-file config/wsgi.py