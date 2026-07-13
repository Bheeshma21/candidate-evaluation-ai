from sqlalchemy import func

from models.evaluation import Evaluation


class DashboardRepository:

    @staticmethod
    def get_stats(db):

        total = db.query(Evaluation).count()

        avg_match = (
            db.query(func.avg(Evaluation.match_score))
            .scalar()
            or 0
        )

        avg_confidence = (
            db.query(func.avg(Evaluation.confidence_score))
            .scalar()
            or 0
        )

        recommendations = db.query(Evaluation).all()

        recommendation_counts = {}

        for item in recommendations:

            key = item.recommendation or "Unknown"

            recommendation_counts[key] = (
                recommendation_counts.get(key, 0) + 1
            )

        return {

            "total_evaluations": total,

            "average_match_score": round(
                avg_match,
                2
            ),

            "average_confidence_score": round(
                avg_confidence,
                2
            ),

            "recommendations": recommendation_counts
        }