#!/bin/bash

# Apply database migrations
echo "Applying database migrations..."
python manage.py makemigrations
python manage.py migrate
echo " successfully migrated......"
# Seed fake data
echo "Seeding fake data..."
python manage.py seed tasks --number=15

# Start server
echo "Starting server..."
exec "$@"
