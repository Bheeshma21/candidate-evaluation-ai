from models.candidate_profile import CandidateProfile
from models.job_profile import JobProfile
from models.match_result import MatchResult


class MatchingService:

    @staticmethod
    def match(
        candidate: CandidateProfile,
        job: JobProfile,
    ) -> MatchResult:

        candidate_skills = {
            skill.lower()
            for skill in candidate.skills
        }

        required_skills = {
            skill.lower()
            for skill in job.required_skills
        }

        matched = sorted(candidate_skills.intersection(required_skills))
        missing = sorted(required_skills - candidate_skills)

        if required_skills:
            skill_score = round(
                (len(matched) / len(required_skills)) * 100,
                2
            )
        else:
            skill_score = 100.0

        experience_score = 100.0
        education_score = 100.0
        technology_score = skill_score

        overall_score = round(
            (
                skill_score +
                experience_score +
                education_score +
                technology_score
            ) / 4,
            2
        )

        confidence = overall_score

        interview_ready = overall_score >= 70

        if overall_score >= 85:
            recommendation = "Strong Hire"
        elif overall_score >= 70:
            recommendation = "Hire"
        elif overall_score >= 50:
            recommendation = "Consider"
        else:
            recommendation = "Reject"

        evidence = [
            f"Matched {len(matched)} of {len(required_skills)} required skills."
        ]

        return MatchResult(
            overall_score=overall_score,
            recommendation=recommendation,
            interview_ready=interview_ready,
            confidence=confidence,
            skill_score=skill_score,
            experience_score=experience_score,
            education_score=education_score,
            technology_score=technology_score,
            matched_skills=matched,
            missing_skills=missing,
            evidence=evidence,
        )