#!/bin/sh

# Configuração da venv
ACTIVATE_FILE=venv/bin/activate

if [ ! -f "$ACTIVATE_FILE" ]; then
    python3 -m venv venv
    . "$ACTIVATE_FILE"
    pip install -r requirements.txt
fi

# Execução da aplicação
. "$ACTIVATE_FILE"
gunicorn --bind 0.0.0.0:5000 app:app
# gunicorn --bind 0.0.0.0:5001 app:app &
