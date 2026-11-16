#AUTHOR: MARCIANO MATTIA FELICE
#DATE: 16/11/2026

import os
import smtplib
import threading
from email.mime.text import MIMEText
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()

SENDER = os.getenv("SENDER")
PASSWORD = os.getenv("PASSWORD")
RECEIVER = os.getenv("RECEIVER")
PORT = int(os.getenv("PORT") or 465)
SUBJECT = os.getenv("SUBJECT")
BODY = os.getenv("BODY")
THREADS_COUNT = os.getenv("THREADS_COUNT")


@dataclass
class Email:
    sender: str
    receiver: str
    subject: str
    body: str


class EmailSender:
    sender_email: str
    email_password: str


    def __init__(self, sender_email: str, email_password: str) -> None:
        self.sender_email = sender_email
        self.email_password = email_password


    def send_email(self, email: Email) -> bool:
        msg = MIMEText(email.body, "html")
        msg["Subject"] = email.subject
        msg["From"] = email.sender
        msg["To"] = email.receiver

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", (int(PORT) or 465)) as server:
                server.login(email.sender, self.email_password)
                server.sendmail(email.sender, email.receiver, msg.as_string())
                return True
        except (smtplib.SMTPException, OSError) as e: print(f"Error: unable to send email: {e}")
        return False


def send_indefinitely(sender: EmailSender, email: Email) -> None:
    while True: sender.send_email(email)


def main() -> None:
    if not SENDER or not PASSWORD or not RECEIVER or not PORT or not SUBJECT or not BODY or not THREADS_COUNT:
        raise ValueError("Please set environment variables")

    sender = EmailSender(SENDER, PASSWORD)
    threads = []
    email = Email(SENDER, RECEIVER, SUBJECT, BODY)

    for i in range(int(THREADS_COUNT)):
        threads.append(threading.Thread(target=send_indefinitely, args=(sender, email)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()