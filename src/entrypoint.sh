#!/bin/sh

# if [ "$POSTGRES_DB" = "shiftdatabase" ]
# then
#     echo "Waiting for postgres..."

#     while ! nc -z $DB_HOST $DB_PORT; do
#       sleep 0.1
#     done

#     echo "PostgreSQL started"
# fi

echo uvicorn -------------------------------------------------------
uvicorn src.main:app --host 0.0.0.0 --port 8000
