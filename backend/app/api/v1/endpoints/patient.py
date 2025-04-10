from app.api.v1.schemas.patient import PostPatientModel, GetPatientModel, UpdatePatientModel
from app.api.v1.schemas.user import UserModel
from app.api.v1.endpoints.patienttodoctorcomment import delete_pd_comment_by_patient_id
from app.api.v1.endpoints.patienttoappointcomment import delete_pa_comment_by_patient_id
from app.api.v1.endpoints.patienttohospitalcomment import delete_ph_comment_by_patient_id
from app.extensions import get_db
from app.models.user import User
from app.service.patient import Facade as Patient_facade
from app.service.user import Facade as User_facade
from datetime import datetime
from fastapi import APIRouter, Depends, status, HTTPException
from uuid import uuid4, UUID
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

router = APIRouter(prefix='/api/v1/patient', tags=['patient'])
patient_facade = Patient_facade()
user_facade = User_facade()

@router.post('/', response_model=UserModel, status_code=status.HTTP_201_CREATED)
async def add_patient(
    Model: PostPatientModel,
    session: AsyncSession = Depends(get_db)
):
    existing_user: User = await user_facade.get_user_by_email(email=Model.email,session=session)
    if existing_user:
        raise HTTPException(
            detail='Email has already signed up',
            status_code=status.HTTP_400_BAD_REQUEST
        )
    
    Model.id = uuid4()
    Model.created_at = datetime.now()
    Model.updated_at = datetime.now()
    
    new_user = await user_facade.add_user(Model=Model, session=session)
    await patient_facade.add_patient(Model=Model, session=session)
    return new_user

@router.get('/', response_model=List[GetPatientModel], status_code=status.HTTP_200_OK)
async def get_all_patients(
    session: AsyncSession = Depends(get_db)
):
    patients: List[GetPatientModel] = await patient_facade.get_all_patients(session=session)

    if not patients:
        raise HTTPException(
            detail='Patients not found',
            status_code=status.HTTP_404_NOT_FOUND
        )
    data = []
    for patient in patients:
        data.append(patient)
    return data

@router.get('/{patient_id}', response_model=GetPatientModel, status_code=status.HTTP_200_OK)
async def get_patient(
    patient_id: UUID,
    session: AsyncSession = Depends(get_db)
):
    patient: GetPatientModel = await patient_facade.get_patient(patient_id=patient_id, session=session)

    if not patient:
        raise HTTPException(
            detail='Patient not found',
            status_code=status.HTTP_404_NOT_FOUND
        )
    return patient

@router.put('/{patient_id}', response_model=GetPatientModel, status_code=status.HTTP_200_OK)
async def update_patient(
    patient_id: UUID,
    Model: UpdatePatientModel,
    session: AsyncSession = Depends(get_db)
):
    patient: GetPatientModel = await patient_facade.get_patient(patient_id=patient_id, session=session)

    if not patient:
        raise HTTPException(
            detail='Patient not found',
            status_code=status.HTTP_404_NOT_FOUND
        )
    updated_patient = await patient_facade.update_patient(Model=Model, patient_id=patient_id, session=session)
    return updated_patient

@router.delete('/{patient_id}', response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def delete_patient(
    patient_id: UUID,
    session: AsyncSession = Depends(get_db)
):
    patient: GetPatientModel = await patient_facade.get_patient(patient_id=patient_id, session=session)
    if not patient:
        raise HTTPException(
            detail='Patient not found',
            status_code=status.HTTP_404_NOT_FOUND
        )
    # await delete_pd_comment_by_patient_id(patient_id=patient_id, session=session)
    # await delete_pa_comment_by_patient_id(patient_id=patient_id, session=session)
    # await delete_ph_comment_by_patient_id(patient_id=patient_id, session=session)
    await patient_facade.delete_patient(patient_id=patient_id, session=session)
    await user_facade.delete_user(user_id=patient_id, session=session)