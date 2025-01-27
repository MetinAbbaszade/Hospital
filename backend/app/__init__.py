from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlmodel import SQLModel


app = FastAPI()
MYSQL_LINK = 'mysql://root:M3tin190534@localhost/Hospital'
engine = create_engine(MYSQL_LINK, echo=True)

def create_app():
    return app

def create_db_and_tables():
    SQLModel.metadata.create_all(bind=engine)