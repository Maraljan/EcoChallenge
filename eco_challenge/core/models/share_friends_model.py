import typing

from sqlmodel import SQLModel, Field, Relationship


if typing.TYPE_CHECKING:
    from .user_model import User


class ShareFriendCreate(SQLModel):
    is_shared: bool = False
    # user_id: int = Field(foreign_key='user.user_id')


class ShareFriendGet(ShareFriendCreate):
    share_friend_id: int


class ShareFriend(ShareFriendGet, table=True):
    __tablename__ = 'share_friend_create'
    share_friend_id: int | None = Field(default=None, primary_key=True)
    # user: 'User' = Relationship(back_populates='share_friend')

