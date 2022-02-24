
from fastapi_users.db import SQLAlchemyBaseUserTable
from config.base import Base


class UserTable(Base, SQLAlchemyBaseUserTable):
    pass
