from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import secrets

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{secrets.dbuser}:{secrets.dbpass}@{secrets.dbhost}/{secrets.dbname}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

engine.connect()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
