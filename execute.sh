#!/bin/sh

# Configuração da venv
ACTIVATE_FILE=venv/bin/activate
if [ ! -f "$ACTIVATE_FILE" ]; then
    python3 -m venv venv
    . "$ACTIVATE_FILE"
    pip install -r requirements.txt
fi

# Ativação da venv
. "$ACTIVATE_FILE"

# Aplicação
gunicorn --bind 0.0.0.0:5000 app:app &

# Serviços
gunicorn --bind 0.0.0.0:5001 --chdir services elementary_service:app &
gunicorn --bind 0.0.0.0:5002 --chdir services transcendental_service:app &
gunicorn --bind 0.0.0.0:5003 --chdir services log_service:app &
