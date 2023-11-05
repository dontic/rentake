#!/bin/sh

until cd .
do
    echo "Waiting for server volume..."
done

# run celery beat
celery -A rentake beat -l info
