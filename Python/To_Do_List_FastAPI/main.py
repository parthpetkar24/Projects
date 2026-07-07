from fastapi import FastAPI,Depends,HTTPException
from db import To_Do_Task,create_db_and_tables,get_async_session
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from schemas import TaskCreate,TaskShow
from typing import List
from uuid import UUID

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

@app.get("/get-tasks",response_model=list[TaskShow])
async def get_all_task(session:AsyncSession=Depends(get_async_session)):
    result=await session.execute(select(To_Do_Task))
    tasks=result.scalars().all()
    return tasks

@app.get("/get-task/{task_id}",response_model=TaskShow)
async def get_task_by_id(task_id:UUID ,session:AsyncSession=Depends(get_async_session)):
    result=await session.execute(select(To_Do_Task).where(To_Do_Task.id==task_id))
    tasks=result.scalar_one_or_none()
    if tasks is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks