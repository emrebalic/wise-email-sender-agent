import os

import resend
from agents import function_tool
from dotenv import load_dotenv

from writer_agents import historian_agent, literature_agent, philosopher_agent

load_dotenv(override=True)

resend.api_key = os.getenv("RESEND_API_KEY")
EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_TO = os.getenv("EMAIL_TO")


description = "Use this tool to write a wisdom email. In the input, just instruct it to write a wisdom email."


tool1 = philosopher_agent.as_tool(
    tool_name="philosopher_writer", tool_description=description
)
tool2 = historian_agent.as_tool(
    tool_name="historian_writer", tool_description=description
)
tool3 = literature_agent.as_tool(
    tool_name="literature_writer", tool_description=description
)


@function_tool
def send_email_tool(
    subject: str,
    text_body: str,
    html_body: str,
) -> str:
    """
    Send an email using Resend.

    Args:
        subject: Email subject.
        text_body: Plain text version of the email.
        html_body: HTML version of the email.

    Returns:
        response id if succesful, failed otherwise
    """

    try:
        response = resend.Emails.send(
            {
                "from": EMAIL_FROM,
                "to": EMAIL_TO,
                "subject": subject,
                "text": text_body,
                "html": html_body,
            }
        )

        return response["id"]

    except Exception as e:
        return f"Failed: {e}"


tools = [tool1, tool2, tool3, send_email_tool]
