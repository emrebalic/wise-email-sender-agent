from agents import Agent
from prompts import HISTORIAN_PROMPT, LITERARY_PSYCHOLOGY_PROMPT, PHILOSOPHER_PROMPT
from structed_output import EmailWriter

MODEL_NAME = "gpt-5.4-mini"

philosopher_agent = Agent(
    name="philosopher agent",
    instructions=PHILOSOPHER_PROMPT,
    model=MODEL_NAME,
    output_type=EmailWriter,
)

historian_agent = Agent(
    name="historian agent",
    instructions=HISTORIAN_PROMPT,
    model=MODEL_NAME,
    output_type=EmailWriter,
)

literature_agent = Agent(
    name="literature agent",
    instructions=LITERARY_PSYCHOLOGY_PROMPT,
    model=MODEL_NAME,
    output_type=EmailWriter,
)
