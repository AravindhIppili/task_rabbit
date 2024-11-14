from fastapi import APIRouter
from fastapi.responses import Response
from ..Models.pydantic_models import UserRegister,UserLogin
from ..Utils.DAL.connector import PostSQLBase
from ..Utils.DAL.Tables import User
from sqlalchemy.orm import Session


auth_router = APIRouter(prefix="/auth", tags=[""])

@auth_router.post("/register")
async def register(user_data:UserRegister ):
    session:Session =  PostSQLBase.get_session()
    if(user_data.password != user_data.cnfpassword):
        return Response(status_code=400, content="Password donot match")
    data = session.add(
        User(
            fullname = user_data.fullname,
            email = user_data.email,
            password = user_data.password
        )
    )
    session.commit()

    return data

@auth_router.post("/login")
async def login(user_data:UserLogin ):
    session:Session =  PostSQLBase.get_session()
    data = session.get(User.email == user_data.email)
    return data



