import asyncio

from agents.explainability_agent import ExplainabilityAgent


match_result = {
    "overall_score": 60,
    "recommendation": "Potential Hire",
    "confidence": 70,
    "matched_skills": [
        "Python",
        "TensorFlow",
        "AWS"
    ],
    "missing_skills": [
        "Docker",
        "LangGraph"
    ]
}


async def main():

    agent = ExplainabilityAgent()

    result = await agent.execute(match_result)

    print(result)


asyncio.run(main())