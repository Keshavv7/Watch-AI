from fastapi import APIRouter, Depends, HTTPException
from schemas.user_schema import UserCreateSchema, UserLoginSchema
from schemas.admin_schema import AdminLoginSchema
from auth import create_access_token, get_current_user

router = APIRouter()

@router.post("/token")
async def login_for_access_token(form_data: UserLoginSchema):
    # Logic to authenticate user
    # Assuming user authentication is successful, generate access token
    access_token = create_access_token(data={"sub": form_data.username}, type="user")
    return {"access_token": access_token, "token_type": "bearer", "role": "user"}

@router.post("/admin/token")
async def admin_login_for_access_token(form_data: AdminLoginSchema):
    # Logic to authenticate admin
    # Assuming admin authentication is successful, generate access token
    access_token = create_access_token(data={"sub": form_data.username}, type="admin")
    return {"access_token": access_token, "token_type": "bearer", "role": "admin"}

@router.get("/users/me")
async def read_users_me(current_user = Depends(get_current_user)):
    # Assuming get_current_user function returns the user object
    if current_user.role != "user":
        raise HTTPException(status_code=403, detail="User role required")
    return current_user

@router.get("/admins/me")
async def read_admins_me(current_admin = Depends(get_current_user)):
    # Assuming get_current_user function returns the admin object
    if current_admin.role != "admin":
        raise HTTPException(status_code=403, detail="Admin role required")
    return current_admin
