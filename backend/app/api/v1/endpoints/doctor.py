from app.api.v1.schemas.doctor import GetDoctorModel, PostDoctorModel, UpdateDoctorModel
from app.api.v1.schemas.user import UserModel
from app.api.v1.schemas.hospital import HospitalModel
from app.models.doctor import  Doctor
from app.extensions import get_db
from app.service import facade
from datetime import datetime
from fastapi import APIRouter, Depends, status, HTTPException
from uuid import uuid4, UUID
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

router = APIRouter(prefix='/api/v1/doctor', tags=['doctor'])

@router.post('/', response_model=UserModel, status_code=status.HTTP_201_CREATED)
async def add_doctor(
    Model: PostDoctorModel,
    session: AsyncSession = Depends(get_db)
    ):
    existing_email = await facade.get_user_by_email(email=Model.email, session=session)

    if existing_email:
        raise HTTPException(
            detail='Email has already signed up',
            status_code=status.HTTP_400_BAD_REQUEST
        )
    
    existing_hospital = await facade.get_hospital(hospital_id=Model.hospital_id, session=session)
    if not existing_hospital:
        raise HTTPException(
            detail='Hospital does not exist',
            status_code=status.HTTP_404_NOT_FOUND
        )
    
    Model.id = uuid4()
    Model.created_at = datetime.now()
    Model.updated_at = datetime.now()

    user = await facade.add_user(Model=Model, session=session)
    await facade.add_doctor(Model=Model, session=session)

    return user

@router.get('/', response_model=List[GetDoctorModel], status_code=status.HTTP_200_OK)
async def get_all_doctors(
    session: AsyncSession = Depends(get_db)
    ):
    doctors: List[GetDoctorModel] = await facade.get_all_doctors(session=session)

    if not doctors:
        raise HTTPException(
            detail='Doctors not found',
            status_code=status.HTTP_404_NOT_FOUND
        )
    data = []
    for doctor in doctors:
        data.append(doctor)
    return data


@router.get('/{doctor_id}', response_model=GetDoctorModel, status_code=status.HTTP_200_OK)
async def get_doctor(
    doctor_id: UUID, 
    session: AsyncSession = Depends(get_db)
    ):
    doctor: GetDoctorModel = await facade.get_doctor(doctor_id=doctor_id, session=session)

    if not doctor:
        raise HTTPException(
            detail='Doctor not found',
            status_code=status.HTTP_404_NOT_FOUND
        )
    return doctor

@router.get('/hospital/{hospital_id}', response_model=List[GetDoctorModel], status_code=status.HTTP_200_OK)
async def get_doctor_by_hospital(
    hospital_id: UUID, 
    session: AsyncSession = Depends(get_db)
    ):
    hospital: HospitalModel = await facade.get_hospital(hospital_id=hospital_id, session=session)
    print(hospital)
    if not hospital:
        raise HTTPException(
            detail='Hospital not found',
            status_code=status.HTTP_404_NOT_FOUND
        )
    doctors = await facade.get_doctor_by_hospital(hospital_id=hospital_id, session=session)
    print(doctors)
    if doctors is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Doctors not found'
        )
    data = []
    for doctor in doctors:
        data.append(doctor)
    return data


@router.put('/{doctor_id}', response_model=GetDoctorModel, status_code=status.HTTP_200_OK)
async def update_doctor(
    doctor_id: UUID,
    Model: UpdateDoctorModel,
    session: AsyncSession = Depends(get_db)
    ):
    doctor: GetDoctorModel = await facade.get_doctor(doctor_id=doctor_id, session=session)

    if not doctor:
        raise HTTPException(
            detail='Doctor not found',
            status_code=status.HTTP_404_NOT_FOUND
        )

    if Model.hospital_id != doctor.hospital_id and Model.hospital_id:
        hospital = await facade.get_hospital(hospital_id=Model.hospital_id, session=session)
        if not hospital:
            raise HTTPException(
                detail='Hospital not found',
                status_code=status.HTTP_404_NOT_FOUND
            )
    updated_doctor = await facade.update_doctor(Model=Model, doctor_id=doctor_id, session=session)
    return updated_doctor

@router.delete('/{doctor_id}', response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def delete_doctor(
    doctor_id: UUID,
    session: AsyncSession = Depends(get_db)
    ):
    doctor: GetDoctorModel = await facade.get_doctor(doctor_id=doctor_id, session=session)

    if not doctor:
        raise HTTPException(
            detail='Doctor not found',
            status_code=status.HTTP_404_NOT_FOUND
        )
    await facade.delete_doctor(doctor_id=doctor_id, session=session)
    await facade.delete_user(user_id=doctor_id, session=session)