"""Серверная часть приложения. Передача данных в JS на index.html
   Получение запросов о фильтре с index.html обработка и формирование
   запросов к БД MySql"""

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
def table(request: Request, db: Session = Depends(get_db), name = None, operation = None, argument = None):
    """
    Отображаем страницу с таблицей / домашнюю страницу
    """
    products = db.query(Product)
    """
    output_products = db.query(Product)
    products = []
    
    for i in range (10):
        products.append(output_products[i])
    print(len(products))
    """


    if name == '0' and operation == '0':
        products = products.filter(Product.name == argument)
    elif name == '0' and operation == '1':
        products = products.filter(Product.name.like(f"%{argument}%"))
    elif name == '1' and operation == '0':
        products = products.filter(Product.quantity == argument)
    elif name == '1' and operation == '2':
        products = products.filter(Product.quantity > argument)
    elif name == '1' and operation == '3':
        products = products.filter(Product.quantity < argument)
    elif name == '2' and operation == '0':
        products = products.filter(Product.distance == argument)
    elif name == '2' and operation == '2':
        products = products.filter(Product.distance > argument)
    elif name == '2' and operation == '3':
        products = products.filter(Product.distance < argument)   

    
    return templates.TemplateResponse("table.html", {
        "request": request,
        "products": products
    })