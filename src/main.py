import asyncio

from agents import Runner, trace

from manager_agent import mail_manager
from prompts import TASK


async def main() -> None:
    with trace("Email manager"):
        result = await Runner.run(
            mail_manager,
            TASK,
        )


if __name__ == "__main__":
    asyncio.run(main())
