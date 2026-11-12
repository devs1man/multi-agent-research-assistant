from abc import ABC, abstractmethod

class BaseLLM(ABC):
    @abstractmethod
    def generate(
        self, 
        prompt: str,
        system_instruction: str | None = None
    ) -> str:
        """
        Generate a text response from the language model.

        Args:
            prompt: The user's input prompt.
            system_instruction: Optional instructions defining
                                the model's behaviour.

        Returns:
            Generated text response.
        """
        pass