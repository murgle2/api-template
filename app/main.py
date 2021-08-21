from fastapi import FastAPI

from app.router import path
from app.db.database import engine
from app.db import base

# base.Base.metadata.drop_all(bind=engine)
base.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(path.api_router)


@app.get("/api")
async def root():
    return {"message": "Hello World"}
