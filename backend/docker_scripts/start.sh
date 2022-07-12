#!/bin/bash  

cd /app  

echo "DJANGO_DEBUG:" ${DJANGO_DEBUG}

if [ "$DJANGO_DEBUG" = "true" ]; then  
    gunicorn \
        --reload \
        --bind 0.0.0.0:8000 \
        --workers 2 \
        --log-level DEBUG \
        --access-logfile "-" \
        --error-logfile "-" core.wsgi
else  
    gunicorn \
        --bind 0.0.0.0:8000 \
        --workers 2 \
        --log-level DEBUG \
        --access-logfile "-" \
        --error-logfile "-" core.wsgi
fi
