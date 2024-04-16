from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    role: str = "user"  # Default role is user

class Admin(BaseModel):
    username: str
    password: str
    role: str = "admin"  # Default role is admin
