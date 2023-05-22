import typing

from pydantic import EmailStr

from sqlmodel import SQLModel, Field, Relationship
# from .share_friends_model import ShareFriendGet, ShareFriend
if typing.TYPE_CHECKING:
    from eco_challenge.daily_task_app.models.daily_task_history_model import DailyTaskHistory


class UserBase(SQLModel):
    username: str = Field(index=True)
    email: EmailStr = Field(index=True, unique=True)


class UserCreate(UserBase):
    password: str


class UserUpdate(UserCreate):
    pass


class UserGet(UserBase):
    user_id: int
    # share_friend: list[ShareFriendGet] = []


class User(UserGet, table=True):
    user_id: int | None = Field(default=None, primary_key=True)
    hashed_password: str
    task_history: list['DailyTaskHistory'] = Relationship(back_populates='user')

