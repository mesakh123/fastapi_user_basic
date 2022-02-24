from typing import AsyncGenerator
from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase

import databases

from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator

from models.usermodel import UserTable
from schemas.user import UserDB

from .base import Base, DATABASE_URL, engine

database = databases.Database(DATABASE_URL)


async_session_maker = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    # yield SQLAlchemyUserDatabase(UserDB, database, UserTable)
    yield SQLAlchemyUserDatabase(UserDB, session, UserTable.__table__)
