# AI Telegram Support Kit

Open-source starter kit for building AI-assisted Telegram support bots for small teams, online schools, creators, and community projects.

The project focuses on practical maintenance workflows:

- collect user messages and support requests in a structured way;
- classify incoming messages by topic and urgency;
- generate safe draft replies with an LLM provider;
- store conversations locally in SQLite;
- make it easier for maintainers to review, debug, and improve bot logic.

This repository is intentionally small and readable. It is designed as a foundation for maintainers who need a transparent bot architecture instead of a closed no-code platform.

## Why This Exists

Many small teams run Telegram bots for support, lead collection, online courses, and communities. Common problems are:

- no clear message history;
- broken automation chains;
- poor visibility into errors;
- limited integrations in bot builders;
- hard-to-review logic when the bot grows.

AI Telegram Support Kit provides a code-first baseline that can be audited, tested, extended, and maintained in public.

## Features

- Telegram bot entrypoint based on `aiogram`.
- AI reply draft generation through the OpenAI API.
- Deterministic triage rules for common support categories.
- SQLite storage for users, messages, and triage results.
- Environment-based configuration.
- Unit tests for core logic.
- GitHub Actions workflow for CI.

## Project Structure

```text
.
├── src/ai_telegram_support_kit/
│   ├── bot.py          # Telegram bot runtime
│   ├── config.py       # Environment configuration
│   ├── llm.py          # LLM provider wrapper
│   ├── prompts.py      # Prompt templates
│   ├── storage.py      # SQLite storage
│   └── triage.py       # Message classification
├── tests/
│   ├── test_storage.py
│   └── test_triage.py
├── .env.example
├── pyproject.toml
└── README.md
```

## Quick Start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env
```

Fill `.env`:

```text
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-5-mini
DATABASE_PATH=./support_bot.db
```

Run the bot:

```bash
python -m ai_telegram_support_kit.bot
```

Run tests:

```bash
pytest
```

## Maintainer Workflows

The repository is built around real maintainer tasks:

- review incoming support issues;
- inspect triage decisions;
- improve prompt templates;
- add integrations with Google Sheets, CRM tools, payment providers, or admin dashboards;
- review pull requests and test bot logic before release.

## Roadmap

- Admin dashboard for reviewing conversations.
- Google Sheets export.
- Webhook mode for production deployment.
- More integrations for online schools and creator communities.
- Better safety checks for AI-generated replies.
- Codex Security scan workflow for bot and integration code.

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## License

MIT. See [LICENSE](LICENSE).