from ai_telegram_support_kit.storage import StoredMessage, SupportStorage


def test_storage_saves_message(tmp_path):
    storage = SupportStorage(str(tmp_path / "support.db"))
    storage.migrate()

    message_id = storage.save_message(
        StoredMessage(
            user_id=123,
            username="user",
            text="Не работает доступ",
            category="access",
            urgency="normal",
            needs_human=False,
        )
    )

    rows = storage.list_recent_messages()

    assert message_id == 1
    assert len(rows) == 1
    assert rows[0]["text"] == "Не работает доступ"
    assert rows[0]["category"] == "access"