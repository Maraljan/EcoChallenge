import typing

if typing.TYPE_CHECKING:
    from .daily_task_history_model import DailyTaskHistory
from sqlmodel import SQLModel, Field, Relationship


class UserResponseCreate(SQLModel):
    response: str
    response_image: str
    task_history_id: int = Field(foreign_key='daily_task_history.task_history_id')


class ActionApprove(SQLModel):
    is_completed: bool = Field(default=False)
    user_response_id: int


class UserResponseGet(UserResponseCreate):
    user_response_id: int | None = Field(default=None, primary_key=True)


class UserResponse(UserResponseCreate, table=True):
    __tablename__ = 'user_response'
    user_response_id: int | None = Field(default=None, primary_key=True)
    task_history: 'DailyTaskHistory' = Relationship(
        back_populates='user_response',
        sa_relationship_kwargs={
            'lazy': 'selectin',
        }
    )
