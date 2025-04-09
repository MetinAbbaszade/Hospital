from app.api.v1.schemas.hospital import HospitalModel, UpdateHospitalModel
from app.api.v1.schemas.hospitalspecialization import PostHospitalSpecializationModel, GetHospitalSpecializationModel
from app.api.v1.endpoints.patienttohospitalcomment import delete_ph_comment_by_hospital_id
from app.api.v1.endpoints.doctortohospitalcomments import delete_dh_comment_by_hospital_id
from app.extensions import get_db
from app.models.hospital import Hospital
from app.service.hospital import Facade as Hospital_facade
from app.service.owner import Facade as Owner_facade
from app.service.specialities import Facade as Specialities_facade
from app.service.hospitalspecialities import Facade as HS_facade
from datetime import datetime
from fastapi import APIRouter, Depends, status, HTTPException
from uuid import uuid4, UUID
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

router = APIRouter(prefix='/api/v1/hospital', tags=['hospital'])

hospital_facade = Hospital_facade()
owner_facade = Owner_facade()
specialities_facade = Specialities_facade()
hs_facade = HS_facade()

@router.post('/', response_model=HospitalModel, status_code=status.HTTP_201_CREATED)
async def add_hospital(
    Model: HospitalModel,
    session: AsyncSession = Depends(get_db)
):
    existing_email = await hospital_facade.get_hospital_by_email(email=Model.email, session=session)
    if existing_email:
        raise HTTPException(
            detail='Hospital has already created',
            status_code=status.HTTP_400_BAD_REQUEST
        )
    
    owner = await owner_facade.get_hospital_owner(owner_id=Model.owner_id, session=session)
    if not owner:
        raise HTTPException(
            detail='Owner not found',
            status_code=status.HTTP_404_NOT_FOUND
        )

    Model.id = uuid4()
    Model.created_at = datetime.now()
    Model.updated_at = datetime.now()

    for speciality in Model.specialities:
        specialization = await specialities_facade.get_specialization_by_name(name=speciality, session=session)
        if not specialization:
            raise HTTPException(
                detail='Specialization does not exist',
                status_code=status.HTTP_404_NOT_FOUND
            )
        hospital_specialization = PostHospitalSpecializationModel(
            id=None,
            hospital_id=Model.id,
            specialization_id=specialization.id,
            created_at=None,
            updated_at=None
        )
        await hs_facade.add_hospitalspecialization(Model=hospital_specialization, session=session)
    hospital = await hospital_facade.add_hospital(Model=Model, session=session)
    return hospital


@router.get('/', response_model=List[HospitalModel], status_code=status.HTTP_200_OK)
async def get_all_hospitals(
    session: AsyncSession = Depends(get_db)
):
    hospitals = await hospital_facade.get_all_hospitals(session=session)
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
    hospital = await hospital_facade.get_hospital(hospital_id=hospital_id, session=session)
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
    owner = await owner_facade.get_hospital_owner(owner_id=owner_id, session=session)
    if not owner:
        raise HTTPException(
            detail='Owners not found',
            status_code=status.HTTP_400_BAD_REQUEST
        )
    hospitals = await hospital_facade.get_hospital_by_owner(owner_id=owner_id, session=session)
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
    hospital = await hospital_facade.get_hospital_by_email(email=email, session=session)
    if not hospital:
        raise HTTPException(
            detail='Hospitals not found',
            status_code=status.HTTP_400_BAD_REQUEST
        )
    return hospital

@router.get('/specialization/{specialization}', response_model=List[GetHospitalSpecializationModel], status_code=status.HTTP_200_OK)
async def get_hospital_by_specialization(
    specialization,
    session: AsyncSession = Depends(get_db)
):
    hospitals = await hs_facade.get_hospitalspecialization_by_specialization(specialization_id=specialization, session=session)
    if not hospitals:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Hospitals not found'
        )
    data = []
    for hospital in hospitals:
        data.append(hospital)
    return data

@router.put('/{hospital_id}', response_model=HospitalModel, status_code=status.HTTP_200_OK)
async def update_hospital(
    hospital_id: UUID,
    Model: UpdateHospitalModel, session: AsyncSession = Depends(get_db)
):
    hospital: Hospital = await hospital_facade.get_hospital(hospital_id=hospital_id, session=session)
    if not hospital:
        raise HTTPException(
            detail='Hospitals not found',
            status_code=status.HTTP_400_BAD_REQUEST
        )
    if Model.owner_id and hospital.owner_id != Model.owner_id:
        owner = await owner_facade.get_hospital_owner(owner_id=Model.owner_id, session=session)
        if not owner:
            raise HTTPException(
            detail='Owners not found',
            status_code=status.HTTP_400_BAD_REQUEST
        )
    updated_hospital = await hospital_facade.update_hospital(Model=Model, hospital_id=hospital_id, session=session)
    return updated_hospital

@router.delete('/{hospital_id}', response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def delete_hospital(
    hospital_id: UUID,
    session: AsyncSession = Depends(get_db)
):
    hospital = await hospital_facade.get_hospital(hospital_id=hospital_id, session=session)
    if not hospital:
        raise HTTPException(
            detail='Hospitals not found',
            status_code=status.HTTP_400_BAD_REQUEST
        )
    
    # await delete_dh_comment_by_hospital_id(hospital_id=hospital_id, session=session)
    # await delete_ph_comment_by_hospital_id(hospital_id=hospital_id, session=session)
    # await hs_facade.delete_hospitalspecialization_by_hospital(hospital_id=hospital_id, session=session)
    await hospital_facade.delete_hospital(hospital_id=hospital_id, session=session)