import typing

from pydantic import EmailStr

from sqlmodel import SQLModel, Field, Relationship

from .points_count_model import PointsCount
from .points_transaction_model import PointsTransaction

if typing.TYPE_CHECKING:
    from eco_challenge.daily_task_app.models.daily_task_history_model import DailyTaskHistory


class UserBase(SQLModel):
    username: str = Field(index=True)
    email: EmailStr = Field(index=True, unique=True)
    user_image: str | None = None
    phone_number: str | None = None


class UserCreate(UserBase):
    password: str


class UserUpdate(UserCreate):
    pass


class UserGet(UserBase):
    user_id: int


class User(UserGet, table=True):
    __tablename__ = 'user'
    user_id: int | None = Field(default=None, primary_key=True)
    hashed_password: str
    task_history: list['DailyTaskHistory'] = Relationship(back_populates='user')
    points_transactions: list['PointsTransaction'] = Relationship(back_populates='user')
    points_count: PointsCount = Relationship(back_populates='user')
    points_count_id: int = Field(foreign_key='points_count.points_count_id')

