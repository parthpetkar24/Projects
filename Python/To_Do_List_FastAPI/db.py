from collections.abc import AsyncGenerator
import uuid
from sqlalchemy import Column,String,Date,Time,Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession,create_async_engine,async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from config import DATABASE_URL
from datetime import datetime
import enum

class Base(DeclarativeBase):
    pass

class TaskStatus(enum.Enum):
    PENDING = "Pending"
    DUE = "Due"
    COMPLETED = "Completed"
    FAILED = "Failed"

class To_Do_Task(Base):
    __tablename__="ToDo"

    id=Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    task=Column(String(255),nullable=False)
    date=Column(Date,default=datetime.now().date(),nullable=False)
    time=Column(Time,default=datetime.now().time(),nullable=False)
    due_date=Column(Date,nullable=False)
    status=Column(Enum(TaskStatus),default=TaskStatus.PENDING,nullable=False)

engine=create_async_engine(DATABASE_URL)
async_session_make=async_sessionmaker(engine,expire_on_commit=False)

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_async_session() -> AsyncGenerator[AsyncSession,None]:
    async with async_session_make() as session:
        yield session