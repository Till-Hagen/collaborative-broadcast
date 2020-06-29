#!/bin/sh

cd app
ls -l
gunicorn --bind 0.0.0.0:8005 --timeout 120 app:app
