#!/bin/sh

python manage.py compilescss
python manage.py collectstatic --noinput
python manage.py migrate --noinput
service cron start
python manage.py crontab add
gunicorn -w 4 task_manager.wsgi -b 0.0.0.0:8000