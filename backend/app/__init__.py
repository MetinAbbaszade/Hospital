from app.api.v1.endpoints.auth import router as auth_router
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlmodel import SQLModel


app = FastAPI()
MYSQL_LINK = 'mysql+pymysql://root:M3tin190534@localhost/Hospital'
engine = create_engine(MYSQL_LINK, echo=True)

def create_app():
    app.include_router(router=auth_router)
    return app

def create_db_and_tables():
    SQLModel.metadata.create_all(bind=engine)