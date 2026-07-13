import asyncio

from agents.followup_agent import FollowUpAgent


explanation = {
    "weaknesses": [
        "No Docker experience",
        "No LangGraph experience",
        "Limited Vector Database knowledge"
    ]
}


async def main():

    agent = FollowUpAgent()

    result = await agent.execute(explanation)

    print(result)


asyncio.run(main())