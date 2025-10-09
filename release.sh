#!/bin/bash
python manage.py migrate
python manage.py setup_superuser
