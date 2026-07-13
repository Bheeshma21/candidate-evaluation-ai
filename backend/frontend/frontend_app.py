from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="frontend/static"),
    name="static"
)

templates = Jinja2Templates(
    directory="frontend/templates"
)


@app.get("/")
async def home():
    return FileResponse("frontend/templates/index.html")


@app.get("/interview")
async def interview():
    return FileResponse("frontend/templates/interview.html")