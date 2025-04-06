from app.api.v1.schemas.auth import CustomOAuthBearer, create_access_token
from app.api.v1.schemas.patient import PostPatientModel
from app.api.v1.schemas.user import UserModel
from app.models.user import User
from app.extensions import get_db
from app.service.patient import Facade as Patient_facade
from app.service.user import Facade as User_facade
from datetime import datetime, timezone
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

patient_facade = Patient_facade()
user_facade = User_facade()

router = APIRouter(prefix='/api/v1/auth', tags=['authentication'])

@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=str)
async def signup(Model: PostPatientModel, session: AsyncSession = Depends(get_db)):
    existing_user = await user_facade.get_user_by_email(email=Model.email, session=session)

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Email already exists'
        )

    Model.id = uuid4()
    Model.updated_at = datetime.now(timezone.utc)
    Model.created_at = datetime.now(timezone.utc)

    new_user: User = await user_facade.add_user(Model=Model, session=session)
    await patient_facade.add_patient(Model=Model, session=session)

    payload = {
        'sub': new_user.id,
        'email': new_user.email,
        'role': new_user.role
    }
    access_token = await create_access_token(payload)

    return access_token


@router.post('/login', response_model=str, status_code=status.HTTP_201_CREATED)
async def login(formdata: CustomOAuthBearer = Depends(), session: AsyncSession = Depends(get_db)):
    email = formdata.email
    existing_user: User = await user_facade.get_user_by_email(email=email, session=session)

    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User not found'
        )
    
    if not existing_user.verify_password(formdata.password, existing_user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Incorrect Password'
        )
    
    payload = {
        'sub': existing_user.id,
        'email': existing_user.email,
        'role': existing_user.role
    }

    access_token = await create_access_token(payload)

    return access_token