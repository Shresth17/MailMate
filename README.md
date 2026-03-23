# MailMate

MailMate is an AI-powered terminal assistant for reading inbox threads, syncing Gmail data locally, and answering questions about your email history.

## Features

- Read inbox threads from the terminal.
- Sync Gmail data into a local store for querying.
- Use OpenAI models to answer questions about your emails.
- Extract event-like information from email content.

## Environment Variables

Create a `.env` file in the repository root and add:

- `OPENAI_API_KEY`
- `DB_URI`
- `CHROMA_DB_PATH`

If you use the helper utilities in `src/utils/events.py`, you can also set:

- `MAIL_DB_NAME`
- `MAIL_DB_USER`
- `MAIL_DB_PASSWORD`
- `MAIL_DB_HOST`
- `MAIL_DB_PORT`
