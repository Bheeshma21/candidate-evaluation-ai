from database.database import SessionLocal
from repositories.candidate_repository import CandidateRepository
from repositories.job_repository import JobRepository

db = SessionLocal()

candidate = CandidateRepository.get_by_id(db, 1)
job = JobRepository.get_by_id(db, 1)
    
print(candidate.name)
print(job.title)

db.close()