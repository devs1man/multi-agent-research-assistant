from backend.app.llm.base import BaseLLM

class MockLLM(BaseLLM):

    def generate(
        self, 
        prompt: str,
        system_instruction: str |None = None
    )-> str:

        return (
            "This is a mock LLM response. "
            "The system received your prompt successfully. "
            f"Your prompt was: {prompt}"
        )