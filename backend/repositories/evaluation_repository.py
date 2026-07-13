from models.evaluation import Evaluation


class EvaluationRepository:

    @staticmethod
    def create(db, state: dict):

        evaluation = Evaluation(

            candidate_name=state.get(
                "candidate_profile",
                {}
            ).get(
                "name",
                "Unknown Candidate"
            ),

            job_title=state.get(
                "job_profile",
                {}
            ).get(
                "title",
                "Unknown Job"
            ),

            match_score=state.get(
                "match_score",
                0.0
            ),

            confidence_score=state.get(
                "confidence_score",
                0.0
            ),

            recommendation=state.get(
                "recommendation"
            ),

            recruiter_decision=None,
            recruiter_notes=None,

            candidate_profile=state.get(
                "candidate_profile",
                {}
            ),

            job_profile=state.get(
                "job_profile",
                {}
            ),

            match_result=state.get(
                "match_result",
                {}
            ),

            explanation=state.get(
                "explanation",
                {}
            ),

            followup_questions=state.get(
                "followup_questions",
                []
            ),

            audit_log=[
                entry.model_dump()
                if hasattr(entry, "model_dump")
                else entry
                for entry in state.get(
                    "audit_log",
                    []
                )
            ]
        )

        db.add(evaluation)
        db.commit()
        db.refresh(evaluation)

        return evaluation

    @staticmethod
    def get_all(db):

        return (
            db.query(Evaluation)
            .order_by(Evaluation.id.desc())
            .all()
        )

    @staticmethod
    def get_by_id(db, evaluation_id: int):

        return (
            db.query(Evaluation)
            .filter(Evaluation.id == evaluation_id)
            .first()
        )

    @staticmethod
    def update_decision(
        db,
        evaluation_id: int,
        decision: str,
        notes: str = ""
    ):

        evaluation = (
            db.query(Evaluation)
            .filter(Evaluation.id == evaluation_id)
            .first()
        )

        if evaluation is None:
            return None

        evaluation.recruiter_decision = decision
        evaluation.recruiter_notes = notes

        db.commit()
        db.refresh(evaluation)

        return evaluation

    @staticmethod
    def delete(db, evaluation_id: int):

        evaluation = (
            db.query(Evaluation)
            .filter(Evaluation.id == evaluation_id)
            .first()
        )

        if evaluation is None:
            return None

        db.delete(evaluation)
        db.commit()

        return evaluation