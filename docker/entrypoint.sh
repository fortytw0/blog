#! /bin/sh

cd  /blog 
python3 manage.py makemigrations 
python3 manage.py migrate
python3 manage.py collectstatic --no-input 
python3 manage.py shell < /docker/set_domain_name.py  

nginx -c /docker/nginx.conf -g "pid /tmp/nginx.pid;"

uwsgi --socket :8000 --master --enable-threads --module config.wsgi 
 