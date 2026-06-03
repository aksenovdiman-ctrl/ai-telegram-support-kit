SUPPORT_SYSTEM_PROMPT = """You are a support assistant for a small online team.
Write concise, calm, helpful draft replies.
Do not invent facts. If the request requires a human operator, say that the
message should be escalated."""


def build_support_prompt(user_message: str, category: str, urgency: str) -> str:
    return (
        "Prepare a draft reply for this Telegram support message.\n"
        f"Category: {category}\n"
        f"Urgency: {urgency}\n"
        f"User message: {user_message}\n"
    )