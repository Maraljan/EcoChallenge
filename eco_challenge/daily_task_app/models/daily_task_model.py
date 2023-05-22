import typing

from sqlmodel import SQLModel, Field, Relationship

if typing.TYPE_CHECKING:
    from eco_challenge.daily_task_app.models.daily_task_history_model import DailyTaskHistory


class DailyTaskCreate(SQLModel):
    task: str = Field(index=True)
    task_detail: str
    points: int = 50


class DailyTaskGet(DailyTaskCreate):
    task_id: int


class DailyTask(DailyTaskCreate, table=True):
    __tablename__ = 'daily_task'
    task_id: int | None = Field(default=None, primary_key=True)
    task_history: list['DailyTaskHistory'] = Relationship(back_populates='daily_task')
