# Contributing

Thanks for your interest in contributing.

## Good First Contributions

- Improve documentation.
- Add tests for triage behavior.
- Add support for a new export format.
- Improve prompt templates.
- Add examples for real support workflows.

## Development

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

## Pull Requests

Please include:

- a clear description of the change;
- tests for behavior changes;
- notes about any new environment variables;
- screenshots or logs if the change affects bot output.

## Code Style

Keep code small, explicit, and easy to review. Prefer boring, maintainable Python over clever abstractions.