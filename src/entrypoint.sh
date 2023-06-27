#!/bin/sh

if [ "$POSTGRES_DB" = "shiftdatabase" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 1
    done

    echo "PostgreSQL started"
fi

gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
# uvicorn src.main:app --host 0.0.0.0 --port 8000
