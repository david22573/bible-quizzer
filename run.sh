#!/bin/bash

# Check if .venv directory exists
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
    pip install -r requirements.txt
fi

# Activate the virtual environment (cross-platform)
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    # Windows (Git Bash or Cygwin)
    source .venv/Scripts/activate
    flask --app app run --debug
else
    # Unix (Linux or macOS)
    source .venv/bin/activate
    flask --app app run
fi

# Deactivate the virtual environment
deactivate
