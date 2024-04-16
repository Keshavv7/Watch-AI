from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from schemas.user_schema import UserCreateSchema, UserLoginSchema
from schemas.admin_schema import AdminCreateSchema, AdminLoginSchema
from models.user import User
from models.admin import Admin
import jwt
from jwt import PyJWTError
from typing import Optional
from sqlalchemy.orm import Session
from models import User, Admin

SECRET_KEY = "YOUR_SECRET_KEY"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class TokenData:
    username: Optional[str] = None
    role: Optional[str] = None  # Add role field

def create_access_token(data: dict, type: str, role: str):  # Modify this function
    to_encode = data.copy()
    to_encode.update({"type": type, "role": role})  # Include role in the token payload
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
        role: str = payload.get("role")  # Extract role from the token payload
        if username is None or role is None:
            raise credentials_exception
        token_data = TokenData(username=username, role=role)
    except PyJWTError:
        raise credentials_exception
    if token_data.role == "user":
        user = get_user_by_username(username=token_data.username)
    elif token_data.role == "admin":
        user = get_admin_by_username(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


# incomplete functions
def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def get_admin_by_username(db: Session, username: str):
    return db.query(Admin).filter(Admin.username == username).first()
