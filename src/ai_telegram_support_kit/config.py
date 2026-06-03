from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    telegram_bot_token: str
    openai_api_key: str
    openai_model: str = "gpt-5-mini"
    database_path: str = "./support_bot.db"
    enable_ai_replies: bool = True


def _bool_from_env(value: str | None, default: bool) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def load_settings() -> Settings:
    return Settings(
        telegram_bot_token=os.getenv("TELEGRAM_BOT_TOKEN", ""),
        openai_api_key=os.getenv("OPENAI_API_KEY", ""),
        openai_model=os.getenv("OPENAI_MODEL", "gpt-5-mini"),
        database_path=os.getenv("DATABASE_PATH", "./support_bot.db"),
        enable_ai_replies=_bool_from_env(os.getenv("ENABLE_AI_REPLIES"), True),
    )