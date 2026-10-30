import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

BASE_DIR = Path(__file__).resolve().parents[2]

load_dotenv(BASE_DIR / ".env")

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

try:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input="Say hello in one sentence."
    )

    print("API connection successful!")
    print(response.output_text)

except Exception as e:
    print("API connection failed!")
    print(type(e).__name__, str(e))