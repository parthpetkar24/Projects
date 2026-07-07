from fastapi import FastAPI,Depends
from db import To_Do_Task,create_db_and_tables,get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from schemas import TaskCreate,TaskShow

@asynccontextmanager
async def lifespan(app:FastAPI):
    await create_db_and_tables()
    yield

app=FastAPI(lifespan=lifespan)

@app.get("/")
def home():
    return {"message":"Welcome to TaskForge"}

@app.post("/new-task",response_model=TaskShow)
async def create_task(
    task_in:TaskCreate,
    session:AsyncSession=Depends(get_async_session)
):
    new_task=To_Do_Task(**task_in.model_dump())
    session.add(new_task)
    await session.commit()
    await session.refresh(new_task)
    return new_task