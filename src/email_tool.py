import os

import resend
from dotenv import load_dotenv

load_dotenv(override=True)

resend.api_key = os.getenv("RESEND_API_KEY")
email_from = os.getenv("EMAIL_FROM")
email_to = os.getenv("EMAIL_TO")


r = resend.Emails.send(
    {
        "from": email_from,
        "to": email_to,
        "subject": "Hello World",
        "html": "<p>Congrats on sending your <strong>first email</strong>!</p>",
    }
)

print(r)
