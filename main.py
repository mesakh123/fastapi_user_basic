
from fastapi import FastAPI, Depends
from config.database import database
from schemas.user import UserDB

from users import userrouter
from config.database import create_db_and_tables

app = FastAPI()


@app.on_event("startup")
async def startup():
    await create_db_and_tables()

"""
@app.on_event("shutdown")
async def shutdown():
    retu"""


@app.get("/authenticated-route")
async def authenticated_route(user: UserDB = Depends(userrouter.current_active_user)):
    return {"message": f"Hello {user.email}!"}


from pydantic import BaseModel
from typing import Optional


class Dataset(BaseModel):
    name: Optional[str] = "test"
    length: Optional[int] = 10


@app.post("/test")
async def test_route(request: Dataset = None):
    if not request:
        request = Dataset().json()
    return request


app.include_router(userrouter.router)
