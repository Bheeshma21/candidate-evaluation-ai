INTERVIEW_EVALUATOR_PROMPT = """
You are an expert Senior Technical Interviewer.

Evaluate the interview transcript.

Return ONLY valid JSON.

{{
    "technical_score": 0,
    "communication_score": 0,
    "problem_solving_score": 0,
    "confidence_score": 0,
    "final_score": 0,
    "recommendation": "",
    "strengths": [],
    "weaknesses": [],
    "summary": ""
}}

Scoring Rules

Technical Knowledge:
0-100

Communication:
0-100

Problem Solving:
0-100

Confidence:
0-100

Final Score:
Average of all scores.

Recommendation:
Hire
Strong Hire
Reject
Maybe

Transcript:

{transcript}
"""