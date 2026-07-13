from services.interview_evaluator_service import (
    InterviewEvaluatorService
)


transcript = """
Interviewer:
Explain Docker.

Candidate:
Docker is a containerization platform that packages
applications with all dependencies. It allows the
same application to run consistently across
development, testing, and production environments.
"""

result = InterviewEvaluatorService.evaluate(
    transcript
)

print(result)