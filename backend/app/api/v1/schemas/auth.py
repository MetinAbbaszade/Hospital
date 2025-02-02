from app.extensions import get_db
from app.models.user import User
from datetime import datetime
import jwt
from fastapi import Form, Depends, HTTPException, status
from fastapi.security import HTTPBearer
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from service import facade
from pydantic import BaseModel

http_token = HTTPBearer()

SECRETKEY = 'b1LpX8$^92Ww7JsdQm4!RgTzZf9#nCvMkRpY03!H5LN8@aX&yF7#G2'
ALGORITHM = 'HS256'

class UserModel(BaseModel):
    id: UUID
    role: str
    email: str
    password: str

class SignUpModel(BaseModel):
    id: UUID | None = None
    name: str
    surname: str
    email: str
    password: str
    role: str | None = 'patient'
    created_at: datetime | None = None
    updated_at: datetime | None = None


class CustomOAuthBearer:
    def __init__(self,
        email = Form(...),
        password = Form(...)
    ):
        self.email = email
        self.password = password

async def create_access_token(payload):
    for key, value in payload.items():
        if isinstance(value, UUID):
            payload[key] = str(value)
        
    access_token = jwt.encode(
        payload=payload,
        key = SECRETKEY,
        algorithm=ALGORITHM
    )

    return access_token

async def decode_token(token):
    decoded_token = jwt.decode(
        jwt=token,
        key=SECRETKEY,
        algorithms=[ALGORITHM]
    )

    return decoded_token

async def get_token_from_credentials(token: str = Depends(http_token)):
    return token.credentials

async def get_current_user(token: str = Depends(get_token_from_credentials), session: AsyncSession = Depends(get_db)):
    decoded_token = await decode_token(token)
    email: str = decoded_token.get('email')

    user: User = await facade.get_user_by_email(email=email, session=session)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User not found'
        )
    return user