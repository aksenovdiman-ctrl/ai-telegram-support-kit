from openai import OpenAI

from .prompts import SUPPORT_SYSTEM_PROMPT, build_support_prompt


class ReplyDraftGenerator:
    def __init__(self, api_key: str, model: str):
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def generate(self, user_message: str, category: str, urgency: str) -> str:
        prompt = build_support_prompt(user_message, category, urgency)
        response = self.client.responses.create(
            model=self.model,
            input=[
                {"role": "system", "content": SUPPORT_SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
        )
        return response.output_text.strip()