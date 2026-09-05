import os

# Safe: Reading token from environment variables instead of hardcoding
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")