#!/bin/bash

# entrypoint.sh file of Dockerfile

set -o errexit  
set -o pipefail  
set -o nounset

postgres_ready() {  
    python << END
import sys

from psycopg2 import connect
from psycopg2.errors import OperationalError

try:
    connect(
        dbname="${POSTGRES_NAME}",
        user="${POSTGRES_USER}",
        password="${POSTGRES_PASSWORD}",
        host="${POSTGRES_HOST}",
        port="5432"
    )
except OperationalError:
    sys.exit(-1)
END
}

until postgres_ready; do
  >&2 echo "Waiting for PostgreSQL to become available..."
  sleep 5
done
>&2 echo "PostgreSQL is available"

python manage.py collectstatic --noinput  
python manage.py makemigrations  
python manage.py migrate

if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    python manage.py initadmin
fi

exec "$@"
