# from ethanportfolio import settings

class settings:
    DEFAULT_FROM_EMAIL = "mail@ethankremer.com"
    DEFAULT_EMAIL_SUBJECT = "SENT FROM PYTHON"

import smtplib
from email.message import EmailMessage

def send_email(
    *,
    recipient: str,
    from_email=settings.DEFAULT_FROM_EMAIL,
    subject=settings.DEFAULT_EMAIL_SUBJECT,
    content: str):
    
    msg = EmailMessage()
    msg['From'] = from_email
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.add_header('Content-Type', 'text')

    msg.set_content(content)

    msg.set_payload("This is your message.")

    smtp_obj = smtplib.SMTP("localhost")
    smtp_obj.sendmail(msg['From'], [msg['To']], msg.as_string())
    smtp_obj.quit()

send_email(
    recipient="ethankremer.web@gmail.com",
    subject="hello",
    content="OSIDFOISDJF"
)