import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# Locate project root
BASE_DIR = Path(__file__).resolve().parents[2]

# Load environment variables
load_dotenv(BASE_DIR / ".env")

# Read Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")

# Initialize Gemini client
client = genai.Client(api_key=api_key)

# Send a test prompt
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Explain what a multi-agent AI system is in three sentences."
)

print("Gemini connection successful!")
print(response.text)