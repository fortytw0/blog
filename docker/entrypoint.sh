#! /bin/sh

set -e

cd /blog

python manage.py makemigrations
python manage.py migrate

python manage.py shell < docker/set_domain_name.py

uwsgi --http :8000 --master --enable-threads --module config.wsgi