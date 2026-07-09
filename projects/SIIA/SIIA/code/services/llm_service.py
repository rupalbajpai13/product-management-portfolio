import os


class LLMService:
    """
    Service responsible for generating LLM-based explanations.

    Current implementation:
        - Calls Claude API via anthropic SDK if ANTHROPIC_API_KEY is set.

    Future implementation:
        - SAP AI Core
        - Azure OpenAI
        - Any other LLM provider
    """

    def __init__(self):
        self.api_key = os.getenv("ANTHROPIC_API_KEY")
        self.model = "claude-opus-4-8"

    def generate(self, prompt: str) -> dict:
        if not self.api_key:
            return self._fallback()

        try:
            import anthropic
            client = anthropic.Anthropic(api_key=self.api_key)
            response = client.messages.create(
                model=self.model,
                max_tokens=1024,
                messages=[{"role": "user", "content": prompt}]
            )
            text = response.content[0].text
            return self._parse_response(text)

        except Exception as e:
            return self._fallback(error=str(e))

    def _parse_response(self, text: str) -> dict:
        return {
            "root_cause": self._extract_section(text, "Root Cause"),
            "recommendation": self._extract_section(text, "Resolution"),
            "risk": self._extract_section(text, "Risk"),
            "confidence": 0.85,
        }

    def _extract_section(self, text: str, section: str) -> str:
        lines = text.split("\n")
        capture = False
        result = []
        for line in lines:
            if section.lower() in line.lower():
                capture = True
                continue
            if capture:
                if line.strip().startswith(("1.", "2.", "3.", "**", "#")) and result:
                    break
                if line.strip():
                    result.append(line.strip())
        return " ".join(result) if result else text[:200]

    def _fallback(self, error: str = None) -> dict:
        return {
            "root_cause": "LLM not available. Please review findings above for root cause.",
            "recommendation": "Check the findings section for SAP T-codes and recommended actions.",
            "risk": "Unable to assess risk automatically. Manual review required.",
            "confidence": 0.0,
        }
