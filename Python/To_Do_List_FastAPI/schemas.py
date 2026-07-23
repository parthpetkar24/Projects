from pydantic import BaseModel,ConfigDict
from datetime import date, time
from uuid import UUID
from db import TaskStatus,TaskPriority, TaskCategory
from typing import Optional

class TaskCreate(BaseModel):
    task:str
    due_date: date
    status: TaskStatus=TaskStatus.PENDING

class TaskShow(BaseModel):
    id:UUID
    task:str
    description: Optional[str] = None
    priority: TaskPriority
    date: date
    time: time
    due_date: date
    status: TaskStatus
    category: TaskCategory
    model_config = ConfigDict(from_attributes=True)

class TaskUpdate(BaseModel):
    task: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[date] = None
    priority: Optional[TaskPriority] = None
    category: Optional[TaskCategory] = None
    status: Optional[TaskStatus] = None
    