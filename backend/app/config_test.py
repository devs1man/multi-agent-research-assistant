import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[2]

# Load .env from project root
env_path = BASE_DIR / ".env"

load_dotenv(dotenv_path=env_path)

# Read API key
api_key = os.getenv("OPENAI_API_KEY")

print("Project directory:", BASE_DIR)
print("Environment file exists:", env_path.exists())
print("API key loaded:", bool(api_key))