from database.database import Base, engine

# Import ALL database models
import database.models

from models.interview_evaluation import InterviewEvaluation
from models.evaluation import Evaluation
from models.interview import Interview


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
    print("✅ Database initialized successfully.")