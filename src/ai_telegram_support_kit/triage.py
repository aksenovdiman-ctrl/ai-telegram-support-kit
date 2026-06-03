from dataclasses import dataclass


@dataclass(frozen=True)
class TriageResult:
    category: str
    urgency: str
    needs_human: bool


PAYMENT_WORDS = {"payment", "paid", "invoice", "refund", "оплата", "оплатил", "чек", "возврат"}
ACCESS_WORDS = {"access", "login", "password", "доступ", "логин", "пароль", "курс", "урок"}
TECH_WORDS = {"error", "bug", "broken", "ошибка", "не работает", "сломалось", "не приходит"}
URGENT_WORDS = {"urgent", "asap", "срочно", "горит", "сейчас"}


def triage_message(text: str) -> TriageResult:
    normalized = text.strip().lower()

    if any(word in normalized for word in PAYMENT_WORDS):
        category = "payment"
    elif any(word in normalized for word in ACCESS_WORDS):
        category = "access"
    elif any(word in normalized for word in TECH_WORDS):
        category = "technical"
    else:
        category = "general"

    urgency = "high" if any(word in normalized for word in URGENT_WORDS) else "normal"
    needs_human = category in {"payment", "technical"} or urgency == "high"

    return TriageResult(category=category, urgency=urgency, needs_human=needs_human)