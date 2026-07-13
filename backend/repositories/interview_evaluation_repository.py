from models.interview_evaluation import InterviewEvaluation


class InterviewEvaluationRepository:

    @staticmethod
    def create(
        db,
        interview_id,
        evaluation
    ):

        interview_evaluation = InterviewEvaluation(

            interview_id=interview_id,

            technical_score=evaluation.get(
                "technical_score",
                0
            ),

            communication_score=evaluation.get(
                "communication_score",
                0
            ),

            problem_solving_score=evaluation.get(
                "problem_solving_score",
                0
            ),

            confidence_score=evaluation.get(
                "confidence_score",
                0
            ),

            final_score=evaluation.get(
                "final_score",
                0
            ),

            recommendation=evaluation.get(
                "recommendation",
                ""
            ),

            strengths=evaluation.get(
                "strengths",
                []
            ),

            weaknesses=evaluation.get(
                "weaknesses",
                []
            ),

            summary=evaluation.get(
                "summary",
                ""
            )
        )

        db.add(interview_evaluation)
        db.commit()
        db.refresh(interview_evaluation)

        return interview_evaluation

    @staticmethod
    def get_all(db):

        return (
            db.query(InterviewEvaluation)
            .order_by(
                InterviewEvaluation.id.desc()
            )
            .all()
        )

    @staticmethod
    def get_by_interview(
        db,
        interview_id
    ):

        return (
            db.query(InterviewEvaluation)
            .filter(
                InterviewEvaluation.interview_id == interview_id
            )
            .first()
        )