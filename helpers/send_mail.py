from configs.config import MAIL_FROM, MAIL_PASSWORD, MAIL_PORT, MAIL_SERVER,  MailBody
from ssl import create_default_context
from email.mime.text import MIMEText
from smtplib import SMTP


def send_email(data: dict | None = None):
    msg = MailBody(**data)
    message = MIMEText(msg.body, "html")
    message["FROM"] = MAIL_FROM
    message["TO"] = ",".join(msg.to)
    message["Subject"] = msg.subject

    ctx = create_default_context()

    try: 
        with SMTP(MAIL_SERVER, MAIL_PORT) as server:
            server.ehlo()
            server.starttls(context=ctx)
            server.ehlo()
            server.login(MAIL_FROM, MAIL_PASSWORD)
            server.send_message(message)
            server.quit()
    except Exception as e:
        return {"status": 500, "errors": e}