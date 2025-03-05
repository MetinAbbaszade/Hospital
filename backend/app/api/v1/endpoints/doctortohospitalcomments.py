from app.api.v1.schemas.doctortohospitalcomment import PostDoctorToHospitalCommentModel, UpdateDoctorToHospitalCommentModel, GetDoctorToHospitalCommentModel
from app.extensions import get_db
from app.service import facade
from datetime import datetime
from fastapi import APIRouter, HTTPException, status, Depends
from uuid import UUID, uuid4
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession 

router = APIRouter(prefix='/api/v1/dh_comment', tags=['Comment Was Written to Hospital by Doctor'])

@router.post('/', response_model=GetDoctorToHospitalCommentModel, status_code=status.HTTP_201_CREATED)
async def create_doctor_to_hospital_comment(Model: PostDoctorToHospitalCommentModel, session: AsyncSession = Depends(get_db)):
    existing_hospital = await facade.get_hospital(hospital_id=Model.hospital_id, session=session)
    if not existing_hospital:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Hospital not found'
        )
    existing_doctor = await facade.get_doctor(doctor_id=Model.doctor_id, session=session)
    if not existing_doctor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Doctor not found'
        )
    Model.id = uuid4()
    Model.created_at = datetime.now()
    Model.updated_at = datetime.now()
    hospitalcomment = await facade.add_dh_comment(Model=Model, session=session)
    return hospitalcomment

@router.get('/', response_model=List[GetDoctorToHospitalCommentModel], status_code=status.HTTP_200_OK)
async def get_doctor_to_hospital_comments(session: AsyncSession = Depends(get_db)):
    hospitalcomments = await facade.get_all_dh_comments(session=session)
    if not hospitalcomments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is not any comments which are written to hospital by doctor'
        )
    data = []
    for hospitalcomment in hospitalcomments:
        data.append(hospitalcomment)
    return data

@router.get('/{hospitalcomment_id}', response_model=GetDoctorToHospitalCommentModel, status_code=status.HTTP_200_OK)
async def get_doctor_to_hospital_comment(hospitalcomment_id: UUID | str, session: AsyncSession = Depends(get_db)):
    hospitalcomment = await facade.get_dh_comment(doctortohospitalcomment_id=hospitalcomment_id, session=session)
    if not hospitalcomment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is not any comments which are written to hospital by doctor'
        )
    return hospitalcomment

@router.get('/hospital/{hospital_id}', response_model=List[GetDoctorToHospitalCommentModel], status_code=status.HTTP_200_OK)
async def get_dh_comment_by_hospital_id(hospital_id: UUID, session: AsyncSession = Depends(get_db)):
    existing_hospital = await facade.get_hospital(hospital_id=hospital_id, session=session)
    if not existing_hospital:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Hospital not found'
        )
    
    comments = await facade.get_dh_comment_by_hospital_id(hospital_id=hospital_id, session=session)
    if not comments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There isn't any comment on this hospital_id"
        )

    data = []
    for comment in comments:
        data.append(comment)

    return data

@router.get('/doctor/{doctor_id}', response_model=List[GetDoctorToHospitalCommentModel], status_code=status.HTTP_200_OK)
async def get_dh_comment_by_doctor_id(doctor_id: UUID, session: AsyncSession = Depends(get_db)):
    existing_doctor = await facade.get_doctor(doctor_id=doctor_id, session=session)
    if not existing_doctor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Doctor not found'
        )
    
    comments = await facade.get_dh_comment_by_doctor_id(doctor_id=doctor_id, session=session)
    if not comments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There isn't any comment on this doctor_id"
        )
    
    data = []
    for comment in comments:
        data.append(comment)

    return data


@router.put('/{hospitalcomment_id}', response_model=GetDoctorToHospitalCommentModel, status_code=status.HTTP_200_OK)
async def update_doctor_to_hospital_comment(hospitalcomment_id: UUID | str, Model: UpdateDoctorToHospitalCommentModel, session: AsyncSession = Depends(get_db)):
    existing_hospitalcomment = await facade.get_dh_comment(doctortohospitalcomment_id=hospitalcomment_id, session=session)
    if not existing_hospitalcomment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is not any comments which are written to hospital by doctor'
        )
    if Model.hospital_id and Model.hospital_id != existing_hospitalcomment.hospital_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Hospital_id cannot be changed'
        )
    if Model.doctor_id and Model.doctor_id != existing_hospitalcomment.doctor_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Doctor_id cannot be changed'
        )
    hospitalcomment = await facade.update_dh_comment(Model=Model, doctortohospitalcomment_id=hospitalcomment_id, session=session)
    return hospitalcomment

@router.delete('/{hospitalcomment_id}', response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def delete_doctor_to_hospital_comment(hospitalcomment_id: UUID | str, session: AsyncSession = Depends(get_db)):
    existing_hospitalcomment = await facade.get_dh_comment(doctortohospitalcomment_id=hospitalcomment_id, session=session)
    if not existing_hospitalcomment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Hospitalcomment not found'
        )
    await facade.delete_dh_comment(doctortohospitalcomment_id=hospitalcomment_id, session=session)
    return None


@router.delete('/hospital/{hospital_id}', response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def delete_dh_comment_by_hospital_id(hospital_id: UUID, session: AsyncSession = Depends(get_db)):
    existing_hospitalcomment = await facade.get_dh_comment_by_hospital_id(hospital_id=hospital_id, session=session)
    if not existing_hospitalcomment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Hospitalcomment not found'
        )
    await facade.delete_dh_comment_by_hospital_id(hospital_id=hospital_id, session=session)
    return None


@router.delete('/doctor/{doctor_id}', response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def delete_dh_comment_by_doctor_id(doctor_id: UUID, session: AsyncSession = Depends(get_db)):
    existing_doctorcomment = await facade.get_dh_comment_by_doctor_id(doctor_id=doctor_id, session=session)
    if not existing_doctorcomment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Hospitalcomment not found'
        )
    await facade.delete_dh_comment_by_doctor_id(doctor_id=doctor_id, session=session)
    return None