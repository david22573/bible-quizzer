#!/bin/bash

# Check if .venv directory exists
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

# Activate the virtual environment (cross-platform)
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    # Windows (Git Bash or Cygwin)
    source .venv/Scripts/activate
        pip install -r requirements.txt
        py bible.py
else
    # Unix (Linux or macOS)
    source .venv/bin/activate
        pip install -r requirements.txt
        py bible.py
fi
