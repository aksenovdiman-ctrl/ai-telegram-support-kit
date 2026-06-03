# Security Policy

## Reporting Security Issues

Please do not open public issues for security problems.

Send a private report to the repository maintainer with:

- affected component;
- reproduction steps;
- impact;
- suggested fix, if known.

## Security Notes

This project handles user messages and may call external AI APIs. Maintainers should:

- never commit API keys or bot tokens;
- avoid logging sensitive user data in production;
- review AI-generated replies before enabling fully automatic responses;
- use environment variables or secret managers for credentials;
- keep dependencies updated.