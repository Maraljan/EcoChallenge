import datetime
import typing


from sqlmodel import SQLModel, Field, Relationship
if typing.TYPE_CHECKING:
    from .user_model import User


class PointsTransactionCreate(SQLModel):
    points: int = 0
    user_id: int = Field(foreign_key='user.user_id')


class PointsTransactionGet(PointsTransactionCreate):
    points_transaction_id: int
    create_at: datetime.datetime


class PointsTransaction(PointsTransactionCreate, table=True):
    __tablename__ = 'points_transaction'
    points_transaction_id: int | None = Field(default=None, primary_key=True)
    user: 'User' = Relationship(back_populates='points_transactions')
    create_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
