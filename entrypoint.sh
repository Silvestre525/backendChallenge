#!/bin/sh

/wait-for-postgres.sh "$DB_HOST" "echo 'Aplicando migraciones de la base de datos...'"
/wait-for-postgres.sh "$DB_HOST" "python manage.py migrate"

exec "$@"
