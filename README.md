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

## Local Setup

Clone the project:

```bash
git clone https://github.com/Shresth17/MailMate.git
cd MailMate
```

Create and activate a virtual environment:

```bash
python3 -m venv myenv
source myenv/bin/activate
```

Install dependencies:

```bash
pip3 install -r requirements.txt
```

Add your local Gmail OAuth credential files in the repository root:

- `client_secret.json`
- `gmail_token.json`

These files should stay local and must not contain committed credentials.

Start the sync service:

```bash
cd services
python3 sync_service.py
```

Run the terminal app from a second shell:

```bash
cd src
python3 main.py
```

Wait a few minutes before starting the CLI the first time, since the sync service may need time to download messages.

## Maintainer

Shresth Sharma
