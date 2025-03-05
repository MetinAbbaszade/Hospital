from app.api.v1.schemas.doctortoappointcomment import GetDoctorToAppointCommentModel, UpdateDoctorToAppointCommentModel, PostDoctorToAppointCommentModel
from app.service import facade
from app.extensions import get_db
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, status
from uuid import uuid4
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List


router = APIRouter(prefix='/api/v1/da_comment', tags=['Comments are written by Doctor to Specific Appoint'])

@router.post('/', response_model=GetDoctorToAppointCommentModel, status_code=status.HTTP_201_CREATED)
async def add_da_comment(Model: PostDoctorToAppointCommentModel, session: AsyncSession = Depends(get_db)):
    existing_doctor = await facade.get_doctor(doctor_id=Model.doctor_id, session=session)
    if not existing_doctor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Doctor Not found'
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

    comment = await facade.add_da_comment(Model=Model, session=session)
    return comment
    

@router.get('/', response_model=List[GetDoctorToAppointCommentModel], status_code=status.HTTP_200_OK)
async def get_all_da_comments(session: AsyncSession = Depends(get_db)):
    comments = await facade.get_all_da_comments(session=session)
    if not comments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is not any comments which are written to appointment by doctor"
        )
    
    data = []
    for comment in comments:
        data.append(comment)
    return data


@router.get('/{doctortoappointcomment_id}', response_model=GetDoctorToAppointCommentModel, status_code=status.HTTP_200_OK)
async def get_da_comment(doctortoappointcomment_id, session: AsyncSession = Depends(get_db)):
    comment = await facade.get_da_comment(doctortoappointcomment_id=doctortoappointcomment_id, session=session)
    if not comment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There isn't any coment on this id"
        )
    return comment

@router.get('/doctor/{doctor_id}', response_model=List[GetDoctorToAppointCommentModel], status_code=status.HTTP_200_OK)
async def get_da_comment_by_doctor_id(doctor_id, session: AsyncSession = Depends(get_db)):
    existing_doctor = await facade.get_doctor(doctor_id=doctor_id, session=session)
    if not existing_doctor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Doctor Not found'
        )
    
    comments = await facade.get_da_comment_by_doctor_id(doctor_id=doctor_id, session=session)
    if not comments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There isn't any comment on this doctor_id"
        )
    data = []

    for comment in comments:
        data.append(comment)

    return data


@router.get('/appoint/{appoint_id}', response_model=List[GetDoctorToAppointCommentModel], status_code=status.HTTP_200_OK)
async def get_da_comment_by_appoint_id(appoint_id, session: AsyncSession = Depends(get_db)):
    existing_appoint = await facade.get_appointment(appointment_id=appoint_id, session=session)
    if not existing_appoint:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Appoint Not found'
        )
    
    comments = await facade.get_da_comment_by_appoint_id(appoint_id=appoint_id, session=session)
    if not comments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There isn't any comment on this appoint_id"
        )
    data = []

    for comment in comments:
        data.append(comment)

    return data



@router.put('/{doctortoappointcomment_id}', response_model=GetDoctorToAppointCommentModel, status_code=status.HTTP_200_OK)
async def update_da_comment(doctortoappointcomment_id, Model: UpdateDoctorToAppointCommentModel, session: AsyncSession = Depends(get_db)):
    existing_comment = await facade.get_da_comment(doctortoappointcomment_id=doctortoappointcomment_id, session=session)
    if not existing_comment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Comment not found'
        )
    
    if Model.doctor_id and Model.doctor_id != existing_comment.doctor_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="You can't change doctor_id"
        )
        
    if Model.appoint_id and Model.appoint_id != existing_comment.appoint_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="You can't change appoint_id"
        )
        
    updated_comment = await facade.update_da_comment(Model=Model, doctortoappointcomment_id=doctortoappointcomment_id, session=session)

    return updated_comment

@router.delete('/{doctortoappointcomment_id}', response_model=None, status_code=status.HTTP_204_NO_CONTENT)    
async def delete_da_comment(doctortoappointcomment_id, session: AsyncSession = Depends(get_db)):
    existing_comment = await facade.get_da_comment(doctortoappointcomment_id=doctortoappointcomment_id, session=session)
    if not existing_comment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Comment not found'
        )
    await facade.delete_da_comment(doctortoappointcomment_id=doctortoappointcomment_id, session=session)
    return None

@router.delete('/doctor/{doctor_id}', response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def delete_da_comment_by_doctor_id(doctor_id, session: AsyncSession = Depends(get_db)):
    existing_comment = await facade.get_da_comment_by_doctor_id(doctor_id=doctor_id, session=session)

    if not existing_comment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Comment not found'
        )
    
    await facade.delete_da_comment_by_doctor_id(doctor_id=doctor_id, session=session)
    return None

@router.delete('/appoint/{appoint_id}', response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def delete_da_comment_by_appoint_id(appoint_id, session: AsyncSession = Depends(get_db)):
    existing_comment = await facade.get_da_comment_by_appoint_id(appoint_id=appoint_id, session=session)

    if not existing_comment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Comment not found'
        )
    
    await facade.delete_da_comment_by_appoint_id(appoint_id=appoint_id, session=session)
    return None