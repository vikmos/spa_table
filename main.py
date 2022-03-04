"""Серверная часть приложения. Передача данных в JS на index.html
   Получение запросов о фильтре с index.html обработка и формирование
   запросов к БД MySql"""

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def table(request: Request):
    """
    Отображаем страницу с таблицей / домашнюю страницу
    """
    return templates.TemplateResponse("table.html", {
        "request": request
    })

@app.post("/table")
def create_table():
    """
    Создаем таблицу в базе данных
    """
    return {
        "code": "success",
        "message": "table created"
    }