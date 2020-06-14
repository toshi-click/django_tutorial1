#!/bin/bash

# Install packages for local
pip install -r requirements/local.txt

# Set environment for local
export DJANGO_SETTINGS_MODULE=config.settings.local

# Prepare database
python manage.py migrate
python manage.py shell -c "from django.contrib.auth import get_user_model; get_user_model().objects.create_superuser('admin', 'admin@example.com', 'adminpass');"

# Start runserver
gunicorn config.wsgi --workers 1 --bind 0.0.0.0:80 --max-requests 1
