
from fastapi_users.db import SQLAlchemyBaseUserTable
from config.database import Base


class UserTable(Base, SQLAlchemyBaseUserTable):
    pass
