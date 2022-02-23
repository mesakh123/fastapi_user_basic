
from fastapi import FastAPI

from config.database import database


from users import userrouter

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(userrouter.router)
