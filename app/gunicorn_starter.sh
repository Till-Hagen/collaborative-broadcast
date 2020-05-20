#!/bin/sh

cd app
ls -l
gunicorn --bind 0.0.0.0:8005 app:app
