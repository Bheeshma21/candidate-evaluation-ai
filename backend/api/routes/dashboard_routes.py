from fastapi import APIRouter, Depends

from auth.dependencies import get_current_user
from database.database import SessionLocal
from repositories.dashboard_repository import DashboardRepository

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/stats")
def dashboard_stats(current_user=Depends(get_current_user)):

    db = SessionLocal()

    try:
        return DashboardRepository.get_stats(db)

    finally:
        db.close()