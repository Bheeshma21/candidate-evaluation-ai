from fastapi import FastAPI
from api.interview_routes import router as interview_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from api.email_routes import router as email_router
from api.routes.auth_routes import router as auth_router
from api.routes.dashboard_routes import router as dashboard_router
try:
    from api.routes.voice_routes import router as voice_router
except:
    voice_router = None
from api.routes.evaluation_routes import router as evaluation_router
from api.interview_routes import router as interview_router
from api.routes.interview_evaluation_routes import (
    router as interview_evaluation_router
)
from api.resume_routes import router as resume_router
from api.job_routes import router as job_router
from api.match_ai_routes import router as match_ai_router

from database.database import Base, engine

import database.models
import models.evaluation
import models.interview_evaluation
import models.interview_model

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Candidate Evaluation AI",
    version="1.0.0"
)

app.mount(
    "/static",
    StaticFiles(directory="frontend/static"),
    name="static"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:8501",
        "http://localhost:8501"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def home():
    return FileResponse(
        "frontend/templates/index.html"
    )
@app.get("/interview")
async def interview():
    return FileResponse(
        "frontend/templates/interview.html"
    )


app.include_router(interview_router)
app.include_router(email_router)
app.include_router(auth_router)
app.include_router(dashboard_router)
if voice_router:
    app.include_router(voice_router) 
app.include_router(evaluation_router)
app.include_router(interview_router)
app.include_router(interview_evaluation_router)
app.include_router(resume_router)
app.include_router(job_router)
app.include_router(match_ai_router)