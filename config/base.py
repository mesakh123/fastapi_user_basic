
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.ext.asyncio import create_async_engine


#DATABASE_URL = "sqlite+aiosqlite:///./test.db"
DATABASE_URL = "postgresql+asyncpg://root:root@localhost/mydatabase"
SECRET = "93c52c5d8ddb5ab1f3b92856f2655371d6ba32a42bdcce7f2eefa738a9136345"

Base: DeclarativeMeta = declarative_base()
engine = create_async_engine(DATABASE_URL)

# Base.metadata.create_all(engine)
