from agents import Agent

from prompts import MAIN_PROMPT
from tools import tools

MODEL_NAME = "gpt-5.4-mini"

mail_manager = Agent(
    name="Mail Manager", instructions=MAIN_PROMPT, tools=tools, model=MODEL_NAME
)
