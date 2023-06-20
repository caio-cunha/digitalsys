#!/bin/bash
set -e

echo "Starting System SYS API - Dev Environment"
# Allows for log messages
export PYTHONUNBUFFERED=1

python3 app/manage.py makemigrations
python3 app/manage.py migrate

echo "Creating superuser..."
python app/manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
user = User.objects.create_superuser('admin', 'admin@example.com', '123456')
EOF

echo "#====================================="
echo "Starting application"
echo "#====================================="
python3 app/manage.py runserver 0.0.0.0:8000