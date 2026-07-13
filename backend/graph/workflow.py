from langgraph.graph import StateGraph, START, END

from schemas.workflow_state import WorkflowState

from graph.nodes import (
    resume_node,
    job_node,
    match_node,
    explainability_node,
    followup_node,
)

builder = StateGraph(WorkflowState)

# Register Nodes
builder.add_node("resume", resume_node)
builder.add_node("job", job_node)
builder.add_node("match", match_node)
builder.add_node("explainability", explainability_node)
builder.add_node("followup", followup_node)

# Define Flow
builder.add_edge(START, "resume")
builder.add_edge("resume", "job")
builder.add_edge("job", "match")
builder.add_edge("match", "explainability")
builder.add_edge("explainability", "followup")
builder.add_edge("followup", END)

workflow = builder.compile()