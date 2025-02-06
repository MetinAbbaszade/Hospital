from app.api.v1.schemas.admin import GetAdminModel, PostAdminModel, UpdateAdminModel
from app.api.v1.schemas.user import UserModel
from app.extensions import get_db
from app.models.user import User
from app.service import facade
from datetime import datetime
from fastapi import APIRouter, Depends, status, HTTPException
from uuid import UUID, uuid4
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

router = APIRouter(prefix='/api/v1/admin', tags=['admin'])


@router.post('/', response_model=UserModel, status_code=status.HTTP_201_CREATED)
async def add_admin(Model: PostAdminModel, session: AsyncSession = Depends(get_db)):
    existing_user: User = await facade.get_user_by_email(email=Model.email,session=session)
    if existing_user:
        raise HTTPException(
            detail='Email has already signed up',
            status_code=status.HTTP_400_BAD_REQUEST
        )
    
    Model.id = uuid4()
    Model.created_at = datetime.now()
    Model.updated_at = datetime.now()
    
    new_user = await facade.add_user(Model=Model, session=session)
    await facade.add_admin(Model=Model, session=session)
    return new_user

@router.get('/', response_model=List[GetAdminModel], status_code=status.HTTP_200_OK)
async def get_all_admins(session: AsyncSession = Depends(get_db)):
    admins: List[GetAdminModel] = await facade.get_all_admins(session=session)

    if not admins:
        raise HTTPException(
            detail='Admins not found',
            status_code=status.HTTP_404_NOT_FOUND
        )
    data = []
    for admin in admins:
        data.append(admin)
    return data

@router.get('/{admin_id}', response_model=GetAdminModel, status_code=status.HTTP_200_OK)
async def get_admin(admin_id, session: AsyncSession = Depends(get_db)):
    admin: GetAdminModel = await facade.get_admin(admin_id=admin_id, session=session)

    if not admin:
        raise HTTPException(
            detail='Admin not found',
            status_code=status.HTTP_404_NOT_FOUND
        )
    return admin


@router.put('/{admin_id}', response_model=GetAdminModel, status_code=status.HTTP_200_OK)
async def update_admin(
    admin_id: UUID,
    Model: UpdateAdminModel,
    session: AsyncSession = Depends(get_db)
):
    admin: GetAdminModel = await facade.get_admin(admin_id=admin_id, session=session)

    if not admin:
        raise HTTPException(
            detail='Admin not found',
            status_code=status.HTTP_404_NOT_FOUND
        )
    updated_admin = await facade.update_admin(admin_id=admin_id, Model=Model, session=session)
    return updated_admin

@router.delete('/{admin_id}', response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def delete_admin(admin_id, session: AsyncSession = Depends(get_db)):
    admin: GetAdminModel = await facade.get_admin(admin_id=admin_id, session=session)

    if not admin:
        raise HTTPException(
            detail='Admin not found',
            status_code=status.HTTP_404_NOT_FOUND
        )
    await facade.delete_admin(admin_id=admin_id, session=session)
    await facade.delete_user(user_id=admin_id, session=session)