#!/bin/sh
set -e
mkdir -p "$DATA_DIR"
python manage.py migrate --noinput
python manage.py seed
if [ -n "$ADMIN_PASSWORD" ]; then
  python manage.py shell -c "
import os
from django.contrib.auth import get_user_model
U = get_user_model()
if not U.objects.filter(username='admin').exists():
    U.objects.create_superuser('admin', 'admin@example.com', os.environ['ADMIN_PASSWORD'])
"
fi
exec gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 2
