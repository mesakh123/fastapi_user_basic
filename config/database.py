import databases
import sqlalchemy
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

DATABASE_URL = "sqlite:///./test.db"
SECRET = "SECRET"

database = databases.Database(DATABASE_URL)
Base: DeclarativeMeta = declarative_base()

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
Base.metadata.create_all(engine)
