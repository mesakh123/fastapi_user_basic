from fastapi import APIRouter
from fastapi_users import FastAPIUsers
from fastapi_users.db import SQLAlchemyUserDatabase


from models.usermodel import UserTable
from schemas.user import User, UserCreate, UserUpdate, UserDB
from auth.auth import jwt_authentication
from config.database import database


router = APIRouter()

users = UserTable.__table__
user_db = SQLAlchemyUserDatabase(UserDB, database, users)

fastapi_users = FastAPIUsers(
    user_db,
    [jwt_authentication],
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)
