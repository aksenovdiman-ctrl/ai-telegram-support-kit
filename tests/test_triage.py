from ai_telegram_support_kit.triage import triage_message


def test_payment_message_needs_human():
    result = triage_message("Я оплатил курс, но чек не пришел")

    assert result.category == "payment"
    assert result.urgency == "normal"
    assert result.needs_human is True


def test_urgent_message_has_high_urgency():
    result = triage_message("Срочно, доступ не работает")

    assert result.category == "access"
    assert result.urgency == "high"
    assert result.needs_human is True


def test_general_message_can_be_automatic():
    result = triage_message("Здравствуйте, расскажите подробнее")

    assert result.category == "general"
    assert result.urgency == "normal"
    assert result.needs_human is False