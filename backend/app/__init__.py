from app.api.v1.endpoints.auth import router as auth_router
from app.api.v1.endpoints.admin import router as admin_router
from app.api.v1.endpoints.patient import router as patient_router
from app.api.v1.endpoints.doctor import router as doctor_router
from app.api.v1.endpoints.hospital import router as hospital_router
from app.api.v1.endpoints.owner import router as owner_router
from app.api.v1.endpoints.appointment import router as appointment_router
from app.api.v1.endpoints.specialization import router as specialization_router
from app.api.v1.endpoints.doctorspecialization import router as doctorspecialization_router
from app.api.v1.endpoints.patienttodoctorcomment import router as pd_comment_router
from app.api.v1.endpoints.doctortoappointcomment import router as da_comment_router
from app.api.v1.endpoints.patienttoappointcomment import router as pa_comment_router
from app.api.v1.endpoints.patienttohospitalcomment import router as ph_comment_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlmodel import SQLModel


app = FastAPI()
MYSQL_LINK = 'mysql+pymysql://root:M3tin190534@localhost/Hospital'
engine = create_engine(MYSQL_LINK, echo=True)

def create_app():

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(router=auth_router)
    app.include_router(router=admin_router)
    app.include_router(router=patient_router)
    app.include_router(router=doctor_router)
    app.include_router(router=hospital_router)
    app.include_router(router=owner_router)
    app.include_router(router=appointment_router)
    app.include_router(router=specialization_router)
    app.include_router(router=doctorspecialization_router)
    app.include_router(router=pd_comment_router)
    app.include_router(router=da_comment_router)
    app.include_router(router=pa_comment_router)
    app.include_router(router=ph_comment_router)
    return app

def create_db_and_tables():
    SQLModel.metadata.create_all(bind=engine)