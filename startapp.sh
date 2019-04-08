#!/bin/bash
#before running this make sure redis is running

#starts django server
python3 manage.py runserver & 
sleep 2
#starts celery handlers

celery -A ALFF worker -l info &
sleep 2
celery -A ALFF beat -l info &
sleep 2
