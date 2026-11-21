from fastapi import FastAPI
from fastapi import Request, Response
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI(title="MyFastApi", version="0.1.0", description="description")

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

""" Эндпоинт Главной Страницы """

@app.get("/")
def page_1(request: Request):
    return templates.TemplateResponse(request, "page_1.html")