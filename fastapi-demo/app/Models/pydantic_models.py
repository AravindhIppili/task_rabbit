from pydantic import BaseModel, EmailStr

class UserRegister(BaseModel):
    fullname: str
    email: EmailStr
    password: str
    cnfpassword: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str