"""Серверная часть приложения. Передача данных в JS на index.html
   Получение запросов о фильтре с index.html обработка и формирование
   запросов к БД MySql"""

from pydantic import BaseModel
import models
from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from pydantic import BaseModel
from models import Product

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

class TableRequest(BaseModel):
    symbol: str

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def table(request: Request, db: Session = Depends(get_db)):
    """
    Отображаем страницу с таблицей / домашнюю страницу
    """
    products = db.query(Product).all()


    return templates.TemplateResponse("table.html", {
        "request": request,
        "products": products
    })