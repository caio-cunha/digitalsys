#!/bin/bash
set -e

cd ./app
echo "Starting Celery Worker - Dev Environment"
echo Starting celery workers
exec celery -A app worker -l INFO