from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class AuditEntry(BaseModel):
    timestamp: str
    step: str
    message: str


class WorkflowState(BaseModel):
    """
    Shared state between all AI agents.
    Every agent reads from and writes to this object.
    """

    # Uploaded data
    resume_text: Optional[str] = None
    job_description: Optional[str] = None
    interview_text: Optional[str] = None

    # Parsed information
    candidate_profile: Dict[str, Any] = Field(default_factory=dict)
    job_profile: Dict[str, Any] = Field(default_factory=dict)

    # Matching
    match_result: Dict[str, Any] = Field(default_factory=dict)
    explanation: Dict[str, Any] = Field(default_factory=dict)

    match_score: float = 0.0
    interview_ready: bool = False
    confidence_score: float = 0.0

    # Explainability
    evidence: List[str] = Field(default_factory=list)

    # Follow-up Questions
    followup_questions: List[Dict[str, Any]] = Field(default_factory=list)

    # Recommendation
    recommendation: Optional[str] = None

    # Human Approval
    recruiter_decision: Optional[str] = None

    # Audit Trail
    audit_log: List[AuditEntry] = Field(default_factory=list)