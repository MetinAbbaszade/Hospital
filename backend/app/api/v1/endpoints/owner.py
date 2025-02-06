from app.api.v1.schemas.owner import GetOwnerModel, PostOwnerModel, UpdateOwnerModel
from app.api.v1.schemas.user import UserModel
from app.extensions import get_db
from app.models.owner import Owner
from app.service import facade
from datetime import datetime
from fastapi import APIRouter, Depends, status, HTTPException
from uuid import uuid4, UUID
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

router = APIRouter(prefix='/api/v1/owner', tags=['Hospital Owner'])

@router.post('/', response_model=UserModel, status_code=status.HTTP_201_CREATED)
async def add_owner(
    Model: PostOwnerModel,
    session: AsyncSession = Depends(get_db)
):
    existing_email = await facade.get_user_by_email(email=Model.email, session=session)

    if existing_email:
        raise HTTPException(
            detail='Email has already exist',
            status_code=status.HTTP_400_BAD_REQUEST
        )
    Model.id = uuid4()
    Model.created_at = datetime.now()
    Model.updated_at = datetime.now()

    user = await facade.add_user(Model=Model, session=session)
    await facade.add_hospital_owner(Model=Model, session=session)

    return user

@router.get('/', response_model=List[GetOwnerModel], status_code=status.HTTP_200_OK)
async def get_all_owners(
    session: AsyncSession = Depends(get_db)
):
    owners = await facade.get_all_hospital_owners(session=session)
    if not owners:
        raise HTTPException(
            detail='Owners not found',
            status_code=status.HTTP_404_NOT_FOUND
        )
    
    data = []
    for owner in owners:
        data.append(owner)
    
    return data

@router.get('/{owner_id}', response_model=GetOwnerModel, status_code=status.HTTP_200_OK)
async def get_owner(
    owner_id: UUID,
    session: AsyncSession = Depends(get_db)
):
    owner = await facade.get_hospital_owner(owner_id=owner_id, session=session)
    if not owner:
        raise HTTPException(
            detail='Owners not found',
            status_code=status.HTTP_404_NOT_FOUND
        )
    
    return owner

@router.put('/{owner_id}', response_model=GetOwnerModel, status_code= status.HTTP_200_OK)
async def update_owner(
    owner_id: UUID, 
    Model: UpdateOwnerModel, 
    session: AsyncSession = Depends(get_db)
):
    owner: Owner = await facade.get_hospital_owner(owner_id=owner_id, session=session)

    if not owner:
        raise HTTPException(
            detail='Owner not found',
            status_code=status.HTTP_404_NOT_FOUND
        )
    
    updated_owner = await facade.update_hospital_owner(owner_id=owner_id, Model=Model, session=session)
    return updated_owner

@router.delete('/{owner_id}', response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def delete_owner(
    owner_id: UUID,
    session: AsyncSession = Depends(get_db)
):
    owner = await facade.get_hospital_owner(owner_id=owner_id, session=session)
    if not owner:
        raise HTTPException(
            detail='Owners not found',
            status_code=status.HTTP_404_NOT_FOUND
        )
    await facade.delete_hospital_owner(owner_id=owner_id, session=session)
    await facade.delete_user(user_id=owner_id, session=session)