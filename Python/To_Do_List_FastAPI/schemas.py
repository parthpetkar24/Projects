from pydantic import BaseModel,ConfigDict
from datetime import date, time
from uuid import UUID
from db import TaskStatus
from typing import Optional

class TaskCreate(BaseModel):
    task:str
    due_date: date
    status: TaskStatus=TaskStatus.PENDING

class TaskShow(BaseModel):
    id:UUID
    task:str
    date: date
    time: time
    due_date: date
    status: TaskStatus
    model_config = ConfigDict(from_attributes=True)

class TaskUpdate(BaseModel):
    task: Optional[str] = None
    due_date: Optional[date] = None
    status: Optional[TaskStatus] = None
    