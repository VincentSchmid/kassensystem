#!/bin/bash

# entrypoint.sh file of Dockerfile

set -o errexit  
set -o pipefail  
set -o nounset

postgres_ready() {  
    python << END
import sys

from psycopg import connect
from psycopg.conninfo import conninfo_to_dict
from psycopg.errors import OperationalError

pg_uri = "${DATABASE_URL}"
conn_dict = conninfo_to_dict(pg_uri)

try:
    connect(**conn_dict)
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

python manage.py initgroups

if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    python manage.py initadmin  \
    --username "$DJANGO_SUPERUSER_USERNAME" \
    --email "$DJANGO_SUPERUSER_EMAIL" \
    --password "$DJANGO_SUPERUSER_PASSWORD"
fi

exec "$@"
