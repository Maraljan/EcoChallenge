import typing

from sqlmodel import SQLModel, Field, Relationship


class DailyTaskCreate(SQLModel):
    task: str = Field(index=True)
    task_detail: str
    points: int = 50


class DailyTaskGet(DailyTaskCreate):
    task_id: int


class DailyTask(DailyTaskCreate, table=True):
    task_id: int | None = Field(default=None, primary_key=True)
