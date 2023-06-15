#!/bin/bash
set -e

echo "Starting System SYS API - Dev Environment"
# Allows for log messages
export PYTHONUNBUFFERED=1

echo "#====================================="
echo "Starting application"
echo "#====================================="
python3 app/manage.py runserver 0.0.0.0:8000