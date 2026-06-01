# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

SOREFOR is a single-page Flask marketing site for a French professional hunting regulation company. Its sole purpose is to present the company and capture contact leads: visitors fill out a form, which triggers an email notification to the owners via Gmail SMTP.

## Commands

```bash
# Install dependencies
uv sync

# Run locally
uv run flask --app app run

# Run with gunicorn (mirrors production)
uv run gunicorn app:app
```

## Architecture

The app is two files:

- **`app.py`** — Flask routes. `GET /` renders the page; `POST /contact` collects form data, stamps a timestamp, calls `notify_owner()`, and re-renders with `success=True`.
- **`mailer.py`** — `notify_owner(data)` sends the contact form payload as a plain-text email to both `OWNER_EMAIL_1` and `OWNER_EMAIL_2` via Gmail SMTP SSL (port 465).

The single Jinja2 template (`templates/index.html`) is self-contained: all CSS is inline, there is no JS framework, and the `{% if success %}` block swaps the form for a confirmation message.

## Environment variables

Required in `.env` (gitignored):

| Variable | Purpose |
|---|---|
| `EMAIL_USER` | Gmail address used as sender |
| `EMAIL_PASS` | Gmail app password |
| `OWNER_EMAIL_1` | First notification recipient |
| `OWNER_EMAIL_2` | Second notification recipient |

## Deployment

Deployed on Railway. The `Procfile` runs `gunicorn app:app`. Push to `master` triggers a deploy.
