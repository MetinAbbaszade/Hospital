from app.api.v1.schemas.patienttodoctorcomment import PostPatientToDoctorCommentModel, GetPatientToDoctorCommentModel, UpdatePatientToDoctorCommentModel
from app.extensions import get_db
from app.service import facade
from datetime import datetime
from fastapi import APIRouter, HTTPException, status, Depends
from uuid import UUID, uuid4
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession 

router = APIRouter(prefix='/api/v1/pd_comment', tags=['Comment Was Written to Doctor by Patient'])

@router.post('/', response_model=GetPatientToDoctorCommentModel, status_code=status.HTTP_201_CREATED)
async def create_patient_to_doctor_comment(Model: PostPatientToDoctorCommentModel, session: AsyncSession = Depends(get_db)):
    existing_doctor = await facade.get_doctor(doctor_id=Model.doctor_id, session=session)
    if not existing_doctor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Doctor not found'
        )
    existing_patient = await facade.get_patient(patient_id=Model.patient_id, session=session)
    if not existing_patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Patient not found'
        )
    Model.id = uuid4()
    Model.created_at = datetime.now()
    Model.updated_at = datetime.now()
    doctorcomment = await facade.add_pd_comment(Model=Model, session=session)
    return doctorcomment

@router.get('/', response_model=List[GetPatientToDoctorCommentModel], status_code=status.HTTP_200_OK)
async def get_patient_to_doctor_comments(session: AsyncSession = Depends(get_db)):
    doctorcomments = await facade.get_all_pd_comments(session=session)
    if not doctorcomments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is not any comments which are written by patient to doctor'
        )
    data = []
    for doctorcomment in doctorcomments:
        data.append(doctorcomment)
    return data

@router.get('/{doctorcomment_id}', response_model=GetPatientToDoctorCommentModel, status_code=status.HTTP_200_OK)
async def get_patient_to_doctor_comment(doctorcomment_id: UUID | str, session: AsyncSession = Depends(get_db)):
    doctorcomment = await facade.get_pd_comment(patienttodoctorcomment_id=doctorcomment_id, session=session)
    if not doctorcomment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is not any comments which are written by patient to doctor'
        )
    return doctorcomment

@router.get('/doctor/{doctor_id}', response_model=List[GetPatientToDoctorCommentModel], status_code=status.HTTP_200_OK)
async def get_pd_comment_by_doctor_id(doctor_id: UUID, session: AsyncSession = Depends(get_db)):
    existing_doctor = await facade.get_doctor(doctor_id=doctor_id, session=session)
    if not existing_doctor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Doctor not found'
        )
    
    comments = await facade.get_pd_comment_by_doctor_id(doctor_id=doctor_id, session=session)

    data = []
    for comment in comments:
        data.append(comment)

    return data

@router.get('/patient/{patient_id}', response_model=List[GetPatientToDoctorCommentModel], status_code=status.HTTP_200_OK)
async def get_pd_comment_by_patient_id(patient_id: UUID, session: AsyncSession = Depends(get_db)):
    existing_patient = await facade.get_patient(patient_id=patient_id, session=session)
    if not existing_patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Patient not found'
        )
    
    comments = await facade.get_pd_comment_by_patient_id(patient_id=patient_id, session=session)

    data = []
    for comment in comments:
        data.append(comment)

    return data


@router.put('/{doctorcomment_id}', response_model=GetPatientToDoctorCommentModel, status_code=status.HTTP_200_OK)
async def update_patient_to_doctor_comment(doctorcomment_id: UUID | str, Model: UpdatePatientToDoctorCommentModel, session: AsyncSession = Depends(get_db)):
    existing_doctorcomment = await facade.get_all_patienttodoctorcomments(doctorcomment_id=doctorcomment_id, session=session)
    if not existing_doctorcomment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is not any comments which are written by patient to doctor'
        )
    if Model.doctor_id and Model.doctor_id != existing_doctorcomment.doctor_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Doctor_id cannot be changed'
        )
    if Model.patient_id and Model.patient_id != existing_doctorcomment.patient_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Patient_id cannot be changed'
        )
    doctorcomment = await facade.update_pd_comment(doctorcomment_id=doctorcomment_id, Model=Model, session=session)
    return doctorcomment

@router.delete('/{doctorcomment_id}', response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def delete_patient_to_doctor_comment(doctorcomment_id: UUID | str, session: AsyncSession = Depends(get_db)):
    existing_doctorcomment = await facade.get_pd_comment(doctorcomment_id=doctorcomment_id, session=session)
    if not existing_doctorcomment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Doctorcomment not found'
        )
    await facade.delete_pd_comment(doctorcomment_id=doctorcomment_id, session=session)
    return None


@router.delete('/doctor/{doctor_id}', response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def delete_pd_comment_by_doctor_id(doctor_id: UUID, session: AsyncSession = Depends(get_db)):
    existing_doctorcomment = await facade.get_pd_comment_by_doctor_id(doctor_id=doctor_id, session=session)
    if not existing_doctorcomment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Doctorcomment not found'
        )
    await facade.delete_pd_comment_by_doctor_id(doctor_id=doctor_id, session=session)
    return None


@router.delete('/patient/{patient_id}', response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def delete_pd_comment_by_patient_id(patient_id: UUID, session: AsyncSession = Depends(get_db)):
    existing_doctorcomment = await facade.get_pd_comment_by_patient_id(patient_id=patient_id, session=session)
    if not existing_doctorcomment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Doctorcomment not found'
        )
    await facade.delete_pd_comment_by_patient_id(patient_id=patient_id, session=session)
    return None