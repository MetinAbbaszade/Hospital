from app.api.v1.schemas.hospitalspecialization import GetHospitalSpecializationModel, UpdateHospitalSpecializationModel, PostHospitalSpecializationModel
from app.extensions import get_db
from app.service import facade
from datetime import datetime
from fastapi import APIRouter, status, HTTPException, Depends
from uuid import uuid4, UUID
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List


router = APIRouter(prefix='/api/v1/hospitalspecialization', tags=['HospitalSpecialization'])

@router.post('/', response_model=GetHospitalSpecializationModel, status_code=status.HTTP_201_CREATED)
async def create_hospitalspecialization(Model: PostHospitalSpecializationModel, session: AsyncSession = Depends(get_db)):
    existing_hospital = await facade.get_hospital(hospital_id=Model.hospital_id, session=session)

    if not existing_hospital:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Hospital not found'
        )
    
    Model.id = uuid4()
    Model.created_at = datetime.now()
    Model.updated_at = datetime.now()

    new_relationship = await facade.add_hospitalspecialization(Model=Model, session=session)

    return new_relationship


@router.get('/', response_model=List[GetHospitalSpecializationModel], status_code=status.HTTP_200_OK)
async def get_all_hospitalspecialization(session: AsyncSession = Depends(get_db)):
    relationships = await facade.get_all_hospitalspecialization(session=session)
    if not relationship:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='No Hospital Specialization Found'
        )
    data = []
    for relationship in relationships:
        data.append(relationship)

    return data

@router.get('/{hospitalspecialization_id}', response_model=GetHospitalSpecializationModel, status_code=status.HTTP_200_OK)
async def get_hospitalspecialization(hospitalspecialization_id: UUID, session: AsyncSession = Depends(get_db)):
    relationship = await facade.get_hospitalspecialization(hospitalspecialization_id=hospitalspecialization_id, session=session)
    if not relationship:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Hospital Specialization Not Found'
        )
    return relationship

@router.put('/{hospitalspecialization_id}', response_model=GetHospitalSpecializationModel, status_code=status.HTTP_200_OK)
async def update_hospitalspecialization(hospitalspecialization_id: UUID, Model: UpdateHospitalSpecializationModel, session: AsyncSession = Depends(get_db)):
    existing_relationship = await facade.get_hospitalspecialization(hospitalspecialization_id=hospitalspecialization_id, session=session)
    if not existing_relationship:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Hospital Specialization Not Found'
        )
    if existing_relationship.hospital_id != Model.hospital_id and Model.hospital_id:
        existing_hospital = facade.get_hospital(hospital_id=Model.hospital_id, session=session)
        if not existing_hospital:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Hospital Not Found'
            )
    if existing_relationship.specialization_id != Model.specialization_id and Model.specialization_id:
        existing_specialization = facade.get_specialization(specialization_id=Model.specialization_id, session=session)
        if not existing_specialization:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Specialization Not Found'
            )
    
    updated_relationship = await facade.update_hospitalspecialization(hospitalspecialization_id=hospitalspecialization_id, Model=Model, session=session)
    return updated_relationship

@router.delete('/{hospitalspecialization_id}', response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def delete_hospitalspecialization(hospitalspecialization_id: UUID, session: AsyncSession = Depends(get_db)):
    existing_relationship = await facade.get_hospitalspecialization(hospitalspecialization_id=hospitalspecialization_id, session=session)
    if not existing_relationship:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Doctor Specialization Not Found'
        )
    await facade.delete_hospitalspecialization(hospitalspecialization_id=hospitalspecialization_id, session=session)
    return None