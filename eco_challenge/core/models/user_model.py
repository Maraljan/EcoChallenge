import typing

from pydantic import EmailStr

from sqlmodel import SQLModel, Field, Relationship

from .points_count_model import PointsCount
from .points_transaction_model import PointsTransaction
from .role_model import Role

if typing.TYPE_CHECKING:
    from eco_challenge.daily_task_app.models.daily_task_history_model import DailyTaskHistory

Password = typing.NewType('Password', str)
HashedPassword = typing.NewType('HashedPassword', str)


class UserBase(SQLModel):
    username: str = Field(index=True)
    email: EmailStr = Field(index=True, unique=True)
    user_image: str | None = None
    phone_number: str | None = None


class UserCreate(UserBase):
    password: Password


class UserUpdate(UserCreate):
    pass


class UserGet(UserBase):
    user_id: int
    user_role: Role


class User(UserBase, table=True):
    __tablename__ = 'user'
    user_id: int | None = Field(default=None, primary_key=True)
    hashed_password: HashedPassword
    task_history: list['DailyTaskHistory'] = Relationship(
        back_populates='user',
        sa_relationship_kwargs={
            'cascade': 'delete',
        }
    )
    points_transactions: list['PointsTransaction'] = Relationship(
        back_populates='user',
        sa_relationship_kwargs={
            'cascade': 'delete',
        }
    )
    points_count: PointsCount = Relationship(back_populates='user')
    points_count_id: int = Field(foreign_key='points_count.points_count_id')
    role_id: int = Field(foreign_key='role.role_id')
    user_role: Role = Relationship(
        back_populates='users',
        sa_relationship_kwargs={'lazy': 'selectin'},
    )
