#!/bin/sh

gunicorn --workers 1 -k gthread --thread=8 --timeout 900 --name app -b 0.0.0.0:5000 app:app --reload
