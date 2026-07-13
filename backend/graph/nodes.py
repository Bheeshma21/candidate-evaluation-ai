from schemas.workflow_state import WorkflowState

from audit.logger import AuditLogger

from agents.resume_agent import ResumeAgent
from agents.job_agent import JobAgent
from agents.match_agent import MatchAgent
from agents.explainability_agent import ExplainabilityAgent
from agents.followup_agent import FollowUpAgent


resume_agent = ResumeAgent()
job_agent = JobAgent()
match_agent = MatchAgent()
explainability_agent = ExplainabilityAgent()
followup_agent = FollowUpAgent()


async def resume_node(state: WorkflowState):

    candidate = await resume_agent.execute(
        state.resume_text
    )

    state.candidate_profile = candidate

    AuditLogger.log(
        state,
        "Resume Agent",
        "Resume parsed successfully"
    )

    return state


async def job_node(state: WorkflowState):

    job = await job_agent.execute(
        state.job_description
    )

    state.job_profile = job

    AuditLogger.log(
        state,
        "Job Agent",
        "Job description parsed successfully"
    )

    return state


async def match_node(state: WorkflowState):

    match = await match_agent.execute(
        state.candidate_profile,
        state.job_profile
    )

    state.match_result = match

    if "overall_score" in match:
        state.match_score = match["overall_score"]
        state.interview_ready = state.match_score >= 70

    if "confidence" in match:
        state.confidence_score = match["confidence"]

    if "evidence" in match:
        state.evidence = match["evidence"]

    if "recommendation" in match:
        state.recommendation = match["recommendation"]

    AuditLogger.log(
        state,
        "Match Agent",
        "Candidate matched with job successfully"
    )

    return state


async def explainability_node(state: WorkflowState):

    explanation = await explainability_agent.execute(
        state.match_result
    )

    state.explanation = explanation

    if "confidence" in explanation:
        state.confidence_score = explanation["confidence"]

    if "decision" in explanation:
        state.recommendation = explanation["decision"]

    AuditLogger.log(
        state,
        "Explainability Agent",
        "Explainability report generated"
    )

    return state


async def followup_node(state: WorkflowState):

    questions = await followup_agent.execute(
        state.explanation
    )

    state.followup_questions = questions.get(
        "questions",
        []
    )

    AuditLogger.log(
        state,
        "Follow-up Agent",
        "AI follow-up interview questions generated"
    )

    return state