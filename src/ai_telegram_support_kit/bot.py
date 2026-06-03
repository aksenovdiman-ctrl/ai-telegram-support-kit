import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

from .config import load_settings
from .llm import ReplyDraftGenerator
from .storage import StoredMessage, SupportStorage
from .triage import triage_message


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main() -> None:
    settings = load_settings()
    if not settings.telegram_bot_token:
        raise RuntimeError("TELEGRAM_BOT_TOKEN is required")

    storage = SupportStorage(settings.database_path)
    storage.migrate()

    draft_generator = None
    if settings.enable_ai_replies and settings.openai_api_key:
        draft_generator = ReplyDraftGenerator(settings.openai_api_key, settings.openai_model)

    bot = Bot(token=settings.telegram_bot_token)
    dispatcher = Dispatcher()

    @dispatcher.message(F.text)
    async def handle_text(message: Message) -> None:
        text = message.text or ""
        triage = triage_message(text)
        storage.save_message(
            StoredMessage(
                user_id=message.from_user.id if message.from_user else 0,
                username=message.from_user.username if message.from_user else None,
                text=text,
                category=triage.category,
                urgency=triage.urgency,
                needs_human=triage.needs_human,
            )
        )

        if draft_generator is None:
            await message.answer("Спасибо, сообщение получено. Мы скоро вернемся с ответом.")
            return

        try:
            draft = draft_generator.generate(text, triage.category, triage.urgency)
        except Exception:
            logger.exception("Failed to generate AI draft")
            await message.answer("Спасибо, сообщение получено. Передали его оператору.")
            return

        await message.answer(draft)

    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())