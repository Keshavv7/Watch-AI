from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from auth.auth import create_access_token, get_current_user
from models.user import User
from models.admin import Admin
from schemas.user_schema import UserCreateSchema, UserLoginSchema
from schemas.admin_schema import AdminCreateSchema, AdminLoginSchema

router = APIRouter()

@router.post("/token", response_model=dict)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user.username}, type="user")
    return {"access_token": access_token, "token_type": "bearer"}

# Admin login route can be similar to user login, just needs to use different schemas and authentication function

def authenticate_user(username: str, password: str):
    # Placeholder function to simulate user authentication
    # Replace this with your actual authentication logic
    pass

def authenticate_admin(username: str, password: str):
    # Placeholder function to simulate admin authentication
    # Replace this with your actual authentication logic
    pass
