from models.interview import Interview


class InterviewRepository:

    @staticmethod
    def create(
        db,
        evaluation,
        interview_date,
        interview_time,
        interviewer,
        meeting_link
    ):

        interview = Interview(

            evaluation_id=evaluation.id,

            candidate_name=evaluation.candidate_name,

            email=(evaluation.candidate_profile.get("email")
            or "bheeshmareddy786@gmail.com"
            ),

            interview_date=interview_date,

            interview_time=interview_time,

            interviewer=interviewer,

            meeting_link=meeting_link
        )

        db.add(interview)
        db.commit()
        db.refresh(interview)

        return interview

    @staticmethod
    def get_all(db):

        return (
            db.query(Interview)
            .order_by(Interview.id.desc())
            .all()
        )

    @staticmethod
    def get_by_id(
        db,
        interview_id
    ):

        return (
            db.query(Interview)
            .filter(Interview.id == interview_id)
            .first()
        )