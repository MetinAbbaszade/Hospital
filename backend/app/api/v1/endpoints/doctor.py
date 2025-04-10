from app.api.v1.schemas.doctor import GetDoctorModel, PostDoctorModel, UpdateDoctorModel
from app.api.v1.schemas.doctorspecialization import PostDoctorSpecializationModel
from app.api.v1.schemas.user import UserModel
from app.api.v1.schemas.hospital import HospitalModel
from app.api.v1.endpoints.patienttodoctorcomment import delete_pd_comment_by_doctor_id
from app.api.v1.endpoints.doctortoappointcomment import delete_da_comment_by_doctor_id
from app.api.v1.endpoints.doctortohospitalcomments import delete_dh_comment_by_doctor_id
from app.extensions import get_db
from app.service.user import Facade as User_facade
from app.service.doctor import Facade as Doctor_facade
from app.service.hospital import Facade as Hospital_facade
from app.service.specialities import Facade as Specialization_facade
from app.service.doctorspecialities import Facade as DS_facade
from datetime import datetime
from fastapi import APIRouter, Depends, status, HTTPException
from uuid import uuid4, UUID
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

router = APIRouter(prefix='/api/v1/doctor', tags=['doctor'])
user_facade = User_facade()
doctor_facade = Doctor_facade()
hospital_facade = Hospital_facade()
specialization_facade = Specialization_facade()
doctorspecialization_facade = DS_facade()

@router.post('/', response_model=UserModel, status_code=status.HTTP_201_CREATED)
async def add_doctor(
    Model: PostDoctorModel,
    session: AsyncSession = Depends(get_db)
    ):
    existing_email = await user_facade.get_user_by_email(email=Model.email, session=session)

    if existing_email:
        raise HTTPException(
            detail='Email has already signed up',
            status_code=status.HTTP_400_BAD_REQUEST
        )
    
    existing_hospital = await hospital_facade.get_hospital(hospital_id=Model.hospital_id, session=session)
    if not existing_hospital:
        raise HTTPException(
            detail='Hospital does not exist',
            status_code=status.HTTP_404_NOT_FOUND
        )
    
    Model.id = uuid4()
    Model.created_at = datetime.now()
    Model.updated_at = datetime.now()


    user = await user_facade.add_user(Model=Model, session=session)
    await doctor_facade.add_doctor(Model=Model, session=session)

    session.commit()
    for speciality in Model.specialities:
        specialization = await specialization_facade.get_specialization_by_name(name=speciality, session=session)
        if not specialization:
            raise HTTPException(
                detail='Specialization does not exist',
                status_code=status.HTTP_404_NOT_FOUND
            )
        doctor_specialization = PostDoctorSpecializationModel(
            id=None,
            doctor_id=Model.id,
            specialization_id=specialization.id,
            created_at=None,
            updated_at=None
        )
        await doctorspecialization_facade.add_doctorspecialization(Model=doctor_specialization, session=session)

    session.commit()

    return user

@router.get('/', response_model=List[GetDoctorModel], status_code=status.HTTP_200_OK)
async def get_all_doctors(
    session: AsyncSession = Depends(get_db)
    ):
    doctors: List[GetDoctorModel] = await doctor_facade.get_all_doctors(session=session)

    if not doctors:
        raise HTTPException(
            detail='Doctors not found',
            status_code=status.HTTP_404_NOT_FOUND
        )
    data = []
    for doctor in doctors:
        data.append(doctor)
    return data


@router.get('/{doctor_id}', response_model=GetDoctorModel, status_code=status.HTTP_200_OK)
async def get_doctor(
    doctor_id: UUID, 
    session: AsyncSession = Depends(get_db)
    ):
    doctor: GetDoctorModel = await doctor_facade.get_doctor(doctor_id=doctor_id, session=session)

    if not doctor:
        raise HTTPException(
            detail='Doctor not found',
            status_code=status.HTTP_404_NOT_FOUND
        )
    return doctor

@router.get('/hospital/{hospital_id}', response_model=List[GetDoctorModel], status_code=status.HTTP_200_OK)
async def get_doctor_by_hospital(
    hospital_id: UUID, 
    session: AsyncSession = Depends(get_db)
    ):
    hospital: HospitalModel = await hospital_facade.get_hospital(hospital_id=hospital_id, session=session)
    print(hospital)
    if not hospital:
        raise HTTPException(
            detail='Hospital not found',
            status_code=status.HTTP_404_NOT_FOUND
        )
    doctors = await doctor_facade.get_doctor_by_hospital(hospital_id=hospital_id, session=session)
    print(doctors)
    if doctors is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Doctors not found'
        )
    data = []
    for doctor in doctors:
        data.append(doctor)
    return data

@router.get('/specialization/{specialization}', response_model=List[GetDoctorModel], status_code=status.HTTP_200_OK)
async def get_doctor_by_specialization(
    specialization,
    session: AsyncSession = Depends(get_db)
):
    doctors = await doctor_facade.get_doctor_by_specialization(specialization=specialization, session=session)
    if not doctors:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Doctors not found'
        )
    
    data = []
    for doctor in doctors:
        data.append(doctor)
    return data

@router.put('/{doctor_id}', response_model=GetDoctorModel, status_code=status.HTTP_200_OK)
async def update_doctor(
    doctor_id: UUID,
    Model: UpdateDoctorModel,
    session: AsyncSession = Depends(get_db)
    ):
    doctor: GetDoctorModel = await doctor_facade.get_doctor(doctor_id=doctor_id, session=session)

    if not doctor:
        raise HTTPException(
            detail='Doctor not found',
            status_code=status.HTTP_404_NOT_FOUND
        )
    updated_doctor = await doctor_facade.update_doctor(Model=Model, doctor_id=doctor_id, session=session)
    return updated_doctor

@router.delete('/{doctor_id}', response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def delete_doctor(
    doctor_id: UUID,
    session: AsyncSession = Depends(get_db)
    ):
    doctor: GetDoctorModel = await doctor_facade.get_doctor(doctor_id=doctor_id, session=session)

    if not doctor:
        raise HTTPException(
            detail='Doctor not found',
            status_code=status.HTTP_404_NOT_FOUND
        )
    # await delete_pd_comment_by_doctor_id(doctor_id=doctor_id, session=session)
    # await delete_da_comment_by_doctor_id(doctor_id=doctor_id, session=session)
    # await delete_dh_comment_by_doctor_id(doctor_id=doctor_id, session=session)
    await doctorspecialization_facade.delete_doctorspecialization_by_doctor(doctor_id=doctor_id, session=session)
    await doctor_facade.delete_doctor(doctor_id=doctor_id, session=session)
    await user_facade.delete_user(user_id=doctor_id, session=session)