#!/bin/sh

until cd .
do
    echo "Waiting for server volume..."
done

# run a worker :)
celery -A backend worker -l info --concurrency 1 -E
