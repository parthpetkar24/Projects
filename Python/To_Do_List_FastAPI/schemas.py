from pydantic import BaseModel,ConfigDict
from datetime import date, time
from uuid import UUID
from db import TaskStatus

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