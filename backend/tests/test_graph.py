import asyncio

from database.database import SessionLocal

from graph.workflow import workflow
from schemas.workflow_state import WorkflowState

from repositories.evaluation_repository import EvaluationRepository


async def main():

    db = SessionLocal()

    try:

        state = WorkflowState(
            resume_text="""
Python Developer

Skills:
Python
FastAPI
SQL
Machine Learning
Docker
""",

            job_description="""
Looking for an AI Engineer.

Required Skills:
Python
FastAPI
Machine Learning
Docker
Git
"""
        )

        result = await workflow.ainvoke(state)

        # Save evaluation to database
        EvaluationRepository.create(
            db,
            result
        )

        print("\n========== GRAPH RESULT ==========\n")
        print(result)
        print("\n==================================\n")

        print("\n✅ Evaluation saved successfully.\n")

    finally:
        db.close()


if __name__ == "__main__":
    asyncio.run(main())