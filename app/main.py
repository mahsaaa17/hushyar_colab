from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from hooshyar.app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)
templates = Jinja2Templates(directory="hooshyar/app/templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})