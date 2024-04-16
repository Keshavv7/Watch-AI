from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from schemas.user_schema import UserCreateSchema, UserLoginSchema
from schemas.admin_schema import AdminCreateSchema, AdminLoginSchema
from models.user import User
from models.admin import Admin
import jwt
from jwt import PyJWTError
from typing import Optional

SECRET_KEY = "YOUR_SECRET_KEY"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class TokenData:
    username: Optional[str] = None

def create_access_token(data: dict, type: str):
    to_encode = data.copy()
    to_encode.update({"type": type})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_type: str = payload.get("type")
        if username is None or user_type is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except PyJWTError:
        raise credentials_exception
    if user_type == "user":
        user = get_user_by_username(username=token_data.username)
    elif user_type == "admin":
        user = get_admin_by_username(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

def get_user_by_username(username: str):
    # Placeholder function to simulate querying the database for a user by username
    # Replace this with your actual database query logic
    pass

def get_admin_by_username(username: str):
    # Placeholder function to simulate querying the database for an admin by username
    # Replace this with your actual database query logic
    pass
