#!/bin/bash
set -e

echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "Starting Gunicorn..."
exec python -m gunicorn --bind :8000 --workers 1 --worker-class sync --worker-tmp-dir /dev/shm --timeout 30 --graceful-timeout 5 --access-logfile - --error-logfile - sisnum.wsgi:application
