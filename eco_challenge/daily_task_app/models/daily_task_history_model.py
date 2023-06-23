import datetime

from sqlalchemy import Column, DateTime
from .daily_task_model import DailyTask, DailyTaskGet
from eco_challenge.core.models.user_model import User
from sqlmodel import SQLModel, Field, Relationship

from .user_response_model import UserResponse, UserResponseGet


class DailyTaskHistoryCreate(SQLModel):

    start_time: datetime.datetime = Field(
        default_factory=datetime.datetime.utcnow,
        sa_column=Column(DateTime(timezone=False)),
    )
    end_time: datetime.datetime | None = Field(
        default=None,
        sa_column=Column(DateTime(timezone=False)),
    )
    is_completed: bool = False
    task_id: int = Field(foreign_key='daily_task.task_id')


class DailyTaskHistoryGet(DailyTaskHistoryCreate):
    task_history_id: int
    daily_task: DailyTaskGet
    user_response: UserResponseGet | None
    user_id: int


class DailyTaskHistory(DailyTaskHistoryCreate, table=True):
    __tablename__ = 'daily_task_history'
    task_history_id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key='user.user_id')
    user: User = Relationship(back_populates='task_history')
    daily_task: DailyTask = Relationship(back_populates='task_history', sa_relationship_kwargs={'lazy': 'selectin'})
    user_response: UserResponse | None = Relationship(
        back_populates='task_history',
        sa_relationship_kwargs={
            'lazy': 'selectin',
            'uselist': False,
            'cascade': 'delete',
        },
    )
