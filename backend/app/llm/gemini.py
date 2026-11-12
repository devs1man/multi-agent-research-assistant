import os

from google import genai
from google.genai import types

from backend.app.llm.base import BaseLLM

class GeminiLLM(BaseLLM):
    def __init__(self, model:str |None = None):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI API KEY not found")

        self.model = model or os.getenv(
            "GEMINI_MODEL",
            "gemini-3.8-flash"
        )

        self.client = genai.client(api_key=api_key)

    def generate(
            self, 
            prompt: str,
            system_instruction: str | None = None
    ) -> str:

        config = None

        if system_instruction:
            config = types.GenerateContentConfig(
                system_instruction=system_instruction
            )
        response = self.client.models.generate_content(
            model = self.model,
            contents = prompt,
            config = config
        )

        if not response.text:
            raise RuntimeError("gemini returned an empty response")

        return response.text