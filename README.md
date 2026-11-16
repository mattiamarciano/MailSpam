# Multithreaded Email Sender

A Python application that sends HTML emails through Gmail SMTP using multithreading. It features configurable thread counts and an object-oriented architecture.

## Features

- Gmail SMTP over SSL.
- HTML email support.
- Multithreaded email sending.
- Configurable SMTP settings.
- Environment-based configuration using `.env`.
- SMTP and connection error handling.

## Requirements

- Python 3.10+
- Gmail account.
- Gmail App Password.

## Installation

Clone the repository:

```bash
git clone https://github.com/mattiamarciano/MailSpam.git
cd MailSpam
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root directory.

Add the following environment variables:

```env
SENDER=your-email@gmail.com
PASSWORD=your-app-password
RECEIVER=recipient@example.com
PORT=465
SUBJECT=Test Email
BODY=<h1>Hello World!</h1>
THREADS_COUNT=5
```

The `.env` file is used to store application configuration and credentials.

| Variable | Description |
|---|---|
| `SENDER` | Sender Gmail address |
| `PASSWORD` | Gmail App Password |
| `RECEIVER` | Recipient email address |
| `PORT` | SMTP SSL port |
| `SUBJECT` | Email subject |
| `BODY` | HTML email content |
| `THREADS_COUNT` | Number of concurrent threads |

**Security:** Never upload real credentials to GitHub. Keep your actual `.env` file private. If you need to publish an example configuration, use `.env.example` with placeholder values.

## Usage

Run the application:

```bash
python main.py
```

The application starts the configured number of threads and waits for all of them to complete.

## Project Structure

```text
.
├── main.py
├── .env
├── requirements.txt
└── README.md
```

## Dependencies

- `python-dotenv` – Loads environment variables from `.env`.
- `smtplib` – SMTP communication.
- `threading` – Concurrent execution.
- `email.mime` – HTML email formatting.

## Notes

- Each thread currently sends the same email to the configured recipient.
- Excessive concurrent connections may trigger Gmail limits.
- Intended for educational purposes and experimentation with Python multithreading and SMTP.
