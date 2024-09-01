if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    # Windows (Git Bash or similar)
    source .venv/Scripts/activate
elif [[ "$OSTYPE" == "linux-android" || "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux or Termux (Android)
    source .venv/bin/activate
else
    echo "Unsupported operating system"
    exit 1
fi
nohup py bible.py > /dev/null 2>&1 &