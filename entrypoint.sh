#!/bin/sh
python manage.py makemigrations
python manage.py migrate
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@admin.com', 'rdms_admin001')" | python manage.py shell
exec "$@"