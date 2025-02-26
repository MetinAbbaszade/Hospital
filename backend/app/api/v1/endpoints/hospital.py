from app.api.v1.schemas.hospital import HospitalModel, UpdateHospitalModel
from app.extensions import get_db
from app.models.hospital import Hospital
from app.service import facade
from datetime import datetime
from fastapi import APIRouter, Depends, status, HTTPException
from uuid import uuid4, UUID
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

router = APIRouter(prefix='/api/v1/hospital', tags=['hospital'])

@router.post('/', response_model=HospitalModel, status_code=status.HTTP_201_CREATED)
async def add_hospital(
    Model: HospitalModel,
    session: AsyncSession = Depends(get_db)
):
    existing_email = await facade.get_hospital_by_email(email=Model.email, session=session)
    if existing_email:
        raise HTTPException(
            detail='Hospital has already created',
            status_code=status.HTTP_400_BAD_REQUEST
        )
    
    owner = await facade.get_hospital_owner(owner_id=Model.owner_id, session=session)
    if not owner:
        raise HTTPException(
            detail='Owner not found',
            status_code=status.HTTP_404_NOT_FOUND
        )

    Model.id = uuid4()
    Model.created_at = datetime.now()
    Model.updated_at = datetime.now()

    hospital = await facade.add_hospital(Model=Model, session=session)
    return hospital


@router.get('/', response_model=List[HospitalModel], status_code=status.HTTP_200_OK)
async def get_all_hospitals(
    session: AsyncSession = Depends(get_db)
):
    hospitals = await facade.get_all_hospitals(session=session)
    if not hospitals:
        raise HTTPException(
            detail='Hospitals not found',
            status_code=status.HTTP_400_BAD_REQUEST
        )
    
    data = []
    for hospital in hospitals:
        data.append(hospital)
    return data

@router.get('/{hospital_id}', response_model=HospitalModel, status_code=status.HTTP_200_OK)
async def get_hospital(
    hospital_id: UUID,
    session: AsyncSession = Depends(get_db)):
    hospital = await facade.get_hospital(hospital_id=hospital_id, session=session)
    if not hospital:
        raise HTTPException(
            detail='Hospitals not found',
            status_code=status.HTTP_400_BAD_REQUEST
        )
    return hospital

@router.get('/owner/{owner_id}', response_model=List[HospitalModel], status_code=status.HTTP_200_OK)
async def get_hospital_by_owner(
    owner_id: UUID,
    session: AsyncSession = Depends(get_db)):
    owner = await facade.get_hospital_owner(owner_id=owner_id, session=session)
    if not owner:
        raise HTTPException(
            detail='Owners not found',
            status_code=status.HTTP_400_BAD_REQUEST
        )
    hospitals = await facade.get_hospital_by_owner(owner_id=owner_id, session=session)
    if not hospitals:
        raise HTTPException(
            detail='Hospitals not found',
            status_code=status.HTTP_400_BAD_REQUEST
        )
    
    data = []
    for hospital in hospitals:
        data.append(hospital)
    return data

@router.get('/email/{email}', response_model=HospitalModel, status_code=status.HTTP_200_OK)
async def get_hospital_by_email(
    email: str,
    session: AsyncSession = Depends(get_db)):
    hospital = await facade.get_hospital_by_email(email=email, session=session)
    if not hospital:
        raise HTTPException(
            detail='Hospitals not found',
            status_code=status.HTTP_400_BAD_REQUEST
        )
    return hospital

@router.put('/{hospital_id}', response_model=HospitalModel, status_code=status.HTTP_200_OK)
async def update_hospital(
    hospital_id: UUID,
    Model: UpdateHospitalModel, session: AsyncSession = Depends(get_db)
):
    hospital: Hospital = await facade.get_hospital(hospital_id=hospital_id, session=session)
    if not hospital:
        raise HTTPException(
            detail='Hospitals not found',
            status_code=status.HTTP_400_BAD_REQUEST
        )
    if Model.owner_id and hospital.owner_id != Model.owner_id:
        owner = await facade.get_hospital_owner(owner_id=Model.owner_id, session=session)
        if not owner:
            raise HTTPException(
            detail='Owners not found',
            status_code=status.HTTP_400_BAD_REQUEST
        )
    updated_hospital = await facade.update_hospital(Model=Model, hospital_id=hospital_id, session=session)
    return updated_hospital

@router.delete('/{hospital_id}', response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def delete_hospital(
    hospital_id: UUID,
    session: AsyncSession = Depends(get_db)
):
    hospital = await facade.get_hospital(hospital_id=hospital_id, session=session)
    if not hospital:
        raise HTTPException(
            detail='Hospitals not found',
            status_code=status.HTTP_400_BAD_REQUEST
        )
    
    await facade.delete_hospital(hospital_id=hospital_id, session=session)