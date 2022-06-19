#!/bin/bash

# entrypoint.sh file of Dockerfile

set -o errexit  
set -o pipefail  
set -o nounset

if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    python manage.py initadmin
fi

python manage.py collectstatic --noinput  
python manage.py makemigrations  
python manage.py migrate

exec "$@"
