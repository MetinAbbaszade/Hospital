from app.api.v1.schemas.appointment import PostAppointmentModel, GetAppointmentModel, UpdateAppointmentModel
from app.api.v1.endpoints.doctortoappointcomment import delete_da_comment_by_appoint_id
from app.api.v1.endpoints.patienttoappointcomment import delete_pa_comment_by_appoint_id
from app.extensions import get_db
from app.models.appointment import Appointment
from app.service.appointment import Facade as Appoint_facade
from app.service.doctor import Facade as Doctor_facade
from app.service.patient import Facade as Patient_facade
from datetime import datetime
from fastapi import APIRouter, HTTPException, status, Depends
from uuid import uuid4, UUID
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

appoint_facade = Appoint_facade()
doctor_facade = Doctor_facade()
patient_facade = Patient_facade()


router = APIRouter(prefix="/api/v1/appointment", tags=['Appointment'])

@router.post("/", response_model=GetAppointmentModel, status_code=status.HTTP_201_CREATED)
async def create_appoint(
    Model: PostAppointmentModel,
    session: AsyncSession = Depends(get_db)
    ):
    doctor_id = Model.doctor_id
    patient_id = Model.patient_id
    existing_doctor = await doctor_facade.get_doctor(doctor_id=doctor_id, session=session)

    if not existing_doctor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Doctor Not Found'
        )
    
    existing_patient = await patient_facade.get_patient(patient_id=patient_id, session=session)

    if not existing_patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Patient Not Found'
        )
    
    Model.id = uuid4()
    Model.created_at = datetime.now()
    Model.updated_at = datetime.now()

    appoint = await appoint_facade.add_appointment(Model=Model, session=session)

    return appoint

@router.get("/", response_model=List[GetAppointmentModel], status_code=status.HTTP_200_OK)
async def get_all_appoints(
    session: AsyncSession = Depends(get_db)
):
    appoints = await appoint_facade.get_all_appointments(session=session)
    if not appoints:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Appoints not found"
        )
    data = []
    for appoint in appoints:
        data.append(appoint)
    return data

@router.get("/{appoint_id}", response_model=GetAppointmentModel, status_code=status.HTTP_200_OK)
async def get_appoint(
    appoint_id: UUID,
    session: AsyncSession = Depends(get_db)
    ):
    appoint = await appoint_facade.get_appointment(appointment_id=appoint_id, session=session)

    if not appoint:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Appoint not found"
        )
    return appoint

@router.get("/doctor/{doctor_id}", response_model=List[GetAppointmentModel], status_code=status.HTTP_200_OK)
async def get_appoint_by_doctor(
    doctor_id: UUID,
    session: AsyncSession = Depends(get_db)
    ):
    doctor = await doctor_facade.get_doctor(doctor_id=doctor_id, session=session)
    if not doctor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Doctor not found"
        )
    appoints = await appoint_facade.get_appointment_by_doctor(doctor_id=doctor_id, session=session)
    if not appoints:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Appoints not found"
        )
    data = []
    for appoint in appoints:
        data.append(appoint)
    return data

@router.get("/patient/{patient_id}", response_model=List[GetAppointmentModel], status_code=status.HTTP_200_OK)
async def get_appoint_by_patient(
    patient_id: UUID,
    session: AsyncSession = Depends(get_db)
    ):
    patient = await patient_facade.get_patient(patient_id=patient_id, session=session)
    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found"
        )
    appoints = await appoint_facade.get_appointment_by_patient(patient_id=patient_id, session=session)
    if not appoints:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Appoints not found"
        )
    data = []
    for appoint in appoints:    
        data.append(appoint)
    return data

@router.get("/datetime", response_model=List[GetAppointmentModel], status_code=status.HTTP_200_OK)
async def get_appoint_by_datetime(
    datetime: datetime,
    session: AsyncSession = Depends(get_db)
):
    appoints = await appoint_facade.get_appointment_by_datetime(datetime=datetime, session=session)
    if not appoints:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Appoints not found"
        )
    data = []
    for appoint in appoints:
        data.append(appoint)
    return data

@router.put("/appoint_id", response_model=GetAppointmentModel, status_code=status.HTTP_200_OK)
async def update_full_appoint(
    appoint_id: UUID,
    Model: UpdateAppointmentModel,
    session: AsyncSession = Depends(get_db)
    ):
    existing_appoint: Appointment = await appoint_facade.get_appointment(appointment_id=appoint_id, session=session)
    if not existing_appoint:
        raise HTTPException(
            detail='Appoint not found',
            status_code=status.HTTP_404_NOT_FOUND
        )
    if existing_appoint['doctor_id'] != Model.doctor_id and Model.doctor_id:
        existing_doctor = await doctor_facade.get_doctor(doctor_id=Model.doctor_id, session=session)
        if not existing_doctor:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Doctor Not Found'
            )
        
    if existing_appoint['patient_id'] != Model.patient_id and Model.patient_id:
        existing_patient = await patient_facade.get_patient(patient_id=Model.patient_id, session=session)
        if not existing_patient:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Patient Not Found'
            )
    
    appoint = await appoint_facade.update_appointment(appointment_id=appoint_id, Model=Model, session=session)
    return appoint


@router.delete("/appoint_id", response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def delete_appoint(
    appoint_id: UUID,
    session: AsyncSession = Depends(get_db)
):
    appoint = await appoint_facade.get_appointment(appointment_id=appoint_id, session=session)

    if not appoint:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Appoint not found"
        )
    await delete_da_comment_by_appoint_id(appoint_id=appoint_id, session=session)
    await delete_pa_comment_by_appoint_id(appoint_id=appoint_id, session=session)
    await appoint_facade.delete_appointment(appointment_id=appoint_id, session=session)