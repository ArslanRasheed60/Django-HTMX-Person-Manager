#!/bin/bash

# Apply migrations before starting the web server
python manage.py migrate

# Start the actual application
exec "$@"
