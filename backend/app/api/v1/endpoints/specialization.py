from app.api.v1.schemas.specialization import PostSpecialization, UpdateSpecialization, GetSpecialization
from app.extensions import get_db
from app.models.specialization import Specialization
from app.service.specialities import Facade as Specialization_facade
from app.service.hospitalspecialities import Facade as HospitalSpecialities_facade
from app.service.doctorspecialities import Facade as DoctorSpecialities_facade
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID, uuid4

router = APIRouter(prefix="/api/v1/specialization", tags=["Specialization"])

specialization_facade = Specialization_facade()
hospitalspecialities_facade = HospitalSpecialities_facade()
doctorspecialities_facade = DoctorSpecialities_facade()

@router.post("/", response_model=GetSpecialization, status_code=status.HTTP_201_CREATED)
async def create_specialization(Model: PostSpecialization, session: Session = Depends(get_db)):
    Model.id = uuid4()
    Model.created_at = datetime.now()
    Model.updated_at = datetime.now()

    specialization = await specialization_facade.add_specialization(Model=Model, session=session)

    return specialization


@router.get("/", response_model=List[GetSpecialization], status_code=status.HTTP_200_OK)
async def get_specializations(session: Session = Depends(get_db)):
    specializations = await specialization_facade.get_all_specializations(session=session)
    if not specializations:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No specializations found"
            )
    data = []
    for specialization in specializations:
        data.append(specialization)
    return data

@router.get("/{specialization_id}", response_model=GetSpecialization, status_code=status.HTTP_200_OK)
async def get_specialization(specialization_id: UUID, session: Session = Depends(get_db)):
    specialization = await specialization_facade.get_specialization(specialization_id=specialization_id, session=session)
    if not specialization:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Specialization not found"
            )
    return specialization

@router.put("/{specialization_id}", response_model=GetSpecialization, status_code=status.HTTP_200_OK)
async def update_specialization(specialization_id: UUID, Model: UpdateSpecialization, session: Session = Depends(get_db)):
    specialization = await specialization_facade.update_specialization(specialization_id=specialization_id, Model=Model, session=session)
    if not specialization:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Specialization not found"
            )
    return specialization

@router.delete("/{specialization_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_specialization(specialization_id: UUID, session: Session = Depends(get_db)):
    specialization = await specialization_facade.get_specialization(specialization_id=specialization_id, session=session)
    if not specialization:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Specialization not found"
            )
    await doctorspecialities_facade.delete_doctorspecialization_by_specialization(specialization_id=specialization_id, session=session)
    await hospitalspecialities_facade.delete_hospitalspecialization_by_specialization(specialization_id=specialization_id, session=session)
    await specialization_facade.delete_specialization(specialization_id=specialization_id, session=session)
    return None