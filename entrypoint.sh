#!/bin/sh
set -e

echo "Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

echo "Ajustando permissões dos arquivos estáticos..."
find /app/staticfiles -type d -exec chmod 755 {} +
find /app/staticfiles -type f -exec chmod 644 {} +

echo "Aplicando migrações..."
python manage.py migrate --noinput

echo "Criando superusuário padrão (se não existir)..."
python manage.py shell -c "
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', '', 'admin')
    print('Superusuário admin criado.')
else:
    print('Superusuário admin já existe.')
"

echo "Iniciando Gunicorn..."
exec gunicorn sisnum.wsgi:application --bind 0.0.0.0:8000 --workers 1
