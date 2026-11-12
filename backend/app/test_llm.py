from pathlib import Path
from dotenv import load_dotenv

from backend.app.llm.factory import get_llm

BASE_DIR = Path(__file__).resolve().parents[2]
load_dotenv(BASE_DIR/".env")

llm = get_llm()

response = llm.generate(
    prompt="What is a multi agent research assistant"
)

print("Selected LLM: ", type(llm).__name__)
print("Response: ", response)