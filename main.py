from contextlib import asynccontextmanager

from fastapi import FastAPI

from db import create_db_and_tables
from routers import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(router)

@app.get("/health")
def health_check():
    return {"status": "ok"}
