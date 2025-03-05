from fastapi import APIRouter
from app.api.v1.schemas.patienttoappointcomment import GetPatientToAppointCommentModel, UpdatePatientToAppointCommentModel, PostPatientToAppointCommentModel
from app.service import facade
from app.extensions import get_db
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, status
from uuid import uuid4
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List


router = APIRouter(prefix='/api/v1/pa_comment', tags=['Comments are written to Appoint by Patient'])

@router.post('/', response_model=GetPatientToAppointCommentModel, status_code=status.HTTP_201_CREATED)
async def add_pa_comment(Model: PostPatientToAppointCommentModel, session: AsyncSession = Depends(get_db)):
    existing_patient = await facade.get_patient(patient_id=Model.patient_id, session=session)
    if not existing_patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Patient Not found'
        )
    existing_appointment = await facade.get_appointment(appointment_id=Model.appoint_id, session=session)
    if not existing_appointment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Appointment Not found'
        )
    
    Model.id = uuid4()
    Model.created_at = datetime.now()
    Model.updated_at = datetime.now()

    comment = await facade.add_pa_comment(Model=Model, session=session)
    return comment
    

@router.get('/', response_model=List[GetPatientToAppointCommentModel], status_code=status.HTTP_200_OK)
async def get_all_pa_comments(session: AsyncSession = Depends(get_db)):
    comments = await facade.get_all_pa_comments(session=session)
    if not comments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Comments not found"
        )
    
    data = []
    for comment in comments:
        data.append(comment)
    return data


@router.get('/{patienttoappointcomment_id}', response_model=GetPatientToAppointCommentModel, status_code=status.HTTP_200_OK)
async def get_pa_comment(patienttoappointcomment_id, session: AsyncSession = Depends(get_db)):
    comment = await facade.get_pa_comment(patienttoappointcomment_id=patienttoappointcomment_id, session=session)
    if not comment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Comment not found"
        )
    return comment

@router.get('/patient/{patient_id}', response_model=List[GetPatientToAppointCommentModel], status_code=status.HTTP_200_OK)
async def get_da_comment_by_patient_id(patient_id, session: AsyncSession = Depends(get_db)):
    existing_patient = await facade.get_patient(patient_id=patient_id, session=session)
    if not existing_patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Patient Not found'
        )
    
    comments = await facade.get_pa_comment_by_patient_id(patient_id=patient_id, session=session)
    data = []

    for comment in comments:
        data.append(comment)

    return data


@router.get('/appoint/{appoint_id}', response_model=List[GetPatientToAppointCommentModel], status_code=status.HTTP_200_OK)
async def get_pa_comment_by_appoint_id(appoint_id, session: AsyncSession = Depends(get_db)):
    existing_appoint = await facade.get_appointment(appointment_id=appoint_id, session=session)
    if not existing_appoint:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Appoint Not found'
        )
    
    comments = await facade.get_pa_comment_by_appoint_id(appoint_id=appoint_id, session=session)
    data = []

    for comment in comments:
        data.append(comment)

    return data



@router.put('/{patienttoappointcomment_id}', response_model=GetPatientToAppointCommentModel, status_code=status.HTTP_200_OK)
async def update_pa_comment(patienttoappointcomment_id, Model: UpdatePatientToAppointCommentModel, session: AsyncSession = Depends(get_db)):
    existing_comment = await facade.get_pa_comment(patienttoappointcomment_id=patienttoappointcomment_id, session=session)
    if not existing_comment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Comment not found'
        )
    
    if Model.patient_id and Model.patient_id != existing_comment.patient_id:
        existing_patient = await facade.get_patient(patient_id=Model.doctor_id, session=session)
        if not existing_patient:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Patient Not Found'
            )
        
    if Model.appoint_id and Model.appoint_id != existing_comment.appoint_id:
        existing_appoint = await facade.get_appointment(appointment_id=Model.appoint_id, session=session)
        if not existing_appoint:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Appoint Not Found'
            )
        
    updated_comment = await facade.update_pa_comment(Model=Model, patienttoappointcomment_id=patienttoappointcomment_id, session=session)

    return updated_comment

@router.delete('/{patienttoappointcomment_id}', response_model=None, status_code=status.HTTP_204_NO_CONTENT)    
async def delete_pa_comment(patienttoappointcomment_id, session: AsyncSession = Depends(get_db)):
    existing_comment = await facade.get_pa_comment(patienttoappointcomment_id=patienttoappointcomment_id, session=session)
    if not existing_comment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Comment not found'
        )
    await facade.delete_pa_comment(patienttoappointcomment_id=patienttoappointcomment_id, session=session)
    return None

@router.delete('/patient/{patient_id}', response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def delete_pa_comment_by_patient_id(patient_id, session: AsyncSession = Depends(get_db)):
    existing_comment = await facade.get_pa_comment_by_patient_id(patient_id=patient_id, session=session)

    if not existing_comment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Comment not found'
        )
    
    await facade.delete_pa_comment_by_patient_id(patient_id=patient_id, session=session)
    return None

@router.delete('/appoint/{appoint_id}', response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def delete_pa_comment_by_appoint_id(appoint_id, session: AsyncSession = Depends(get_db)):
    existing_comment = await facade.get_pa_comment_by_appoint_id(appoint_id=appoint_id, session=session)

    if not existing_comment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Comment not found'
        )
    
    await facade.delete_pa_comment_by_appoint_id(appoint_id=appoint_id, session=session)
    return None