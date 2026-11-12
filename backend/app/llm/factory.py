import os 

from backend.app.llm.base import BaseLLM
from backend.app.llm.gemini import GeminiLLM
from backend.app.llm.mock import MockLLM

def get_llm() -> BaseLLM:
    provider = os.getenv("LLM_PROVIDER", "mock").lower()

    if provider == "gemini":
        return GeminiLLM()

    elif provider == "mock":
        return MockLLM()

    else:
        raise ValueError(
            f"Unsupported LLM provider: {provider}"
        )