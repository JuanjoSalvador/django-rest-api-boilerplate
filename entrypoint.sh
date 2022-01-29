#!/bin/bash

echo "Running Django migrations"
python manage.py migrate

echo "Running service..."
python manage.py runserver 0.0.0.0:8000