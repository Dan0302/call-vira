#!/bin/bash
export $(grep -v '^#' .env | xargs)
gunicorn -w 2 -b 0.0.0.0:5000 api.webhook_handler:app --config deploy/gunicorn_config.py