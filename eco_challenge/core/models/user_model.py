from pydantic import EmailStr

from sqlmodel import SQLModel, Field, Relationship
# from .share_friends_model import ShareFriendGet, ShareFriend


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
    # share_friend: list[ShareFriend] = Relationship(back_populates='user')

