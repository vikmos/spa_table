from sqlalchemy import Column, Integer, String, Numeric, Date

from database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    name = Column(String)
    quantity = Column(Integer)
    distance = Column(Numeric)