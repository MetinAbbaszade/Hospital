from app.extensions import get_db
from app.models.user import User
import jwt
from app.service.user import Facade as User_facade
from fastapi import Form, Depends, HTTPException, status
from fastapi.security import HTTPBearer
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timedelta
from typing import Dict, Optional, Tuple

http_token = HTTPBearer()

SECRETKEY = 'b1LpX8$^92Ww7JsdQm4!RgTzZf9#nCvMkRpY03!H5LN8@aX&yF7#G2'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRE_DAYS = 1

user_facade = User_facade()


class CustomOAuthBearer:
    def __init__(self,
        email = Form(...),
        password = Form(...)
    ):
        self.email = email
        self.password = password


class TokenResponse:
    def __init__(self, access_token: str, refresh_token: str):
        self.access_token = access_token
        self.refresh_token = refresh_token


async def create_access_token(payload, expires_delta: Optional[timedelta] = None):
    to_encode = payload.copy()
    
    for key, value in to_encode.items():
        if isinstance(value, UUID):
            to_encode[key] = str(value)
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    
    access_token = jwt.encode(
        payload=to_encode,
        key=SECRETKEY,
        algorithm=ALGORITHM
    )

    return access_token


async def create_refresh_token(payload):
    to_encode = payload.copy()
    
    for key, value in to_encode.items():
        if isinstance(value, UUID):
            to_encode[key] = str(value)
    
    expire = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire, "token_type": "refresh"})
    
    refresh_token = jwt.encode(
        payload=to_encode,
        key=SECRETKEY,
        algorithm=ALGORITHM
    )

    return refresh_token


async def create_tokens(payload) -> Tuple[str, str]:
    access_token = await create_access_token(payload)
    refresh_token = await create_refresh_token(payload)
    return access_token, refresh_token


async def decode_token(token):
    try:
        decoded_token = jwt.decode(
            jwt=token,
            key=SECRETKEY,
            algorithms=[ALGORITHM]
        )
        return decoded_token
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired"
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )


async def get_token_from_credentials(token: str = Depends(http_token)):
    return token.credentials


async def get_current_user(token: str = Depends(get_token_from_credentials), session: AsyncSession = Depends(get_db)):
    decoded_token = await decode_token(token)
    email: str = decoded_token.get('email')

    user: User = await user_facade.get_user_by_email(email=email, session=session)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User not found'
        )
    return user