from app.api.v1.schemas.patienttohospitalcomment import PostPatientToHospitalCommentModel, GetPatientToHospitalCommentModel, UpdatePatientToHospitalCommentModel
from app.extensions import get_db
from app.service import facade
from datetime import datetime
from fastapi import APIRouter, HTTPException, status, Depends
from uuid import UUID, uuid4
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession 

router = APIRouter(prefix='/api/v1/ph_comment', tags=['Comment Was Written to Hospital by Patient'])

@router.post('/', response_model=GetPatientToHospitalCommentModel, status_code=status.HTTP_201_CREATED)
async def create_patient_to_hospital_comment(Model: PostPatientToHospitalCommentModel, session: AsyncSession = Depends(get_db)):
    existing_hospital = await facade.get_hospital(hospital_id=Model.hospital_id, session=session)
    if not existing_hospital:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Hospital not found'
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
    hospitalcomment = await facade.add_ph_comment(Model=Model, session=session)
    return hospitalcomment

@router.get('/', response_model=List[GetPatientToHospitalCommentModel], status_code=status.HTTP_200_OK)
async def get_patient_to_hospital_comments(session: AsyncSession = Depends(get_db)):
    hospitalcomments = await facade.get_all_ph_comments(session=session)
    if not hospitalcomments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is not any comments which are written to hospital by patient'
        )
    data = []
    for hospitalcomment in hospitalcomments:
        data.append(hospitalcomment)
    return data

@router.get('/{hospitalcomment_id}', response_model=GetPatientToHospitalCommentModel, status_code=status.HTTP_200_OK)
async def get_patient_to_hospital_comment(hospitalcomment_id: UUID | str, session: AsyncSession = Depends(get_db)):
    hospitalcomment = await facade.get_ph_comment(patienttohospitalcomment_id=hospitalcomment_id, session=session)
    if not hospitalcomment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There isn't any comment on this id"
        )
    return hospitalcomment

@router.get('/hospital/{hospital_id}', response_model=List[GetPatientToHospitalCommentModel], status_code=status.HTTP_200_OK)
async def get_ph_comment_by_hospital_id(hospital_id: UUID, session: AsyncSession = Depends(get_db)):
    existing_doctor = await facade.get_hospital(hospital_id=hospital_id, session=session)
    if not existing_doctor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Doctor not found'
        )
    
    comments = await facade.get_ph_comment_by_hospital_id(hospital_id=hospital_id, session=session)
    if not comments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There isn't comment on this hospital_id"
        )

    data = []
    for comment in comments:
        data.append(comment)

    return data

@router.get('/patient/{patient_id}', response_model=List[GetPatientToHospitalCommentModel], status_code=status.HTTP_200_OK)
async def get_ph_comment_by_patient_id(patient_id: UUID, session: AsyncSession = Depends(get_db)):
    existing_patient = await facade.get_patient(patient_id=patient_id, session=session)
    if not existing_patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Patient not found'
        )
    
    comments = await facade.get_ph_comment_by_patient_id(patient_id=patient_id, session=session)
    if not comments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There isn't comment on this patient_id"
        )
    data = []
    for comment in comments:
        data.append(comment)

    return data


@router.put('/{hospitalcomment_id}', response_model=GetPatientToHospitalCommentModel, status_code=status.HTTP_200_OK)
async def update_patient_to_hospital_comment(hospitalcomment_id: UUID | str, Model: UpdatePatientToHospitalCommentModel, session: AsyncSession = Depends(get_db)):
    existing_hospitalcomment = await facade.get_ph_comment(patienttohospitalcomment_id=hospitalcomment_id, session=session)
    if not existing_hospitalcomment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is not any comments which are written to hospital by patient'
        )
    if Model.hospital_id and Model.hospital_id != existing_hospitalcomment.hospital_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Hospital_id cannot be changed'
        )
    if Model.patient_id and Model.patient_id != existing_hospitalcomment.patient_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Patient_id cannot be changed'
        )
    hospitalcomment = await facade.update_ph_comment(Model=Model, session=session, patienttohospitalcomment_id=hospitalcomment_id)
    return hospitalcomment

@router.delete('/{hospitalcomment_id}', response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def delete_patient_to_hospital_comment(hospitalcomment_id: UUID | str, session: AsyncSession = Depends(get_db)):
    existing_hospitalcomment = await facade.get_ph_comment(patienttohospitalcomment_id=hospitalcomment_id, session=session)
    if not existing_hospitalcomment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Hospitalcomment not found'
        )
    await facade.delete_ph_comment(patienttohospitalcomment_id=hospitalcomment_id, session=session)
    return None


@router.delete('/hospital/{hospital_id}', response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def delete_ph_comment_by_hospital_id(hospital_id: UUID, session: AsyncSession = Depends(get_db)):
    existing_hospitalcomment = await facade.get_ph_comment_by_hospital_id(hospital_id=hospital_id, session=session)
    if not existing_hospitalcomment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Hospitalcomment not found'
        )
    await facade.delete_ph_comment_by_hospital_id(hospital_id=hospital_id, session=session)
    return None


@router.delete('/patient/{patient_id}', response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def delete_ph_comment_by_patient_id(patient_id: UUID, session: AsyncSession = Depends(get_db)):
    existing_doctorcomment = await facade.get_ph_comment_by_patient_id(patient_id=patient_id, session=session)
    if not existing_doctorcomment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Hospitalcomment not found'
        )
    await facade.delete_ph_comment_by_patient_id(patient_id=patient_id, session=session)
    return None