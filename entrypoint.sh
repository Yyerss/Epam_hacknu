#!/bin/sh

# Set Django settings module environment variable

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput

# Check if migrations were successful

# Start server
echo "Starting server..."
exec gunicorn SmartCookBackend.wsgi:application --bind 0.0.0.0:8000