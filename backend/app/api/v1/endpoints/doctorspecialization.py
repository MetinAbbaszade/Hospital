from app.api.v1.schemas.doctorspecialization import PostDoctorSpecializationModel, UpdateDoctorSpecializationModel, GetDoctorSpecializationModel
from app.extensions import get_db
from app.service.doctorspecialities import Facade as Doctorspecialization_facade
from app.service.doctor import Facade as Doctor_facade
from app.service.specialities import Facade as Specialization_facade
from datetime import datetime
from fastapi import APIRouter, status, HTTPException, Depends
from uuid import uuid4, UUID
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List


doctorspecialization_facade = Doctorspecialization_facade()
doctor_facade = Doctor_facade()
specialization_facade = Specialization_facade()


router = APIRouter(prefix='/api/v1/doctorspecialization', tags=['DoctorSpecialization'])

@router.post('/', response_model=GetDoctorSpecializationModel, status_code=status.HTTP_201_CREATED)
async def create_doctorspecialization(Model: PostDoctorSpecializationModel, session: AsyncSession = Depends(get_db)):
    doctor_id = Model.doctor_id
    existing_doctor = await doctor_facade.get_doctor(doctor_id=doctor_id, session=session)

    if not existing_doctor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Doctor not found'
        )
    
    Model.id = uuid4()
    Model.created_at = datetime.now()
    Model.updated_at = datetime.now()

    new_relationship = await doctorspecialization_facade.add_doctorspecialization(Model=Model, session=session)

    return new_relationship


@router.get('/', response_model=List[GetDoctorSpecializationModel], status_code=status.HTTP_200_OK)
async def get_all_doctorspecialization(session: AsyncSession = Depends(get_db)):
    relationships = await doctorspecialization_facade.get_all_doctorspecializations(session=session)
    if not relationship:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='No Doctor Specialization Found'
        )
    data = []
    for relationship in relationships:
        data.append(relationship)

    return data

@router.get('/{doctorspecialization_id}', response_model=GetDoctorSpecializationModel, status_code=status.HTTP_200_OK)
async def get_doctorspecialization(doctorspecialization_id: UUID, session: AsyncSession = Depends(get_db)):
    relationship = await doctorspecialization_facade.get_doctorspecialization(doctorspecialization_id=doctorspecialization_id, session=session)
    if not relationship:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Doctor Specialization Not Found'
        )
    return relationship

@router.put('/{doctorspecialization_id}', response_model=GetDoctorSpecializationModel, status_code=status.HTTP_200_OK)
async def update_doctorspecialization(doctorspecialization_id: UUID, Model: UpdateDoctorSpecializationModel, session: AsyncSession = Depends(get_db)):
    existing_relationship = await doctorspecialization_facade.get_doctorspecialization(doctorspecialization_id=doctorspecialization_id, session=session)
    if not existing_relationship:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Doctor Specialization Not Found'
        )
    if existing_relationship.doctor_id != Model.doctor_id and Model.doctor_id:
        existing_doctor = doctor_facade.get_doctor(doctor_id=Model.doctor_id, session=session)
        if not existing_doctor:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Doctor Not Found'
            )
    if existing_relationship.specialization_id != Model.specialization_id and Model.specialization_id:
        existing_specialization = specialization_facade.get_specialization(specialization_id=Model.specialization_id, session=session)
        if not existing_specialization:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Specialization Not Found'
            )
    
    updated_relationship = await doctorspecialization_facade.update_doctorspecialization(doctorspecialization_id=doctorspecialization_id, Model=Model, session=session)
    return updated_relationship

@router.delete('/{doctorspecialization_id}', response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def delete_doctorspecialization(doctorspecialization_id: UUID, session: AsyncSession = Depends(get_db)):
    existing_relationship = await doctorspecialization_facade.get_doctorspecialization(doctorspecialization_id=doctorspecialization_id, session=session)
    if not existing_relationship:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Doctor Specialization Not Found'
        )
    await doctorspecialization_facade.delete_doctorspecialization(doctorspecialization_id=doctorspecialization_id, session=session)
    return None