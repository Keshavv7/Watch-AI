from pydantic import BaseModel

class AdminCreateSchema(BaseModel):
    username: str
    password: str

class AdminLoginSchema(BaseModel):
    username: str
    password: str
